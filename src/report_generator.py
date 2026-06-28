 """
Project : Data Cleaning & Reporting Automation
File    : report_generator.py
Author  : Abhishek Kumar
"""

import pandas as pd
import numpy as np

from config import (
    CLEANED_DATA,
    SUMMARY_REPORT,
    FINAL_REPORT
)

from utils import (
    application_header,
    print_subtitle,
    load_csv,
    save_csv,
    success
)


class ReportGenerator:

    """
    Report Generator Class
    """

    def __init__(self):

        self.data = None

        self.summary = {}

    # ===========================================
    # LOAD CLEANED DATASET
    # ===========================================

    def load_dataset(self):

        application_header(

            "REPORT GENERATION"

        )

        print_subtitle(

            "Loading Cleaned Dataset"

        )

        self.data = load_csv(

            CLEANED_DATA

        )

        success(

            "Cleaned Dataset Loaded."

        )

    # ===========================================
    # BASIC STATISTICS
    # ===========================================

    def basic_statistics(self):

        print_subtitle(

            "Calculating Statistics"

        )

        self.summary["Total Records"] = len(

            self.data

        )

        self.summary["Total Columns"] = len(

            self.data.columns

        )

        self.summary["Missing Values"] = int(

            self.data.isnull().sum().sum()

        )

        self.summary["Duplicate Records"] = int(

            self.data.duplicated().sum()

        )

        numeric = self.data.select_dtypes(

            include=np.number

        )

        self.summary["Average Sales"] = round(

            numeric["Sales"].mean(),

            2

        )

        self.summary["Maximum Sales"] = round(

            numeric["Sales"].max(),

            2

        )

        self.summary["Minimum Sales"] = round(

            numeric["Sales"].min(),

            2

        )

        success(

            "Statistics Generated."

        )

    # ===========================================
    # CREATE SUMMARY TABLE
    # ===========================================

    def create_summary(self):

        print_subtitle(

            "Creating Summary"

        )

        summary_dataframe = pd.DataFrame(

            self.summary.items(),

            columns=[

                "Metric",

                "Value"

            ]

        )

        save_csv(

            summary_dataframe,

            SUMMARY_REPORT

        )

        success(

            "Summary Report Created."

        )
# ===========================================
    # GENERATE FINAL REPORT
    # ===========================================

    def generate_final_report(self):

        print_subtitle(

            "Generating Final Report"

        )

        report = f"""
============================================================
DATA CLEANING & REPORTING AUTOMATION
============================================================

PROJECT SUMMARY

Total Records            : {self.summary['Total Records']}
Total Columns            : {self.summary['Total Columns']}
Missing Values           : {self.summary['Missing Values']}
Duplicate Records        : {self.summary['Duplicate Records']}

Sales Statistics

Average Sales            : {self.summary['Average Sales']}
Maximum Sales            : {self.summary['Maximum Sales']}
Minimum Sales            : {self.summary['Minimum Sales']}

Cleaning Status          : SUCCESS
Report Generation        : SUCCESS

============================================================
"""

        with open(

            FINAL_REPORT,

            "w",

            encoding="utf-8"

        ) as file:

            file.write(

                report

            )

        success(

            "Final Report Generated."

        )

    # ===========================================
    # EXECUTE REPORT PIPELINE
    # ===========================================

    def execute(self):

        self.load_dataset()

        self.basic_statistics()

        self.create_summary()

        self.generate_final_report()

        success(

            "Report Generation Completed."

        )


# ===========================================
# MAIN PROGRAM
# ===========================================

if __name__ == "__main__":

    generator = ReportGenerator()

    generator.execute()

    print("\n")

    print("=" * 70)

    print("REPORT GENERATION COMPLETED")

    print("=" * 70)

    print("Generated Files")

    print("------------------------------")

    print("✔ summary_report.csv")

    print("✔ final_report.txt")

    print("=" * 70)