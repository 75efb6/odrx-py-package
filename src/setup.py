from setuptools import setup, find_packages


setup(
    name='odrx.py',
    version='1.0.0',
    install_requires=[
        'aiohttp',
    ],
    packages=find_packages(exclude=["tests*", "tests.*"]),
    py_modules=['odrx-py'],
    url="https://github.com/75efb6/odrx-py",
    author="75efb6",
    description="A Python package for the osu!droid relax API.",
)