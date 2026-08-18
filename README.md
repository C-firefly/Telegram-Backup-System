📦 Telegram Backup System

«Telegram Backup Uploader for Termux»

A simple Python-based backup system for Termux/Android that scans files from a selected folder and uploads them to a Telegram Channel using a Telegram Bot.

The system keeps a local record of uploaded files and stores metadata about uploaded files so that the same files can be skipped during future backups.

---

👨‍💻 Author

C-Firefly

- 🌐 GitHub: https://github.com/C-Firefly
- 🌐 Portfolio: https://c-firefly.github.io

---

✨ Features

- 📂 Automatic folder scanning
- 📤 Upload files to a Telegram Channel
- 🤖 Telegram Bot API based
- 🔁 Duplicate upload prevention
- 🗂️ Folder-aware backup
- 📋 File metadata in Telegram captions
- 💾 Local backup state tracking
- 🗃️ JSON database/index
- 🚫 Ignore selected folders
- 📏 Configurable maximum file size
- ⏱️ Configurable upload delay
- 📊 Backup completion statistics
- 🕐 Automatic scheduled backup
- 📱 Designed for Termux/Android

---

🎯 Use Cases

📱 1. Backup Android Files

You can use Termux to backup files from your Android storage to a private Telegram Channel.

Android Storage
      │
      ▼
   Termux
      │
      ▼
Telegram Bot
      │
      ▼
Private Telegram Channel

---

🗂️ 2. Backup Specific Folders

You can configure the backup directory to scan folders such as:

/storage/emulated/0/DCIM
/storage/emulated/0/Documents
/storage/emulated/0/Download
/storage/emulated/0/Pictures

You can also scan the complete Termux shared storage directory.

---

💾 3. Personal Cloud-Style Backup

A Telegram private channel can be used as a simple remote storage destination.

The bot uploads files to the channel while:

backup_state.json
database.json

keep track of uploaded files and their metadata.

---

🔄 4. Re-run Backups Without Uploading Everything Again

After a successful upload, the file path is stored in:

backup_state.json

When the backup runs again, previously uploaded files can be skipped.

---

🕐 5. Automatic Scheduled Backup

The backup scheduler can automatically run at:

00:00
06:00
12:00
18:00

When you run:

python backup.py

the system starts the scheduler and performs the backup according to the configured schedule.

The system also performs duplicate detection to prevent unnecessary uploads.

---

⚠️ File Size Limit

The backup system has a configurable maximum file size.

The default configuration is:

50 MB

Files larger than the configured limit are skipped.

Example

photo.jpg       → Upload
video.mp4       → Upload
large_file.zip  → Skip

The limit is controlled through:

BACKUP_SETTINGS["MAX_FILE_SIZE_MB"]

---

📋 Requirements

You need:

- 📱 Android phone
- 📦 Termux
- 🐍 Python 3
- 📱 Telegram account
- 🤖 Telegram Bot
- 📢 Telegram Channel
- 🌐 Internet connection

Recommended

- 🔒 Private Telegram Channel
- 🤖 Dedicated bot for backup
- 🌐 Stable internet connection
- 💾 Enough available Telegram storage/quota for your use case

---

🤖 Create Telegram Bot

Open Telegram and search for:

@BotFather

Start a conversation with BotFather and use:

/newbot

Follow the instructions.

BotFather will provide a token similar to:

123456789:AAxxxxxxxxxxxxxxxxxxxxxxxxxxxx

«⚠️ Keep this token private. Never publish your bot token on GitHub.»

If your token is accidentally exposed, immediately revoke/regenerate it through BotFather.

---

📢 Create Telegram Channel

Create a Telegram Channel for storing your backups.

Recommended

Private Channel

Add your Telegram bot as an Administrator.

The bot needs permission to send/post documents and messages to the channel.

---

🔑 Get Channel ID

The channel ID must be placed in your configuration.

For a private Telegram Channel, the ID commonly looks like:

-100xxxxxxxxxxxx

