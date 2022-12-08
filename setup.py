import glob
from setuptools import find_packages, setup

setup(
    name="assets_dbt_python",
    packages=find_packages(exclude=["assets_dbt_python_tests"]),
    # package data paths are relative to the package key
    package_data={"assets_dbt_python": ['../' + path for path in glob.glob("dbt_project/**", recursive=True)]},
    install_requires=[
        "dagster",
        "dagster-cloud",
        "boto3",
        "dagster-dbt",
        "pandas",
        "numpy",
        "scipy",
        "dbt-core",
        "dbt-duckdb",
        "dagster-duckdb",
        "dagster-duckdb-pandas",
        "packaging<22.0", # match dbt-core's requirement to workaround a resolution issue
    ],
    extras_require={"dev": ["dagit", "pytest"]},
)
