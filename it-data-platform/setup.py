from setuptools import find_packages, setup

setup(
    name="it_data_platform",
    packages=find_packages(exclude=["it_data_platform_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud"
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
