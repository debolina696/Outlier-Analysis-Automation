import os


def generate_summary_report(
        original_rows,
        cleaned_rows,
        final_rows,
        timestamp,
        reports_folder
):

    print("📄 Generating summary report...")

    os.makedirs(
        reports_folder,
        exist_ok=True
    )

    report_file = os.path.join(
        reports_folder,
        f"summary_{timestamp}.txt"
    )

    outliers_removed = (
        cleaned_rows - final_rows
    )

    with open(
        report_file,
        "w"
    ) as f:

        f.write("📊 DATA PROCESSING SUMMARY\n")

        f.write(
            "============================\n\n"
        )

        f.write(
            f"Original Rows: {original_rows}\n"
        )

        f.write(
            f"After Cleaning: {cleaned_rows}\n"
        )

        f.write(
            f"After Outlier Removal: {final_rows}\n"
        )

        f.write(
            f"Outliers Removed: {outliers_removed}\n"
        )

        f.write(
            f"Timestamp: {timestamp}\n"
        )

    print(
        "✅ Summary report generated:",
        report_file
    )
