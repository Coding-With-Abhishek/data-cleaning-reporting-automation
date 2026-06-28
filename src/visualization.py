"""
Project : Data Cleaning & Reporting Automation
File    : visualization.py
Author  : Abhishek Kumar
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from config import (
    CLEANED_DATA
)

from utils import (
    application_header,
    print_subtitle,
    load_csv,
    success
)


class Visualization:

    """
    Visualization Module
    """

    def __init__(self):

        self.data = None

    # ===========================================
    # LOAD DATASET
    # ===========================================

    def load_dataset(self):

        application_header(

            "DATA VISUALIZATION"

        )

        print_subtitle(

            "Loading Cleaned Dataset"

        )

        self.data = load_csv(

            CLEANED_DATA

        )

        success(

            "Dataset Loaded Successfully."

        )

    # ===========================================
    # SALES DISTRIBUTION
    # ===========================================

    def sales_distribution(self):

        print_subtitle(

            "Sales Distribution"

        )

        plt.figure(

            figsize=(10,6)

        )

        plt.hist(

            self.data["Sales"],

            bins=10,

            edgecolor="black"

        )

        plt.title(

            "Sales Distribution"

        )

        plt.xlabel(

            "Sales"

        )

        plt.ylabel(

            "Frequency"

        )

        plt.grid(True)

        plt.savefig(

            "reports/sales_distribution.png",

            dpi=300

        )

        plt.close()

        success(

            "Sales Distribution Saved."

        )

    # ===========================================
    # SALES TREND
    # ===========================================

    def sales_trend(self):

        print_subtitle(

            "Sales Trend"

        )

        plt.figure(

            figsize=(10,6)

        )

        plt.plot(

            self.data["Purchase_Date"],

            self.data["Sales"],

            marker="o"

        )

        plt.title(

            "Sales Trend"

        )

        plt.xlabel(

            "Purchase Date"

        )

        plt.ylabel(

            "Sales"

        )

        plt.xticks(

            rotation=45

        )

        plt.grid(True)

        plt.tight_layout()

        plt.savefig(

            "reports/sales_trend.png",

            dpi=300

        )

        plt.close()

        success(

            "Sales Trend Saved."

        )
# ===========================================
    # MISSING VALUES CHART
    # ===========================================

    def missing_values_chart(self):

        print_subtitle(

            "Missing Values Chart"

        )

        missing = self.data.isnull().sum()

        plt.figure(

            figsize=(10,6)

        )

        plt.bar(

            missing.index,

            missing.values

        )

        plt.title(

            "Missing Values by Column"

        )

        plt.xlabel(

            "Columns"

        )

        plt.ylabel(

            "Missing Values"

        )

        plt.xticks(

            rotation=45

        )

        plt.tight_layout()

        plt.savefig(

            "reports/missing_values_chart.png",

            dpi=300

        )

        plt.close()

        success(

            "Missing Values Chart Saved."

        )

    # ===========================================
    # PRODUCT SALES ANALYSIS
    # ===========================================

    def product_sales_chart(self):

        print_subtitle(

            "Product Sales Analysis"

        )

        product_sales = self.data.groupby(

            "Product"

        )["Sales"].sum()

        plt.figure(

            figsize=(10,6)

        )

        plt.bar(

            product_sales.index,

            product_sales.values

        )

        plt.title(

            "Product-wise Sales"

        )

        plt.xlabel(

            "Product"

        )

        plt.ylabel(

            "Total Sales"

        )

        plt.xticks(

            rotation=45

        )

        plt.tight_layout()

        plt.savefig(

            "reports/product_sales_chart.png",

            dpi=300

        )

        plt.close()

        success(

            "Product Sales Chart Saved."

        )

    # ===========================================
    # CITY-WISE SALES
    # ===========================================

    def city_sales_chart(self):

        print_subtitle(

            "City-wise Sales"

        )

        city_sales = self.data.groupby(

            "City"

        )["Sales"].sum()

        plt.figure(

            figsize=(10,6)

        )

        plt.bar(

            city_sales.index,

            city_sales.values

        )

        plt.title(

            "City-wise Sales"

        )

        plt.xlabel(

            "City"

        )

        plt.ylabel(

            "Sales"

        )

        plt.xticks(

            rotation=45

        )

        plt.tight_layout()

        plt.savefig(

            "reports/city_sales_chart.png",

            dpi=300

        )

        plt.close()

        success(

            "City Sales Chart Saved."

        )
# ===========================================
    # CUSTOMER DISTRIBUTION
    # ===========================================

    def customer_distribution(self):

        print_subtitle(

            "Customer Distribution"

        )

        plt.figure(

            figsize=(10,6)

        )

        plt.hist(

            self.data["Age"],

            bins=10,

            edgecolor="black"

        )

        plt.title(

            "Customer Age Distribution"

        )

        plt.xlabel(

            "Age"

        )

        plt.ylabel(

            "Frequency"

        )

        plt.grid(True)

        plt.savefig(

            "reports/customer_distribution.png",

            dpi=300

        )

        plt.close()

        success(

            "Customer Distribution Chart Saved."

        )

    # ===========================================
    # EXECUTE VISUALIZATION
    # ===========================================

    def execute(self):

        self.load_dataset()

        self.sales_distribution()

        self.sales_trend()

        self.missing_values_chart()

        self.product_sales_chart()

        self.city_sales_chart()

        self.customer_distribution()

        success(

            "Visualization Completed."

        )


# ===========================================
# MAIN PROGRAM
# ===========================================

if __name__ == "__main__":

    visualizer = Visualization()

    visualizer.execute()

    print("\n")

    print("=" * 70)

    print("VISUALIZATION COMPLETED")

    print("=" * 70)

    print("Generated Charts")

    print("------------------------------")

    print("✔ sales_distribution.png")

    print("✔ sales_trend.png")

    print("✔ missing_values_chart.png")

    print("✔ product_sales_chart.png")

    print("✔ city_sales_chart.png")

    print("✔ customer_distribution.png")

    print("=" * 70)