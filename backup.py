#==========================================
# Telegram Backup Uploader for Termux
# A simple Python-based backup system for Termux
#
# This code is created by C-Firefly
#
# GitHub: https://c-firefly.github.io
#==========================================


import os
import json
import asyncio
from datetime import datetime

from telegram import Bot
import config


# =========================================
# LOCAL DATABASE FILES
# =========================================

STATE_FILE = "backup_state.json"
DATABASE_FILE = "database.json"


# =========================================
# LOAD UPLOADED FILE STATE
# =========================================

def load_state():

    if not os.path.exists(STATE_FILE):
        return set()

    try:
        with open(STATE_FILE, "r") as f:
            return set(json.load(f))

    except Exception as e:

        print(f"⚠️ State load error: {e}")
        return set()


# =========================================
# SAVE UPLOADED FILE STATE
# =========================================

def save_state(uploaded_files):

    try:

        with open(STATE_FILE, "w") as f:
            json.dump(
                list(uploaded_files),
                f,
                indent=4
            )

    except Exception as e:

        print(f"⚠️ State save error: {e}")


# =========================================
# LOAD MAIN DATABASE
# =========================================

def load_database():

    if not os.path.exists(DATABASE_FILE):
        return {}

    try:

        with open(DATABASE_FILE, "r") as f:
            return json.load(f)

    except Exception as e:

        print(f"⚠️ Database load error: {e}")
        return {}


# =========================================
# SAVE DATABASE
# =========================================

def save_database(data):

    try:

        with open(DATABASE_FILE, "w") as f:
            json.dump(
                data,
                f,
                indent=4
            )

    except Exception as e:

        print(f"⚠️ Database save error: {e}")


# =========================================
# CHECK IGNORED FOLDERS
# =========================================

def is_ignored(path):

    for ignored in config.IGNORE_FOLDERS:

        if ignored.lower() in path.lower():
            return True

    return False


# =========================================
# UPDATE DATABASE INDEX
# =========================================

def update_database(device, folder, file_info):

    db = load_database()

    # Create device section
    if device not in db:
        db[device] = {}

    # Create folder section
    if folder not in db[device]:
        db[device][folder] = []

    # Add file info
    db[device][folder].append(file_info)

    save_database(db)


# =========================================
# UPLOAD FILE WITH RETRY
# =========================================

async def upload_file_with_retry(
    bot,
    file_path,
    caption
):

    max_retries = config.BACKUP_SETTINGS.get(
        "MAX_RETRIES",
        3
    )

    retry_delay = config.BACKUP_SETTINGS.get(
        "RETRY_DELAY",
        5
    )

    for attempt in range(1, max_retries + 1):

        try:

            with open(file_path, "rb") as f:

                message = await bot.send_document(
                    chat_id=config.PRIVATE_CHANNEL_ID,
                    document=f,
                    caption=caption
                )

            return message

        except asyncio.CancelledError:

            # User stopped the program
            raise

        except Exception as e:

            print(
                f"❌ Upload failed "
                f"(attempt {attempt}/{max_retries})"
            )

            print(f"   Error: {e}")

            # Last attempt
            if attempt >= max_retries:

                print("❌ Maximum retry reached.")

                return None

            # Exponential backoff
            delay = retry_delay * (2 ** (attempt - 1))

            print(
                f"🔄 Retrying in {delay} seconds..."
            )

            try:

                await asyncio.sleep(delay)

            except asyncio.CancelledError:

                raise

    return None


# =========================================
# MAIN BACKUP FUNCTION
# =========================================