Make sure the bot has permission to send documents to the channel.

«⚠️ Do not publish your real Channel ID together with your bot token in a public repository if you want to keep the backup destination private.»

---

⚙️ Configuration

The project uses a:

config.py

file for configuration.

Example

BOT_TOKEN = "YOUR_BOT_TOKEN"

PRIVATE_CHANNEL_ID = -1001234567890

DEVICE_NAME = "My-Android"

STORAGE_DIR = "/data/data/com.termux/files/home/storage/shared"

IGNORE_FOLDERS = [
    "Android/data",
    "Android/obb",
    ".cache"
]

BACKUP_SETTINGS = {
    "MAX_FILE_SIZE_MB": 50,
    "REMOVE_DUPLICATES": True,
    "UPLOAD_DELAY": 1
}

Configuration Options

Option| Description
"BOT_TOKEN"| Telegram Bot API token
"PRIVATE_CHANNEL_ID"| Destination Telegram Channel ID
"DEVICE_NAME"| Name used to identify the device
"STORAGE_DIR"| Directory that will be scanned
"IGNORE_FOLDERS"| Folders that should be skipped
"MAX_FILE_SIZE_MB"| Maximum allowed file size
"REMOVE_DUPLICATES"| Enable/disable duplicate detection
"UPLOAD_DELAY"| Delay between uploads

---

📥 Installation

1. Install Termux

Install Termux from a trusted source such as F-Droid or the official Termux project.

«⚠️ Avoid using an outdated Termux version if possible.»

---

2. Update Packages

Open Termux and run:

pkg update -y
pkg upgrade -y

---

3. Install Git

pkg install git -y

---

4. Clone the Repository

git clone https://github.com/C-Firefly/Telegram-Backup-System

---

5. Enter the Project Directory

cd Telegram-Backup-System

---

6. Run the Installer

bash install.sh

The installer will prepare the required environment for the backup system.

---

📱 Termux Storage Permission

If the program needs access to Android shared storage, run:

termux-setup-storage

When Android asks for storage permission, allow it.

After granting permission, Termux normally provides access through:

~/storage/shared

For example:

~/storage/shared/DCIM
~/storage/shared/Download
~/storage/shared/Documents

«💡 Make sure "STORAGE_DIR" in "config.py" matches the directory you actually want to scan.»

---

🔐 Security

🚨 Never Publish Your Bot Token

Do not upload your real token to GitHub.

❌ Bad

BOT_TOKEN = "123456789:AAxxxxxxxxxxxxxxxx"

Do not commit a real token inside a public repository.

---

✅ Better

Keep your private configuration separate:

config.py

and add it to:

.gitignore

Example:

config.py

You can also use environment variables or a ".env" file for better secret management.

---

📁 Project Structure

A basic project structure looks like:

Telegram-Backup-System/
│
├── backup.py
├── config.py
├── install.sh
├── backup_state.json
├── database.json
├── .gitignore
└── README.md

«⚠️ If "config.py" contains your real bot token, keep it excluded from Git.»

---

💾 Local Backup State

"backup_state.json"

This file stores information about files that have already been uploaded.

Example

[
    "/storage/shared/DCIM/photo.jpg",
    "/storage/shared/Documents/file.pdf"
]

The purpose is to prevent unnecessary duplicate uploads.

Important

If:

backup_state.json

does not exist, the program starts with an empty state.

The file can be created automatically after a successful upload.

---

🗃️ Database

"database.json"

This file stores metadata about uploaded files.

Example

{
    "My-Android": {
        "DCIM": [
            {
                "name": "photo.jpg",
                "folder": "DCIM",
                "size_mb": 2.45,
                "date": "2026-08-16 20:30:00",
                "message_id": 123,
                "file_id": "xxxxxxxx"
            }
        ]
    }
}

The database contains information such as:

- 📱 Device name
- 📂 Folder
- 📄 File name
- 📏 File size
- 📅 Upload date
- 📨 Telegram message ID
- 🆔 Telegram file ID

