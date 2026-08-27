# This code is created by C-Firefly
#
# GitHub: https://c-firefly.github.io

📦 Telegram Backup Uploader for Termux

A simple Python-based backup system for Termux that scans files from a selected folder and uploads them to a Telegram Channel using a Telegram Bot.

The system keeps a local record of uploaded files and stores metadata about uploaded files so that the same files can be skipped during future backups.

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
- 📱 Designed for Termux/Android

---

🎯 Use Cases

This project can be useful if you want to:

📱 1. Backup Android files

You can use Termux to backup files from your Android storage to a private Telegram Channel.

Example:

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

🗂️ 2. Backup specific folders

You can configure the backup directory to scan folders such as:

/storage/emulated/0/DCIM
/storage/emulated/0/Documents
/storage/emulated/0/Download
/storage/emulated/0/Pictures

You can also scan the complete Termux storage directory.

---

💾 3. Personal cloud-style backup

A Telegram private channel can be used as a simple remote storage destination.

The bot uploads files to the channel while "backup_state.json" and "database.json" keep track of uploaded files.

---

🔄 4. Re-run backups on schedule without uploading everything again

After a successful upload, the file path is stored in:

backup_state.json

When the backup runs again, previously uploaded files can be skipped.

---

🔄 5. Schedule uploaded.

When you run backup.py the system starts uploading your files and wait for next schedule.

File auto upload schedule is 00 a.m., 6 a.m., 12 p.m. and 18 p.m.

System will automatically detect files and upload.
The system also have duplicate detection to prevent duplicate files.

---

⚠️ File Size Limit

The backup system has a configurable maximum file size.

The default configuration is:

50 MB

Files larger than the configured limit are skipped.

Example:

photo.jpg      → Upload
video.mp4      → Upload
large_file.zip → Skip

The limit is controlled through:

config.BACKUP_SETTINGS["MAX_FILE_SIZE_MB"]

---

📋 Requirements

You need:

- Android phone
- Termux
- Python 3
- Telegram account
- Telegram Bot
- Telegram Channel

Recommended:

- Private Telegram Channel
- Dedicated bot for backup
- Stable internet connection
- Enough Telegram storage/quota for your use case

---

🤖 Create Telegram Bot

Open Telegram and search for:

@BotFather

Create a new bot:

/newbot

Follow the instructions.

BotFather will provide a token similar to:

123456789:AAxxxxxxxxxxxxxxxxxxxxxxxxxxxx

Keep this token private.

---

📢 Create Telegram Channel

Create a Telegram Channel for storing backups.

Recommended:

Private Channel

Add your bot as an administrator.

The bot needs permission to post messages/documents in the channel.

---

🔑 Get Channel ID

The channel ID must be placed in your configuration.

For a private Telegram channel, it commonly looks like:

-100xxxxxxxxxxxx

Make sure the bot has permission to send documents to the channel.

---

⚙️ Configuration

The project uses a "config.py" file.

Example:

BOT_TOKEN = "YOUR_BOT_TOKEN"

PRIVATE_CHANNEL_ID = -100**********

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

---

📥 Installation

1. Install Termux

Install Termux from a trusted source such as F-Droid or the official Termux project.

Do not use an outdated Termux version if possible.

---

2. Update packages

Open Termux and run:

pkg update -y
pkg upgrade -y

---

3. Install Backup System

pkg install git -y

Clone repository:

git clone https://github.com/C-Firefly/Telegram-Backup-System

Change directory:

cd Telegram-Backup-System

bash install.sh

---

🔐 Security

Do not upload or publish your bot token to GitHub.

Bad:

BOT_TOKEN = "123456789:AAxxxxxxxx"

inside a public repository.

Better:

config.py

should be excluded from Git.

Add:

config.py

to ".gitignore".

For a public GitHub repository, an even better solution is to use environment variables or a ".env" file.

---

📁 Project Structure

A basic project can look like:

telegram-backup/
│
├── backup.py
├── config.py
├── install.sh
├── backup_state.json
├── database.json
├── .gitignore
└── README.md

---

💾 Local Backup Files

backup_state.json

This file stores information about files that have already been uploaded.

Example:

[
    "/storage/shared/DCIM/photo.jpg",
    "/storage/shared/Documents/file.pdf"
]

The purpose is to prevent unnecessary duplicate uploads.

Important

If "backup_state.json" does not exist, the program starts with an empty state.

It can be created automatically after a successful upload.

---

database.json

This file stores metadata about uploaded files.

Example:

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

- Device name
- Folder
- File name
- File size
- Upload date
- Telegram message ID
- Telegram file ID

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
12. Check scheduled
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

The program checks paths against the configured ignored folder names.

---

🔁 Duplicate Prevention

Duplicate prevention is controlled by:

"REMOVE_DUPLICATES": True

When enabled, the program checks whether the file path already exists in:

backup_state.json

If it exists:

Duplicate → Skip

If it does not exist:

New file → Upload

---

⚠️ Current Limitations

The current version is intentionally simple.

1. Path-based duplicate detection

The current duplicate system checks the file path, not the actual file contents.

For example:

/storage/shared/DCIM/photo.jpg

is considered uploaded because that exact path exists in the state.

If the same file is copied to:

/storage/shared/Backup/photo.jpg

it may be uploaded again.

---

2. File modification is not detected

If a previously uploaded file is modified but keeps the same path, the current system may still consider it uploaded.

---

3. JSON database

The database uses:

database.json

This is simple and easy to understand, but it is not ideal for very large backup systems.

SQLite would be a better option for larger projects.

---

🚀 New Updates:

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

This is especially useful for temporary Telegram/network problems.

---

🕐 4. Scheduled Backup

The system could automatically run:

Every 6 hours
Every day at 00,06,12,18

---

🚀 Recommended Future Updates

The project can be improved significantly.

---

🧮 1. Hash-Based Duplicate Detection

Instead of checking only:

file path

calculate a file hash such as:

SHA-256

Then:

File A → SHA256 = XXXXX
File B → SHA256 = XXXXX

means they are identical.

This would provide much better duplicate detection.

---

📝 2. Better Error Handling

Instead of generic:

except Exception:

use specific exceptions where possible.

For example:

PermissionError
FileNotFoundError
JSONDecodeError
Telegram API errors
Network errors
Timeout errors

This makes debugging easier.

---

📊 3. Progress Bar

Instead of only:

Uploading: video.mp4

the program could show:

video.mp4
██████████████░░░░░░ 72%

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

A future version could allow commands such as:

/start
/backup
/status
/cancel
/files
/get filename

This would allow the backup system to be controlled from Telegram.

---

📂 6. Multiple Backup Folders

Instead of one:

STORAGE_DIR

support:

BACKUP_FOLDERS = [
    "/storage/shared/DCIM",
    "/storage/shared/Documents",
    "/storage/shared/Download"
]

---

🛡️ Recommended Security Improvements

For production/public use:

- Never expose "BOT_TOKEN"
- Use environment variables
- Keep "config.py" out of Git
- Use a private Telegram Channel
- Restrict who can access the backup channel
- Avoid storing sensitive information unnecessarily
- Consider encrypting sensitive files before uploading

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

📌 Important Note

This project is intended primarily as a personal backup utility.

Telegram is being used as the remote destination, while Termux performs the local file scanning and upload operations.

The current version is simple and can be extended into a more advanced backup system with:

- Multi-device support
- Telegram remote control
- File hashing
- SQLite
- Automatic scheduling
- Retry system
- Resume support
- Backup history
- File search
- Restore/download functionality

---
Hope you have a great day.