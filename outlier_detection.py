# =========================================
# Outlier Detection Module
# =========================================

import pandas as pd


def detect_outliers_iqr(df, config):

    """
    Remove outliers using IQR method
    """

    print("📊 Starting outlier detection...")

    outlier_config = config["outliers"]

    columns = outlier_config["columns"]

    multiplier = outlier_config[
        "iqr_multiplier"
    ]

    for column in columns:

        if column in df.columns:

            print(f"🔍 Processing column: {column}")

            Q1 = df[column].quantile(0.25)

            Q3 = df[column].quantile(0.75)

            IQR = Q3 - Q1

            lower_bound = Q1 - multiplier * IQR

            upper_bound = Q3 + multiplier * IQR

            before = df.shape[0]

            df = df[
                (df[column] >= lower_bound)
                &
                (df[column] <= upper_bound)
            ]

            after = df.shape[0]

            print(
                f"🚫 Outliers removed from {column}: {before - after}"
            )

    print("✅ Outlier detection completed")

    return df
