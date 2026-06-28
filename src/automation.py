"""
Project : Data Cleaning & Reporting Automation
File    : automation.py
Author  : Abhishek Kumar
"""

import time
import traceback

from data_cleaning import DataCleaning
from report_generator import ReportGenerator

from utils import (
    application_header,
    print_subtitle,
    success,
    warning,
    error
)


class Automation:

    """
    Complete Automation Pipeline
    """

    def __init__(self):

        self.cleaner = DataCleaning()

        self.report = ReportGenerator()

        self.start_time = None

        self.end_time = None

        self.execution_time = None

    # ===========================================
    # START PIPELINE
    # ===========================================

    def start_pipeline(self):

        application_header(

            "DATA CLEANING & REPORTING AUTOMATION"

        )

        self.start_time = time.time()

        success(

            "Automation Started."

        )

    # ===========================================
    # RUN DATA CLEANING
    # ===========================================

    def run_data_cleaning(self):

        print_subtitle(

            "Executing Data Cleaning"

        )

        self.cleaner.execute()

        success(

            "Data Cleaning Completed."

        )

    # ===========================================
    # RUN REPORT GENERATION
    # ===========================================

    def run_report_generation(self):

        print_subtitle(

            "Executing Report Generator"

        )

        self.report.execute()

        success(

            "Report Generation Completed."

        )

    # ===========================================
    # STOP TIMER
    # ===========================================

    def stop_pipeline(self):

        self.end_time = time.time()

        self.execution_time = round(

            self.end_time - self.start_time,

            2

        )

        success(

            f"Execution Time : {self.execution_time} Seconds"

        )
# ===========================================
    # EXECUTE COMPLETE AUTOMATION
    # ===========================================

    def execute(self):

        try:

            self.start_pipeline()

            self.run_data_cleaning()

            self.run_report_generation()

            self.stop_pipeline()

            success(

                "Automation Pipeline Completed Successfully."

            )

        except Exception as exception:

            error(

                "Automation Failed."

            )

            print("\n")

            print(traceback.format_exc())

            raise exception

    # ===========================================
    # EXECUTION SUMMARY
    # ===========================================

    def execution_summary(self):

        print_subtitle(

            "Execution Summary"

        )

        print(

            f"Start Time : {self.start_time}"

        )

        print(

            f"End Time : {self.end_time}"

        )

        print(

            f"Execution Time : {self.execution_time} Seconds"

        )

        print(

            "Pipeline Status : SUCCESS"

        )

        success(

            "Summary Generated."

        )


# ===========================================
# MAIN PROGRAM
# ===========================================

if __name__ == "__main__":

    automation = Automation()

    automation.execute()

    automation.execution_summary()

    print("\n")

    print("=" * 70)

    print("AUTOMATION COMPLETED")

    print("=" * 70)

    print("Generated Files")

    print("------------------------------")

    print("✔ cleaned_data.csv")

    print("✔ duplicate_records.csv")

    print("✔ summary_report.csv")

    print("✔ final_report.txt")

    print("✔ cleaning_report.txt")

    print("✔ automation_log.txt")

    print("=" * 70)