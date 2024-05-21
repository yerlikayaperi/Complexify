from setuptools import setup , find_packages

with open("LICENSE", "r", encoding="utf-8") as fh:
    license_text = fh.read()

setup(
    name = "complexify",
    version = "1.0.0",
    author = "Peri Yerlikaya, Shahina Chopra",
    author_email = "peri.yerlikaya@epfl.ch, shahina.chopra@epfl.ch",
    description = "streamlit page to navigate a coordination complex database",
    url = 'https://github.com/yerlikayaperi/Complexify',
    packages =find_packages(),
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_require= '>=3.6',
    license= "MIT",
    include_package_data=True,     # Include package data
    package_data={
        '': ['LICENSE'],  # Include LICENSE file
    },
)