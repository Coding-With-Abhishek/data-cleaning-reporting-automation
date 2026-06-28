"""
Project : Data Cleaning & Reporting Automation
File    : utils.py
Author  : Abhishek Kumar
"""

import os
import logging
import pandas as pd

from config import (
    LOG_LEVEL,
    LOG_FORMAT,
    AUTOMATION_LOG
)


# =====================================================
# LOGGING
# =====================================================

logging.basicConfig(

    filename=AUTOMATION_LOG,

    level=getattr(logging, LOG_LEVEL),

    format=LOG_FORMAT

)


# =====================================================
# PRINT FUNCTIONS
# =====================================================

def print_title(title):

    print("\n")

    print("=" * 70)

    print(title)

    print("=" * 70)


def print_subtitle(subtitle):

    print("\n")

    print("-" * 60)

    print(subtitle)

    print("-" * 60)


# =====================================================
# STATUS MESSAGES
# =====================================================

def success(message):

    print(f"[SUCCESS] {message}")

    logging.info(message)


def warning(message):

    print(f"[WARNING] {message}")

    logging.warning(message)


def error(message):

    print(f"[ERROR] {message}")

    logging.error(message)


# =====================================================
# CSV FUNCTIONS
# =====================================================

def load_csv(file_path):

    if not os.path.exists(file_path):

        raise FileNotFoundError(

            f"{file_path} not found."

        )

    return pd.read_csv(file_path)


def save_csv(dataframe, file_path):

    dataframe.to_csv(

        file_path,

        index=False

    )

    success(

        f"Saved : {file_path}"

    )


# =====================================================
# DATA VALIDATION
# =====================================================

def validate_columns(

    dataframe,

    expected_columns

):

    missing_columns = [

        column

        for column in expected_columns

        if column not in dataframe.columns

    ]

    if missing_columns:

        raise ValueError(

            f"Missing Columns : {missing_columns}"

        )

    success(

        "Column validation completed."

    )


# =====================================================
# DATA INFORMATION
# =====================================================

def dataset_information(dataframe):

    print_subtitle(

        "Dataset Information"

    )

    print(

        f"Rows    : {dataframe.shape[0]}"

    )

    print(

        f"Columns : {dataframe.shape[1]}"

    )

    print(

        "\nColumn Names\n"

    )

    for column in dataframe.columns:

        print(column)


# =====================================================
# MISSING VALUES
# =====================================================

def missing_values(dataframe):

    print_subtitle(

        "Missing Values"

    )

    print(

        dataframe.isnull().sum()

    )


# =====================================================
# DUPLICATE RECORDS
# =====================================================

def duplicate_records(dataframe):

    duplicates = dataframe.duplicated().sum()

    print(

        f"Duplicate Records : {duplicates}"

    )

    return duplicates


# =====================================================
# SAVE TEXT REPORT
# =====================================================

def save_report(

    report_path,

    content

):

    with open(

        report_path,

        "w",

        encoding="utf-8"

    ) as file:

        file.write(content)

    success(

        f"Report Saved : {report_path}"

    )


# =====================================================
# APPLICATION HEADER
# =====================================================

def application_header(name):

    print("\n")

    print("=" * 70)

    print(name)

    print("=" * 70)