---

▶️ Run Backup

Run:

python backup.py

The program will:

1. Load the configuration
2. Connect to Telegram
3. Load previous upload state
4. Scan the backup directory
5. Ignore configured folders
6. Check duplicate files
7. Check file size
8. Generate metadata
9. Upload the file
10. Save Telegram information
11. Update local state
12. Check the schedule
13. Continue scanning

---

📝 Telegram Caption

Each uploaded file receives metadata similar to:

#BACKUP

DEVICE=My-Android
FOLDER=DCIM
FILE=photo.jpg
SIZE=2.45MB
DATE=2026-08-16 20:30:00

This makes it easier to identify where a file came from.

---

📊 Backup Output

The terminal displays progress similar to:

================================
⏰ BACKUP SCHEDULER STARTED
================================
📁 Folder: /storage/emulated/0
🕐 Schedule: 00:00, 06:00, 12:00, 18:00
▶️ Running initial backup now...

================================
📦 BACKUP STARTED
================================
📁 Folder: /storage/emulated/0

📤 Uploading: photo.jpg
✅ Uploaded: photo.jpg

📤 Uploading: document.pdf
✅ Uploaded: document.pdf

================================
✅ BACKUP COMPLETED
================================

Uploaded : 2
Duplicate: 5
Large    : 1
Failed   : 0

---

🚫 Ignoring Folders

Folders can be excluded using:

IGNORE_FOLDERS = [
    "Android/data",
    "Android/obb",
    ".cache"
]

The program checks file paths against the configured ignored folder names.

---

🔁 Duplicate Prevention

Duplicate prevention is controlled by:

"REMOVE_DUPLICATES": True

When enabled, the program checks whether the file path already exists in:

backup_state.json

If the path exists

Duplicate → Skip

If the path does not exist

New file → Upload

---

⚠️ Current Limitations

The current version is intentionally simple.

1. Path-Based Duplicate Detection

The current duplicate system checks the file path, not the actual file contents.

For example:

/storage/shared/DCIM/photo.jpg

is considered uploaded because that exact path exists in the state.

If the same file is copied to:

/storage/shared/Backup/photo.jpg

it may be uploaded again.

---

2. File Modification Is Not Detected

If a previously uploaded file is modified but keeps the same path, the current system may still consider it uploaded.

---

3. JSON Database

The database currently uses:

database.json

This is simple and easy to understand, but it is not ideal for very large backup systems.

For larger projects, SQLite would be a better option.

---

🚀 Planned Improvements

The project can be improved significantly.

🔄 1. Retry Failed Uploads

Instead of immediately marking an upload as failed:

Upload failed
      ↓
Wait
      ↓
Retry
      ↓
Retry again
      ↓
Failed

For example:

Maximum retries = 3

---

🛑 2. KeyboardInterrupt Handling

The main program can handle:

KeyboardInterrupt

so pressing:

CTRL + C

does not produce a confusing traceback.

A graceful shutdown could display:

🛑 Backup interrupted by user.

Uploaded : 25
Failed   : 1
Skipped  : 4

State saved.

---

⏳ 3. Automatic Retry + Backoff

A better retry system could use:

Attempt 1
   ↓
2 seconds
   ↓
Attempt 2
   ↓
5 seconds
   ↓
Attempt 3

This is especially useful for temporary Telegram or network problems.

---

🕐 4. Scheduled Backup

The scheduler can automatically run:

00:00
06:00
12:00
18:00

or every six hours depending on the implementation.

---

🚀 Recommended Future Updates

🧮 1. Hash-Based Duplicate Detection

Instead of checking only:

file path

the system could calculate a file hash such as:

SHA-256

For example:

File A → SHA256 = XXXXX
File B → SHA256 = XXXXX

If both hashes are identical, the files are likely identical.

This would provide much better duplicate detection than path-based checking.

---

📝 2. Better Error Handling

Instead of using only:

