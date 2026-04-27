import os
import yaml
import shutil

from src.data_loader import get_latest_file, load_data
from src.data_cleaning import clean_data
from src.outlier_detection import detect_outliers_iqr
from src.visualization import generate_charts
from src.report_generator import generate_summary_report
from src.data_quality import generate_data_quality_report

from src.utils.helpers import (
    create_timestamp,
    clean_old_files
)

from src.utils.logger import setup_logger


def run_pipeline():

    print("🚀 Starting Pipeline...")

    # =========================
    # Load Config
    # =========================

    with open("config/config.yaml", "r") as file:
        config = yaml.safe_load(file)

    paths = config["paths"]

    raw_folder = paths["raw_data"]
    processed_folder = paths["processed_data"]
    archive_folder = paths["archive_data"]
    charts_folder = paths["charts"]
    reports_folder = paths["reports"]
    logs_folder = paths["logs"]

    print("Loaded paths:", paths)

    # =========================
    # Clean Old Outputs
    # =========================

    clean_old_files(processed_folder)
    clean_old_files(charts_folder)
    clean_old_files(reports_folder)
    clean_old_files(logs_folder)

    # =========================
    # Setup Logger
    # =========================

    logger = setup_logger(logs_folder)

    # =========================
    # Create Timestamp
    # =========================

    timestamp = create_timestamp()

    # =========================
    # Get Latest File
    # =========================

    print("📂 Checking raw folder...")

    latest_file = get_latest_file(raw_folder)

    print("✅ Latest file detected:", latest_file)

    # =========================
    # Load Data
    # =========================

    df = load_data(latest_file)

    original_rows = df.shape[0]

    print("📊 Data Shape:", df.shape)

    # =========================
    # Clean Data
    # =========================

    cleaned_df = clean_data(
        df,
        config
    )

    cleaned_rows = cleaned_df.shape[0]

    print("After Cleaning:",
          cleaned_df.shape)

    # =========================
    # Outlier Removal
    # =========================

    final_df = detect_outliers_iqr(
        cleaned_df,
        config
    )

    final_rows = final_df.shape[0]

    print("After Outlier Removal:",
          final_df.shape)

    # =========================
    # Generate Charts
    # =========================

    generate_charts(
        final_df,
        charts_folder,
        timestamp
    )

    # =========================
    # Save Processed File
    # =========================

    os.makedirs(
        processed_folder,
        exist_ok=True
    )

    processed_file = os.path.join(
        processed_folder,
        f"cleaned_data_{timestamp}.csv"
    )

    final_df.to_csv(
        processed_file,
        index=False
    )

    print(
        "💾 Cleaned file saved:",
        processed_file
    )

    # =========================
    # Generate Summary Report
    # =========================

    generate_summary_report(
        original_rows,
        cleaned_rows,
        final_rows,
        timestamp,
        reports_folder
    )

    # =========================
    # Generate Data Quality Report
    # =========================

    generate_data_quality_report(
        final_df,
        timestamp,
        reports_folder
    )

    # =========================
    # Move Raw File to Archive
    # =========================

    os.makedirs(
        archive_folder,
        exist_ok=True
    )

    archive_file = os.path.join(
        archive_folder,
        os.path.basename(
            latest_file
        )
    )

    shutil.move(
        latest_file,
        archive_file
    )

    print(
        "📦 File moved to archive:",
        archive_file
    )

    print(
        "✅ Pipeline Completed Successfully"
    )
