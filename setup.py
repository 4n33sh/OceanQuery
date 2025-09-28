from setuptools import setup, find_packages

setup(
    name="floatchat_pipeline",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "langchain>=1.0",
        "xarray",
        "numpy",
        "pandas",
        "netCDF4",
        "matplotlib",
        "requests",
        "faiss-cpu",
        "chromadb",
        "streamlit",
        "plotly",
        "leaflet",
        "sqlalchemy",
        "spacy"
    ],
    include_package_data=True,
    package_data={
        "": ["pyowc/*", "utils/*", "argofloats/*", "processing/*", "owc_config.json"]
    },
    entry_points={
        "console_scripts": [
            "floatchat-run=main:main"
        ]
    },
)