except Exception:

the system could use specific exceptions where appropriate.

For example:

PermissionError
FileNotFoundError
JSONDecodeError
Telegram API errors
Network errors
Timeout errors

This makes debugging and error reporting easier.

---

📊 3. Progress Bar

Instead of only displaying:

Uploading: video.mp4

the program could show:

video.mp4
██████████████░░░░░░ 72%

This would make large uploads easier to monitor.

---

🗃️ 4. SQLite Database

For a larger backup system:

database.json

could be replaced with:

backup.db

using SQLite.

This would make searching and managing thousands of files much easier.

---

📱 5. Telegram Bot Control

A future version could support commands such as:

/start
/backup
/status
/cancel
/files
/get filename

This would allow the backup system to be controlled remotely through Telegram.

---

📂 6. Multiple Backup Folders

Instead of supporting only:

STORAGE_DIR

a future version could support:

BACKUP_FOLDERS = [
    "/storage/shared/DCIM",
    "/storage/shared/Documents",
    "/storage/shared/Download"
]

This would allow different folders to be backed up independently.

---

🛡️ Recommended Security Improvements

For production or public use:

- 🔐 Never expose "BOT_TOKEN"
- 🔑 Use environment variables for secrets
- 🚫 Keep "config.py" out of Git
- 🔒 Use a private Telegram Channel
- 👥 Restrict who can access the backup channel
- 🧹 Avoid storing sensitive information unnecessarily
- 🔐 Consider encrypting sensitive files before uploading
- 🔄 Regenerate the bot token immediately if it is exposed

---

🧠 How the System Works

              Android Storage
                    │
                    ▼
                 Termux
                    │
                    ▼
              Python Script
                    │
          ┌─────────┴─────────┐
          │                   │
     Check State         Check File Size
          │                   │
          └─────────┬─────────┘
                    │
                    ▼
             Telegram Bot API
                    │
                    ▼
          Private Telegram Channel
                    │
          ┌─────────┴─────────┐
          │                   │
   backup_state.json     database.json

---

🔄 Backup Workflow

Start
  │
  ▼
Load Configuration
  │
  ▼
Load Backup State
  │
  ▼
Scan Files
  │
  ▼
Check Ignored Folder
  │
  ├── Yes → Skip
  │
  └── No
       │
       ▼
Check File Size
       │
       ├── Too Large → Skip
       │
       └── Valid
            │
            ▼
     Check Duplicate
            │
       ├── Duplicate → Skip
       │
       └── New File
            │
            ▼
      Upload to Telegram
            │
            ▼
      Save File Metadata
            │
            ▼
     Update Backup State
            │
            ▼
       Next File

---

📌 Important Notes

This project is intended primarily as a personal backup utility.

Telegram is used as the remote destination, while Termux performs local file scanning and upload operations.

The current version is simple and can be extended into a more advanced backup system with:

- 📱 Multi-device support
- 🤖 Telegram remote control
- 🧮 File hashing
- 🗃️ SQLite database
- 🕐 Automatic scheduling
- 🔄 Retry system
- ▶️ Resume support
- 📊 Backup history
- 🔎 File search
- 📥 Restore/download functionality
- 🔐 File encryption

---

⚡ Quick Start

If Termux is already installed, you can start with:

pkg update -y && pkg upgrade -y
pkg install git -y
termux-setup-storage
git clone https://github.com/C-Firefly/Telegram-Backup-System
cd Telegram-Backup-System
bash install.sh

Then configure your Telegram Bot and Channel in:

config.py

Finally run:

python backup.py

---

⭐ Support the Project

If you find this project useful:

- ⭐ Star the repository
- 🐛 Report bugs
- 💡 Suggest improvements
- 🔧 Contribute code
- 📢 Share the project

---

📜 License

This project is provided for personal and educational use.

Please check the repository for the current license and usage terms.

---

❤️ Thank You

Thanks for checking out Telegram Backup System.

Hope you have a great day! 🚀