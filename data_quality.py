import os
import pandas as pd


def generate_data_quality_report(
        df,
        timestamp,
        reports_folder
):

    print("📊 Generating Data Quality Report...")

    os.makedirs(
        reports_folder,
        exist_ok=True
    )

    report_data = []

    for column in df.columns:

        missing = df[column].isnull().sum()

        unique = df[column].nunique()

        dtype = df[column].dtype

        if pd.api.types.is_numeric_dtype(df[column]):

            mean_val = df[column].mean()

            min_val = df[column].min()

            max_val = df[column].max()

        else:

            mean_val = None

            min_val = None

            max_val = None

        report_data.append({

            "Column": column,

            "Missing Values": missing,

            "Unique Values": unique,

            "Data Type": dtype,

            "Mean": mean_val,

            "Min": min_val,

            "Max": max_val

        })

    quality_df = pd.DataFrame(report_data)

    file_path = os.path.join(

        reports_folder,

        f"data_quality_{timestamp}.csv"

    )

    quality_df.to_csv(

        file_path,

        index=False

    )

    print(

        "✅ Data Quality Report saved:",

        file_path

    )