async def run_backup(folder_path):

    bot = Bot(
        token=config.BOT_TOKEN
    )

    uploaded_files = load_state()

    uploaded_count = 0
    duplicate_count = 0
    skipped_large = 0
    failed_count = 0

    print("\n================================")
    print("📦 BACKUP STARTED")
    print("================================")

    print(f"📁 Folder: {folder_path}")

    try:

        # =====================================
        # WALK THROUGH FOLDERS
        # =====================================

        for root, dirs, files in os.walk(folder_path):

            # Skip ignored folders
            if is_ignored(root):
                continue

            for file_name in files:

                # =================================
                # CHECK KEYBOARD INTERRUPT
                # =================================

                full_path = os.path.join(
                    root,
                    file_name
                )

                # =================================
                # DUPLICATE CHECK
                # =================================

                if (
                    config.BACKUP_SETTINGS[
                        "REMOVE_DUPLICATES"
                    ]
                    and full_path in uploaded_files
                ):

                    duplicate_count += 1
                    continue

                # =================================
                # FILE SIZE CHECK
                # =================================

                try:

                    size_mb = (
                        os.path.getsize(full_path)
                        / (1024 * 1024)
                    )

                except Exception as e:

                    print(
                        f"⚠️ Cannot read file: "
                        f"{file_name}"
                    )

                    print(e)

                    failed_count += 1
                    continue

                if (
                    size_mb
                    > config.BACKUP_SETTINGS[
                        "MAX_FILE_SIZE_MB"
                    ]
                ):

                    skipped_large += 1

                    print(
                        f"⏭️ Skipped large file: "
                        f"{file_name} "
                        f"({round(size_mb, 2)} MB)"
                    )

                    continue

                # =================================
                # RELATIVE FOLDER
                # =================================

                relative_folder = os.path.relpath(
                    root,
                    folder_path
                )

                # Make root folder cleaner
                if relative_folder == ".":
                    relative_folder = "ROOT"

                # =================================
                # FILE METADATA
                # =================================

                upload_date = datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S"
                )

                caption = (
                    f"#BACKUP\n\n"
                    f"DEVICE={config.DEVICE_NAME}\n"
                    f"FOLDER={relative_folder}\n"
                    f"FILE={file_name}\n"
                    f"SIZE={round(size_mb, 2)}MB\n"
                    f"DATE={upload_date}"
                )

                print(
                    f"\n📤 Uploading: {file_name}"
                )

                # =================================
                # TELEGRAM UPLOAD
                # =================================

                message = await upload_file_with_retry(
                    bot,
                    full_path,
                    caption
                )

                # =================================
                # UPLOAD FAILED
                # =================================

                if message is None:

                    failed_count += 1

                    print(
                        f"❌ Failed permanently: "
                        f"{file_name}"
                    )

                    continue

                # =================================
                # SAVE TO DATABASE
                # =================================

                file_info = {

                    "name": file_name,

                    "folder": relative_folder,

                    "size_mb": round(
                        size_mb,
                        2
                    ),

                    "date": upload_date,

                    "message_id":
                        message.message_id,

                    "file_id":
                        message.document.file_id
                }

                update_database(
                    config.DEVICE_NAME,
                    relative_folder,
                    file_info
                )

                # =================================
                # SAVE STATE
                # =================================

                uploaded_files.add(
                    full_path
                )

                save_state(
                    uploaded_files
                )

                uploaded_count += 1

                print(
                    f"✅ Uploaded: {file_name}"
                )

                # =================================
                # UPLOAD DELAY
                # =================================

                delay = config.BACKUP_SETTINGS.get(
                    "UPLOAD_DELAY",
                    2
                )

                await asyncio.sleep(delay)

    except asyncio.CancelledError:

        print("\n🛑 Backup cancelled.")

        # Save current state before exiting
        save_state(uploaded_files)

        raise

    except KeyboardInterrupt:

        print("\n🛑 Backup interrupted by user.")

        # Save current state
        save_state(uploaded_files)

        return

    except Exception as e:

        print("\n❌ Unexpected backup error:")
        print(e)

        # Save current state
        save_state(uploaded_files)

    finally:

        # =====================================
        # FINAL SUMMARY
        # =====================================

        print("\n================================")
        print("📊 BACKUP SUMMARY")
        print("================================")

        print(
            f"Uploaded : {uploaded_count}"
        )

        print(
            f"Duplicate: {duplicate_count}"
        )

        print(
            f"Large    : {skipped_large}"
        )

        print(
            f"Failed   : {failed_count}"
        )

        print("================================")


# =========================================
# SCHEDULER
# =========================================

async def scheduler():

    backup_folder = config.STORAGE_DIR

    schedule_times = config.BACKUP_SETTINGS.get(
        "SCHEDULE_TIMES",
        ["00:00", "06:00", "12:00", "18:00"]
    )

    print("\n================================")
    print("⏰ BACKUP SCHEDULER STARTED")
    print("================================")

    print(f"📁 Folder: {backup_folder}")
    print("🕐 Schedule: " + ", ".join(schedule_times))
    print("▶️ Running initial backup now...")

    # =================================
    # BACKUP NOW
    # =================================

    await run_backup(backup_folder)

    print("\n================================")
    print("😴 INITIAL BACKUP FINISHED")
    print("================================")

    print("⏰ Waiting for next scheduled backup...")

    last_run = None

    while True:

        try:

            now = datetime.now()

            current_time = now.strftime("%H:%M")
            current_date = now.strftime("%Y-%m-%d")

            current_run = (
                f"{current_date}_{current_time}"
            )

            # =================================
            # CHECK SCHEDULE
            # =================================

            if (
                current_time in schedule_times
                and current_run != last_run
            ):

                last_run = current_run

                print("\n================================")
                print(
                    f"⏰ Scheduled backup: {current_time}"
                )
                print("================================")

                await run_backup(
                    backup_folder
                )

                print("\n😴 Waiting for next schedule...")

            # Check every 20 seconds
            await asyncio.sleep(20)

        except asyncio.CancelledError:

            print("\n🛑 Scheduler cancelled.")
            break

        except KeyboardInterrupt:

            print("\n🛑 Scheduler stopped by user.")
            break

        except Exception as e:

            print("\n❌ Scheduler error:")
            print(e)

            print("🔄 Scheduler continuing...")

            await asyncio.sleep(30)


# =========================================
# MAIN
# =========================================

async def main():

    scheduler_enabled = config.BACKUP_SETTINGS.get(
        "SCHEDULE_ENABLED",
        False
    )

    if scheduler_enabled:

        await scheduler()

    else:

        await run_backup(
            config.STORAGE_DIR
        )


# =========================================
# PROGRAM START
# =========================================

if __name__ == "__main__":

    try:

        asyncio.run(main())

    except KeyboardInterrupt:

        print(
            "\n🛑 Backup program stopped by user."
        )

    except Exception as e:

        print(
            "\n❌ Program error:"
        )

        print(e)


# =========================================
# LEGAL OWNER
# =========================================
#
# C-Firefly
#
# GitHub:
# https://c-firefly.github.io
#
# =========================================