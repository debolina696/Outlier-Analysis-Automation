# =========================================
# Data Cleaning Module
# =========================================

import pandas as pd


def clean_data(df, config):

    """
    Clean dataset based on config rules
    """

    print("🧹 Starting data cleaning...")

    # Make safe copy
    df = df.copy()

    cleaning_config = config["cleaning"]

    # =========================
    # Remove duplicates
    # =========================

    if cleaning_config["drop_duplicates"]:

        before = df.shape[0]

        df = df.drop_duplicates()

        after = df.shape[0]

        print(
            f"🧾 Duplicates removed: {before - after}"
        )

    # =========================
    # Fill missing values
    # =========================

    fill_config = cleaning_config["fill_missing"]

    for column, value in fill_config.items():

        if column in df.columns:

            df.loc[:, column] = df[column].fillna(value)

            print(
                f"🧩 Missing values filled in {column}"
            )

    # =========================
    # Remove negative values
    # =========================

    negative_columns = cleaning_config[
        "remove_negative_values"
    ]

    for column in negative_columns:

        if column in df.columns:

            before = df.shape[0]

            df = df[df[column] >= 0]

            after = df.shape[0]

            print(
                f"🚫 Negative values removed from {column}: {before - after}"
            )

    print("✅ Data cleaning completed")

    return df
