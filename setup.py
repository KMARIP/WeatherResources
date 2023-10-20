from setuptools import setup

setup(
    name="WeatherResources",
    version="0.1.1",
    description="A simple weather app",
    author="KMAR",
    author_email="kmaripradio@gmail.com",
    packages=["weather_resources"],
    install_requires=[
        "requests",
        "geopy",
    ],
    entry_points={
        "console_scripts": [
            "weather_resources=weather_resources:main",
        ],
    },
)

