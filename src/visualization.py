import os
import matplotlib.pyplot as plt


def generate_charts(df, charts_folder, timestamp):
    """
    Generate visualization charts with timestamp
    """

    print("📊 Generating charts...")

    # Create folder if not exists
    os.makedirs(charts_folder, exist_ok=True)

    # =========================
    # Quantity Boxplot
    # =========================

    plt.figure()

    plt.boxplot(df["Quantity"])

    plt.title("Quantity Boxplot")

    quantity_chart = os.path.join(
        charts_folder,
        f"quantity_boxplot_{timestamp}.png"
    )

    plt.savefig(quantity_chart)

    plt.close()

    print("📦 Quantity boxplot saved")

    # =========================
    # UnitPrice Histogram
    # =========================

    plt.figure()

    plt.hist(
        df["UnitPrice"],
        bins=50
    )

    plt.title("UnitPrice Histogram")

    unitprice_chart = os.path.join(
        charts_folder,
        f"unitprice_histogram_{timestamp}.png"
    )

    plt.savefig(unitprice_chart)

    plt.close()

    print("📊 UnitPrice histogram saved")

    print("✅ Charts generated successfully")
