# Python TTS Downloader

A lightweight Python script to generate and download AI-powered text-to-speech (TTS) audio files by interfacing with third-party TTS endpoints. This tool supports various voice models and handles MP3 file saving automatically.

## 🎧 Features

* **Reverse API Integration:** Constructs custom payloads to interact with TTS services programmatically.
* **Proxy Support:** Implements dynamic proxy rotation to bypass rate limits during bulk generation.
* **Automated File Saving:** Automatically downloads and saves generated audio with unique filenames.
* **Customizable Parameters:** Allows configuration of voice models (e.g., "alloy", "fable") and speech speed.

## 🛠 Dependencies

* Python 3.x
* `requests`

## 🚀 Usage

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/yourusername/python-tts-downloader.git](https://github.com/yourusername/python-tts-downloader.git)
    cd python-tts-downloader
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configuration:**
    Open `main.py` and update your proxy credentials if needed (or run without proxies for small tests).

4.  **Run the script:**
    ```bash
    python main.py
    ```

## 📝 Code Example

The script mimics a valid browser request to generate audio:

```python
# Generating audio
generate_and_download("Hello world, this is a test.", voice="fable")
# Output: Saves 'audio_fable_1234.mp3' locally
