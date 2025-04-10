# Multiplayer-Format Converter

## Overview

The Multiplayer-Format Converter is a web application that allows users to convert multimedia files (MP4, GIF, MP3) into various formats. It utilizes the FFmpeg library for conversion and provides a user-friendly interface for selecting the desired output format.

## Features

*   **File Conversion:** Supports converting between MP4, GIF, and MP3 formats.
*   **Format Options:** Offers a range of target formats, including:
    *   **MP4:** H.264 (Default), H.265, H.264 (Advanced), 1080p, 720p
    *   **MP3:** Default (192kbps), 128kbps, 192kbps, 320kbps
    *   **GIF:** Conversion of video snippets to animated GIFs
*   **Progress Bar:** Visual progress indicator during the conversion process.
*   **Download History:** Keeps track of downloaded converted files.
*   **Error Handling:** Displays error messages for failed conversions.
*   **Logging:** Logs successful and failed conversions for debugging purposes.

## Technologies Used

*   **Backend:**
    *   Python
    *   Flask (web framework)
    *   FFmpeg (multimedia framework)
    *   uuid (for generating unique filenames)
    *   logging (for tracking conversion status)
*   **Frontend:**
    *   HTML
    *   CSS
    *   JavaScript

## Installation

1.  **Prerequisites:**
    *   Python 3.x
    *   FFmpeg (installed and added to your system's PATH)

2.  **Clone the repository:**

    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

3.  **Create a virtual environment (recommended):**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate  # On Windows
    ```

4.  **Install the dependencies:**

    ```bash
    pip install Flask
    ```

5.  **Run the application:**

    ```bash
    python python.py
    ```

    This will start the Flask development server. By default, it will run on `http://127.0.0.1:5000/`.

## Configuration

*   **`UPLOAD_FOLDER`:**  Specifies the directory where uploaded files and converted files are stored (default: `"uploads"`).  This directory will be automatically created if it doesn't exist.  You can modify this in `app.py`.

## Usage

1.  **Access the web application:** Open your web browser and navigate to the address where the Flask application is running (e.g., `http://127.0.0.1:5000/`).

2.  **Upload a file:** Use the file input field to select the file you want to convert.  Supported file types are MP4, GIF, and MP3.

3.  **Select a target format:** Choose the desired output format from the dropdown menu.

4.  **Click the "Convert" button:** This will start the conversion process.

5.  **Progress indication:** A progress bar will appear, indicating the progress of the conversion.

6.  **Download the converted file:** Once the conversion is complete, the file will be automatically downloaded.  The download will also be added to the "Download History" list.

7.  **Clear History:**  The "Clear History" button will clear the download history list.

8.  **Error Handling:** If the conversion fails, an error message will be displayed in a popup.

## FFmpeg Setup

This application requires FFmpeg to be installed on your system and accessible via the command line.

**Installation Instructions (General):**

1.  Download FFmpeg from the official website: [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html)

2.  Extract the downloaded archive.

3.  Add the FFmpeg `bin` directory to your system's `PATH` environment variable.

**Specific Instructions (Examples):**

*   **Linux (Ubuntu/Debian):**

    ```bash
    sudo apt update
    sudo apt install ffmpeg
    ```

*   **macOS (using Homebrew):**

    ```bash
    brew install ffmpeg
    ```

*   **Windows:**
    1.  Download the appropriate FFmpeg build from [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html). Choose the build that matches your system architecture (32-bit or 64-bit).
    2.  Extract the downloaded archive to a directory (e.g., `C:\ffmpeg`).
    3.  Add the `bin` directory inside the extracted folder (e.g., `C:\ffmpeg\bin`) to your system's `PATH` environment variable:
        *   Open "System Properties" (search for "environment variables" in the Start Menu).
        *   Click "Environment Variables...".
        *   In the "System variables" section, find the "Path" variable and click "Edit...".
        *   Click "New" and add the path to the `bin` directory (e.g., `C:\ffmpeg\bin`).
        *   Click "OK" on all dialogs.
    4.  Restart your command prompt or terminal for the changes to take effect.

**Verification:**

After installing FFmpeg, open a command prompt or terminal and run:

```bash
ffmpeg -version
```

If FFmpeg is correctly installed and configured, you should see the FFmpeg version information.

## Project Structure

```
Multiplayer-Format Converter/
├── python.py              # Main Flask application file
├── index.html          # HTML template for the user interface
├── static/             # Static files (CSS, JavaScript, images)
│   ├── styles.css      # CSS stylesheet
│   ├── script.js       # JavaScript file
│   └── black.png       # Black image used for audio-to-video conversion
├── uploads/            # Directory for uploaded and converted files
├── conversion.log      # Log file for conversion processes
└── README.md           # This file
```

## Logging

The application logs conversion events (successes and failures) to the `conversion.log` file.  This log can be useful for troubleshooting issues.

## Deployment

This application can be deployed to various platforms, such as:

*   **Heroku:** A cloud platform that supports Python applications.
*   **AWS Elastic Beanstalk:** A cloud platform from Amazon Web Services for deploying and managing web applications.
*   **Google App Engine:** A cloud platform from Google Cloud for deploying and scaling web applications.
*   **Docker:** Containerize the application for easy deployment and portability.

Specific deployment instructions will vary depending on the platform you choose.

## Contributing

Contributions are welcome!  If you find a bug or have a suggestion for improvement, please open an issue or submit a pull request.

## License

none
