"""
Project : Data Cleaning & Reporting Automation
File    : config.py
Author  : Abhishek Kumar
"""

import os

# =====================================================
# PROJECT DIRECTORIES
# =====================================================

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

DATA_DIR = os.path.join(
    BASE_DIR,
    "data"
)

REPORT_DIR = os.path.join(
    BASE_DIR,
    "reports"
)

# =====================================================
# INPUT FILES
# =====================================================

RAW_DATA = os.path.join(
    DATA_DIR,
    "raw_data.csv"
)

CLEANED_DATA = os.path.join(
    DATA_DIR,
    "cleaned_data.csv"
)

DUPLICATE_DATA = os.path.join(
    DATA_DIR,
    "duplicate_records.csv"
)

# =====================================================
# REPORT FILES
# =====================================================

CLEANING_REPORT = os.path.join(
    REPORT_DIR,
    "cleaning_report.txt"
)

QUALITY_REPORT = os.path.join(
    REPORT_DIR,
    "quality_report.txt"
)

SUMMARY_REPORT = os.path.join(
    REPORT_DIR,
    "summary_report.csv"
)

FINAL_REPORT = os.path.join(
    REPORT_DIR,
    "final_report.txt"
)

AUTOMATION_LOG = os.path.join(
    REPORT_DIR,
    "automation_log.txt"
)

# =====================================================
# DATA CLEANING SETTINGS
# =====================================================

REMOVE_DUPLICATES = True

FILL_MISSING_NUMERIC = "mean"

FILL_MISSING_CATEGORICAL = "Unknown"

REMOVE_NEGATIVE_VALUES = True

REMOVE_EMPTY_ROWS = True

STANDARDIZE_COLUMNS = True

REMOVE_EXTRA_SPACES = True

CONVERT_DATE_COLUMNS = True

DROP_HIGH_NULL_COLUMNS = False

NULL_THRESHOLD = 0.50

# =====================================================
# EXPECTED DATASET COLUMNS
# =====================================================

EXPECTED_COLUMNS = [

    "Customer_ID",

    "Customer_Name",

    "Age",

    "City",

    "Product",

    "Quantity",

    "Sales",

    "Email",

    "Purchase_Date"

]

# =====================================================
# VISUALIZATION SETTINGS
# =====================================================

FIGURE_WIDTH = 10

FIGURE_HEIGHT = 6

IMAGE_DPI = 300

# =====================================================
# RANDOM STATE
# =====================================================

RANDOM_STATE = 42

# =====================================================
# LOGGING
# =====================================================

LOG_LEVEL = "INFO"

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"

# =====================================================
# APPLICATION INFO
# =====================================================

PROJECT_NAME = "Data Cleaning & Reporting Automation"

VERSION = "1.0.0"

AUTHOR = "Abhishek Kumar"