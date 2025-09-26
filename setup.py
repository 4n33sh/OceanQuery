from setuptools import setup, find_packages

setup(
    name="argo_langchain_pipeline",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "langchain>=1.0",
        "xarray",
        "numpy",
        "pandas",
        "netCDF4",
        "matplotlib",
        "requests"
    ],
    include_package_data=True,
    package_data={
        "": ["pyowc/*", "utils/*", "argofloats/*", "processing/*", "owc_config.json"]
    },
    entry_points={
        "console_scripts": [
            "argo-run=main:main"
        ]
    },
)
