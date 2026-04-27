# =========================================
# Helper Functions Module
# =========================================

import os
import shutil
from datetime import datetime


def create_timestamp():

    """
    Create timestamp for file naming
    """

    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    print("🕒 Timestamp created:", timestamp)

    return timestamp


def move_file(source_path, destination_folder):

    """
    Move raw file to archive folder
    """

    try:

        # Create destination folder if not exists
        if not os.path.exists(destination_folder):

            os.makedirs(destination_folder)

        file_name = os.path.basename(source_path)

        destination_path = os.path.join(
            destination_folder,
            file_name
        )

        shutil.move(
            source_path,
            destination_path
        )

        print("📦 File moved to archive:", destination_path)

    except Exception as e:

        print("❌ Error moving file")

        raise e


def create_folder(folder_path):

    """
    Create folder if not exists
    """

    if not os.path.exists(folder_path):

        os.makedirs(folder_path)

        print("📁 Folder created:", folder_path)
        import os


def clean_old_files(folder):

    """
    Delete all files inside a folder
    """

    if os.path.exists(folder):

        files = os.listdir(folder)

        for file in files:

            file_path = os.path.join(
                folder,
                file
            )

            if os.path.isfile(file_path):

                os.remove(file_path)

        print(
            f"🧹 Old files removed from {folder}"
        )

