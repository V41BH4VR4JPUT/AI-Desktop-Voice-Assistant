# AI Desktop Voice Assistant 🗣️

An intelligent voice-controlled desktop assistant built with Python. It helps you automate tasks, fetch information, and control your system — all through voice commands!

## 🚀 Features
- **Voice Command Processing**: Execute commands via voice.
- **Text-to-Speech**: Get responses through speech.
- **App Management**: Open apps.
- **Web Search**: Fetch online information.


## 🏗️ Project Structure
```
v41bh4vr4jput-ai-desktop-voice-assistant/
├── README.md                  # Project documentation
├── Main.py                    # Main script for the voice assistant
└── tempCodeRunnerFile.py      # Temporary file to get the input microphone index
```

## 🛠️ Tech Stack
- **Python** (Core language)
- **SpeechRecognition** (Voice input)
- **PyAudio** (Microphone access)
- **pyttsx3** (Text-to-speech)

## 📥 Installation
1. **Clone the Repository:**
```bash
git clone https://github.com/your-username/v41bh4vr4jput-ai-desktop-voice-assistant.git
```
2. **Navigate to the Project Folder:**
```bash
cd v41bh4vr4jput-ai-desktop-voice-assistant
```
3. **Install Required Packages:**
```bash
pip install -r requirements.txt
```
4. **Run the Assistant:**
```bash
python Main.py
```

## 🧠 Troubleshooting
If you encounter **"No Default Input Device Available"** errors:
- Ensure your microphone is connected and set as the **default input device**.
- Optionally, set the device index in `Main.py`:
```python
with sr.Microphone(device_index=0) as source:
```

## 🛠️ Usage
Speak commands like:
- "Open Applications like Youtube , Google , StackOverflow etc."
- "Tell me the time"

The assistant listens, processes the command, and speaks the response! 🎯





