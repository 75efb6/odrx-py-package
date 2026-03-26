from setuptools import setup, find_packages

setup(
    name="odrx.py",
    version="1.0.0",
    description="Async Python client for the osu!droid relax (ODRX) API",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="75efb6",
    url="https://github.com/75efb6/odrx-py-package",
    packages=find_packages(exclude=("tests", "tests.*")),
    py_modules=["odrx_py"],
    install_requires=[
        "aiohttp>=3.8.0",
    ],
    python_requires=">=3.8",
    license="MIT",
    keywords=[
        "osu",
        "osu!droid",
        "api",
        "async",
        "wrapper",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    include_package_data=True,
)