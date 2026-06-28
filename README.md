Data Cleaning & Reporting Automation

An end-to-end data automation project developed using Python to clean raw datasets, improve data quality, validate records, detect inconsistencies, and generate automated reports. This project demonstrates practical data preprocessing techniques commonly used in business intelligence, analytics, and machine learning workflows.

---

Features

- Import raw CSV datasets
- Handle missing values automatically
- Remove duplicate records
- Detect inconsistent data
- Standardize column names
- Validate data types
- Generate data quality reports
- Export cleaned datasets
- Create summary reports
- Visualize data quality statistics
- Automated logging
- Modular project architecture

---

Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- OpenPyXL
- CSV
- Logging

---

Project Structure

data-cleaning-reporting-automation
│
├── data
│   ├── raw_data.csv
│   ├── cleaned_data.csv
│   └── duplicate_records.csv
│
├── src
│   ├── config.py
│   ├── utils.py
│   ├── data_cleaning.py
│   ├── report_generator.py
│   ├── automation.py
│   ├── quality_checker.py
│   └── visualization.py
│
├── reports
│   ├── cleaning_report.txt
│   ├── quality_report.txt
│   ├── automation_log.txt
│   ├── summary_report.csv
│   └── final_report.txt
│
├── models
│   └── README.md
│
├── requirements.txt
├── README.md
├── .gitignore
├── LICENSE
└── setup.py

---

Dataset

The project processes raw business datasets containing customer and sales information.

Example columns:

- Customer_ID
- Customer_Name
- Age
- City
- Product
- Quantity
- Sales
- Email
- Purchase_Date

---

Workflow

1. Import raw dataset
2. Validate data
3. Handle missing values
4. Remove duplicate records
5. Detect inconsistent entries
6. Standardize dataset
7. Calculate data quality statistics
8. Generate reports
9. Export cleaned dataset
10. Visualize results

---

Installation

git clone https://github.com/your-username/data-cleaning-reporting-automation.git

cd data-cleaning-reporting-automation

pip install -r requirements.txt

---

Run Project

python src/data_cleaning.py

python src/quality_checker.py

python src/report_generator.py

python src/automation.py

python src/visualization.py

---

Generated Outputs

After execution, the project automatically generates:

Cleaned Data

- cleaned_data.csv
- duplicate_records.csv

Reports

- cleaning_report.txt
- quality_report.txt
- automation_log.txt
- summary_report.csv
- final_report.txt

Generated output files are created automatically during project execution.

---

Future Improvements

- Excel Automation
- Power BI Integration
- Interactive Dashboard
- Email Report Scheduling
- Database Connectivity
- Streamlit Web Application
- Cloud Storage Integration

---

Author

Abhishek Kumar

B.Tech Computer Science & Engineering (Artificial Intelligence)

---

License

This project is licensed under the MIT License.