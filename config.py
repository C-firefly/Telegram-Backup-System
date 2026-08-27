# ==========================================
# TELEGRAM FULL STORAGE BACKUP CONFIGARATION
# ==========================================

BOT_TOKEN = "Your_Bot_Token"

# Private Telegram Channel ID
PRIVATE_CHANNEL_ID = -100**********


# Device Name
DEVICE_NAME = "My_Android"
#DEVICE_NAME = os.system("getprop ro.product.model")

# =========================================
# STORAGE PATHS
# =========================================

STORAGE_DIR = "/storage/emulated/0"

# =========================================
# BACKUP SETTINGS
# =========================================

BACKUP_SETTINGS = {

    # Skip files larger than this size
    "MAX_FILE_SIZE_MB": 50,

    # Scan subfolders recursively
    "SCAN_SUBFOLDERS": True,

    # Prevent duplicate uploads
    "REMOVE_DUPLICATES": True,

    # Delay between uploads
    "UPLOAD_DELAY": 2,

    # =================================
    # RETRY SETTINGS
    # =================================

    "MAX_RETRIES": 3,

    "RETRY_DELAY": 5,

    # =================================
    # SCHEDULER
    # =================================

    "SCHEDULE_ENABLED": True,
    "SCHEDULE_TIMES": [
        "00:00",
        "06:00",
        "12:00",
        "18:00"
    ]
}

# =========================================
# IGNORE FOLDERS
# =========================================

IGNORE_FOLDERS = [
    "Android/data",
    "Android/obb",
    ".thumbnails",
    "cache"
]