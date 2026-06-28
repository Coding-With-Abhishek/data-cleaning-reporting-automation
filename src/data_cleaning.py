"""
Project : Data Cleaning & Reporting Automation
File    : data_cleaning.py
Author  : Abhishek Kumar
"""

import pandas as pd
import numpy as np

from config import (
    RAW_DATA,
    CLEANED_DATA,
    DUPLICATE_DATA,
    EXPECTED_COLUMNS,
    FILL_MISSING_NUMERIC,
    FILL_MISSING_CATEGORICAL
)

from utils import (
    application_header,
    print_subtitle,
    load_csv,
    save_csv,
    validate_columns,
    dataset_information,
    missing_values,
    duplicate_records,
    success,
    warning
)


class DataCleaning:

    """
    Data Cleaning Class
    """

    def __init__(self):

        self.data = None

        self.duplicate_data = None

    # ===========================================
    # LOAD DATASET
    # ===========================================

    def load_dataset(self):

        application_header(

            "DATA CLEANING & REPORTING AUTOMATION"

        )

        print_subtitle(

            "Loading Raw Dataset"

        )

        self.data = load_csv(

            RAW_DATA

        )

        success(

            "Dataset Loaded Successfully."

        )

    # ===========================================
    # VALIDATE DATASET
    # ===========================================

    def validate_dataset(self):

        print_subtitle(

            "Dataset Validation"

        )

        validate_columns(

            self.data,

            EXPECTED_COLUMNS

        )

        dataset_information(

            self.data

        )

    # ===========================================
    # HANDLE MISSING VALUES
    # ===========================================

    def handle_missing_values(self):

        print_subtitle(

            "Handling Missing Values"

        )

        missing_values(

            self.data

        )

        numeric_columns = self.data.select_dtypes(

            include=np.number

        ).columns

        categorical_columns = self.data.select_dtypes(

            exclude=np.number

        ).columns

        for column in numeric_columns:

            if FILL_MISSING_NUMERIC == "mean":

                self.data[column].fillna(

                    self.data[column].mean(),

                    inplace=True

                )

        for column in categorical_columns:

            self.data[column].fillna(

                FILL_MISSING_CATEGORICAL,

                inplace=True

            )

        success(

            "Missing Values Filled."

        )

    # ===========================================
    # REMOVE EMPTY ROWS
    # ===========================================

    def remove_empty_rows(self):

        print_subtitle(

            "Removing Empty Rows"

        )

        before = len(

            self.data

        )

        self.data.dropna(

            how="all",

            inplace=True

        )

        after = len(

            self.data

        )

        print(

            f"Rows Removed : {before-after}"

        )

        success(

            "Empty Rows Removed."

        )
# ===========================================
    # REMOVE DUPLICATE RECORDS
    # ===========================================

    def remove_duplicates(self):

        print_subtitle(

            "Removing Duplicate Records"

        )

        duplicate_records(

            self.data

        )

        self.duplicate_data = self.data[

            self.data.duplicated()

        ]

        save_csv(

            self.duplicate_data,

            DUPLICATE_DATA

        )

        before = len(

            self.data

        )

        self.data.drop_duplicates(

            inplace=True

        )

        after = len(

            self.data

        )

        print(

            f"Duplicates Removed : {before-after}"

        )

        success(

            "Duplicate Records Removed."

        )

    # ===========================================
    # STANDARDIZE COLUMN NAMES
    # ===========================================

    def standardize_columns(self):

        print_subtitle(

            "Standardizing Column Names"

        )

        self.data.columns = [

            column.strip()

            .replace(

                " ",

                "_"

            )

            .title()

            for column in self.data.columns

        ]

        success(

            "Column Names Standardized."

        )

    # ===========================================
    # REMOVE EXTRA SPACES
    # ===========================================

    def remove_extra_spaces(self):

        print_subtitle(

            "Removing Extra Spaces"

        )

        object_columns = self.data.select_dtypes(

            include="object"

        ).columns

        for column in object_columns:

            self.data[column] = self.data[column].astype(

                str

            ).str.strip()

        success(

            "Extra Spaces Removed."

        )

    # ===========================================
    # REMOVE NEGATIVE VALUES
    # ===========================================

    def remove_negative_values(self):

        print_subtitle(

            "Checking Negative Values"

        )

        numeric_columns = self.data.select_dtypes(

            include=np.number

        ).columns

        for column in numeric_columns:

            self.data = self.data[

                self.data[column] >= 0

            ]

        success(

            "Negative Values Removed."

        )

    # ===========================================
    # CONVERT DATE FORMAT
    # ===========================================

    def convert_date(self):

        print_subtitle(

            "Converting Date Format"

        )

        if "Purchase_Date" in self.data.columns:

            self.data["Purchase_Date"] = pd.to_datetime(

                self.data["Purchase_Date"],

                errors="coerce"

            )

        success(

            "Date Format Standardized."

        )

    # ===========================================
    # CLEANING PIPELINE
    # ===========================================

    def clean_dataset(self):

        self.load_dataset()

        self.validate_dataset()

        self.handle_missing_values()

        self.remove_empty_rows()

        self.remove_duplicates()

        self.standardize_columns()

        self.remove_extra_spaces()

        self.remove_negative_values()

        self.convert_date()

        return self.data
# ===========================================
    # SAVE CLEANED DATASET
    # ===========================================

    def save_cleaned_dataset(self):

        print_subtitle(

            "Saving Cleaned Dataset"

        )

        save_csv(

            self.data,

            CLEANED_DATA

        )

        success(

            "Cleaned Dataset Saved Successfully."

        )

    # ===========================================
    # GENERATE CLEANING REPORT
    # ===========================================

    def generate_report(self):

        print_subtitle(

            "Generating Cleaning Report"

        )

        report = f"""
============================================================
DATA CLEANING REPORT
============================================================

Total Records : {len(self.data)}

Total Columns : {len(self.data.columns)}

Duplicate Records Removed : {len(self.duplicate_data)}

Missing Values Handled : Completed

Empty Rows Removed : Completed

Negative Values Removed : Completed

Column Standardization : Completed

Date Conversion : Completed

Cleaning Status : SUCCESS

============================================================
"""

        with open(

            "reports/cleaning_report.txt",

            "w",

            encoding="utf-8"

        ) as file:

            file.write(

                report

            )

        success(

            "Cleaning Report Generated."

        )

    # ===========================================
    # EXECUTE COMPLETE PIPELINE
    # ===========================================

    def execute(self):

        self.clean_dataset()

        self.save_cleaned_dataset()

        self.generate_report()

        success(

            "Data Cleaning Pipeline Completed."

        )


# ===========================================
# MAIN PROGRAM
# ===========================================

if __name__ == "__main__":

    cleaner = DataCleaning()

    cleaner.execute()

    print("\n")

    print("=" * 70)

    print("DATA CLEANING COMPLETED")

    print("=" * 70)

    print("Generated Files")

    print("------------------------------")

    print("✔ cleaned_data.csv")

    print("✔ duplicate_records.csv")

    print("✔ cleaning_report.txt")

    print("=" * 70)