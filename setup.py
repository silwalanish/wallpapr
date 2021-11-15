from setuptools import setup, find_packages

setup(
    name="wallpapr",
    version="0.1.0",
    description="Downloads a random picture and updates the wallpaper.",
    author="Anish Silwal Khatri",
    author_email="silwalanish@gmail.com",
    packages=find_packages(include=["wallpapr", "wallpapr.*"]),
    install_requires=["requests==2.26.0"],
    entry_points={"console_scripts": ["wallpapr=wallpapr.wallpapr:main"]},
)
