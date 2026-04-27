# =========================================
# Data Loader Module
# =========================================

import pandas as pd
import os


def get_latest_file(folder_path):

    """
    Get latest CSV file from raw folder
    """

    print("📂 Checking raw folder...")

    # Get all CSV files
    files = []

    for f in os.listdir(folder_path):

        if f.endswith(".csv"):

            files.append(
                os.path.join(folder_path, f)
            )

    if len(files) == 0:

        raise ValueError(
            "❌ No CSV files found in raw folder"
        )

    # Get latest file
    latest_file = max(
        files,
        key=os.path.getctime
    )

    print("✅ Latest file detected:", latest_file)

    return latest_file


def load_data(file_path):

    """
    Load CSV file into DataFrame
    """

    print("📥 Loading file...")

    try:

        df = pd.read_csv(file_path)

        print("✅ File loaded successfully")

        print("📊 Data Shape:", df.shape)

        return df

    except Exception as e:

        print("❌ Error loading file")

        raise e
