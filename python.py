from flask import Flask, request, send_file, make_response, render_template_string
import os
import uuid
import subprocess
import logging

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


logging.basicConfig(
    filename='conversion.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

ALLOWED_EXTENSIONS = {'mp4', 'gif', 'mp3'} 

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template_string(open("index.html").read())

@app.route('/convert', methods=['POST'])
def convert():
    file = request.files['file']
    target_format = request.form['format']
    original_filename = file.filename

    if file and allowed_file(original_filename):
        
        file_extension = original_filename.rsplit('.', 1)[1].lower()
        input_filename = str(uuid.uuid4()) + "." + file_extension
        input_path = os.path.join(UPLOAD_FOLDER, input_filename)
        file.save(input_path)

        output_ext = target_format.split('-')[0]  
        output_filename = input_filename.rsplit('.', 1)[0] + "." + output_ext
        output_path = os.path.join(UPLOAD_FOLDER, output_filename)

        
        try:
            cmd = []  

            if file_extension == "mp4":
                if target_format == "gif":
                    cmd = ["ffmpeg", "-i", input_path, "-t", "5", "-vf", "fps=10,scale=320:-1:flags=lanczos", output_path]
                elif target_format == "mp3":
                    cmd = ["ffmpeg", "-i", input_path, "-q:a", "0", output_path]
                elif target_format == "mp4-h265":
                    cmd = ["ffmpeg", "-i", input_path, "-c:v", "libx265", "-x265-params", "crf=28", "-tag:v", "hvc1", "-c:a", "copy", output_path] 
                elif target_format == "mp4-h264":
                    cmd = ["ffmpeg", "-i", input_path, "-c:v", "libx264", "-preset", "medium", "-crf", "23", "-c:a", "aac", "-b:a", "128k", output_path] 
                elif target_format == "mp4-1080p":
                    cmd = ["ffmpeg", "-i", input_path, "-vf", "scale=1920:1080", "-c:a", "copy", output_path] 
                elif target_format == "mp4-720p":
                    cmd = ["ffmpeg", "-i", input_path, "-vf", "scale=1280:720", "-c:a", "copy", output_path]  
                    return "Unsupported MP4 conversion", 400

            elif file_extension == "gif":
                if target_format == "mp4":
                    cmd = ["ffmpeg", "-i", input_path, "-movflags", "faststart", "-pix_fmt", "yuv420p", "-vf", "scale=trunc(iw/2)*2:trunc(ih/2)*2", output_path]
                elif target_format == "mp4-x265":  
                    cmd = ["ffmpeg", "-i", input_path, "-c:v", "libx265", "-crf", "28", output_path]
                else:
                    return "Unsupported GIF conversion", 400

            elif file_extension == "mp3":
                if target_format == "mp4":
                    cmd = ["ffmpeg", "-loop", "1", "-i", "static/black.png", "-i", input_path, "-c:v", "libx264", "-tune", "stillimage", "-c:a", "aac", "-b:a", "192k", "-shortest", output_path]
                elif target_format == "mp3-128k":
                    cmd = ["ffmpeg", "-i", input_path, "-vn", "-acodec", "libmp3lame", "-ab", "128k", output_path] 
                elif target_format == "mp3-192k":
                    cmd = ["ffmpeg", "-i", input_path, "-vn", "-acodec", "libmp3lame", "-ab", "192k", output_path] 
                elif target_format == "mp3-320k":
                    cmd = ["ffmpeg", "-i", input_path, "-vn", "-acodec", "libmp3lame", "-ab", "320k", output_path] 
                    return "Unsupported MP3 conversion", 400

            else:
                return "Unsupported conversion", 400

            subprocess.run(cmd, check=True)
            logging.info(f"SUCCESS: {original_filename} ➜ {output_filename}")

        except subprocess.CalledProcessError as e:
            logging.error(f"FAILED: {original_filename} ➜ {output_filename} | {e}")
            os.remove(input_path)
            return f"Conversion failed: {e}", 500

        response = make_response(send_file(output_path, as_attachment=True))
        response.headers["X-Filename"] = output_filename

        os.remove(input_path)
        return response
    else:
        return "Invalid file or extension", 400

if __name__ == "__main__":
    app.run(debug=True)
