from setuptools import setup, find_packages

setup(
    name="data-cleaning-reporting-automation",
    version="1.0.0",
    author="Abhishek Rajput",
    description="Automated Data Cleaning and Reporting System using Python",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "numpy",
        "matplotlib",
        "openpyxl"
    ],
    python_requires=">=3.9"
)