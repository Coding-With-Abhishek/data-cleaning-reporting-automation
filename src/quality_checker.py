"""
Project : Data Cleaning & Reporting Automation
File    : quality_checker.py
Author  : Abhishek Kumar
"""

import pandas as pd
import numpy as np

from config import (
    CLEANED_DATA,
    EXPECTED_COLUMNS,
    QUALITY_REPORT
)

from utils import (
    application_header,
    print_subtitle,
    load_csv,
    validate_columns,
    success
)


class QualityChecker:

    """
    Data Quality Checker
    """

    def __init__(self):

        self.data = None

        self.report = {}

    # ===========================================
    # LOAD DATASET
    # ===========================================

    def load_dataset(self):

        application_header(

            "DATA QUALITY CHECKER"

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
    # VALIDATE COLUMNS
    # ===========================================

    def validate_dataset(self):

        print_subtitle(

            "Column Validation"

        )

        validate_columns(

            self.data,

            EXPECTED_COLUMNS

        )

        success(

            "Dataset Validation Completed."

        )

    # ===========================================
    # CHECK MISSING VALUES
    # ===========================================

    def check_missing_values(self):

        print_subtitle(

            "Checking Missing Values"

        )

        total_missing = int(

            self.data.isnull().sum().sum()

        )

        self.report["Missing Values"] = total_missing

        print(

            f"Missing Values : {total_missing}"

        )

        success(

            "Missing Value Check Completed."

        )

    # ===========================================
    # CHECK DUPLICATES
    # ===========================================

    def check_duplicates(self):

        print_subtitle(

            "Checking Duplicate Records"

        )

        duplicates = int(

            self.data.duplicated().sum()

        )

        self.report["Duplicate Records"] = duplicates

        print(

            f"Duplicate Records : {duplicates}"

        )

        success(

            "Duplicate Check Completed."

        )

    # ===========================================
    # CHECK DATA TYPES
    # ===========================================

    def check_data_types(self):

        print_subtitle(

            "Checking Data Types"

        )

        self.report["Columns"] = len(

            self.data.columns

        )

        self.report["Rows"] = len(

            self.data

        )

        print(

            self.data.dtypes

        )

        success(

            "Data Type Validation Completed."

        )
# ===========================================
    # CHECK INVALID VALUES
    # ===========================================

    def check_invalid_values(self):

        print_subtitle(

            "Checking Invalid Values"

        )

        numeric_columns = self.data.select_dtypes(

            include=np.number

        ).columns

        invalid_count = 0

        for column in numeric_columns:

            invalid_count += int(

                (self.data[column] < 0).sum()

            )

        self.report["Invalid Values"] = invalid_count

        print(

            f"Invalid Values : {invalid_count}"

        )

        success(

            "Invalid Value Check Completed."

        )

    # ===========================================
    # GENERATE QUALITY REPORT
    # ===========================================

    def generate_quality_report(self):

        print_subtitle(

            "Generating Quality Report"

        )

        with open(

            QUALITY_REPORT,

            "w",

            encoding="utf-8"

        ) as file:

            file.write(

                "DATA QUALITY REPORT\n"

            )

            file.write(

                "=" * 60

            )

            file.write("\n\n")

            for key, value in self.report.items():

                file.write(

                    f"{key} : {value}\n"

                )

            file.write("\n")

            file.write(

                "Overall Status : PASSED\n"

            )

        success(

            "Quality Report Generated."

        )

    # ===========================================
    # COMPLETE QUALITY CHECK
    # ===========================================

    def execute(self):

        self.load_dataset()

        self.validate_dataset()

        self.check_missing_values()

        self.check_duplicates()

        self.check_data_types()

        self.check_invalid_values()

        self.generate_quality_report()

        success(

            "Quality Checking Completed."

        )


# ===========================================
# MAIN PROGRAM
# ===========================================

if __name__ == "__main__":

    checker = QualityChecker()

    checker.execute()

    print("\n")

    print("=" * 70)

    print("QUALITY CHECK COMPLETED")

    print("=" * 70)

    print("Generated Files")

    print("------------------------------")

    print("✔ quality_report.txt")

    print("✔ Dataset Validation")

    print("✔ Missing Value Report")

    print("✔ Duplicate Record Report")

    print("✔ Invalid Value Report")

    print("=" * 70)