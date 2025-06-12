from setuptools import setup, find_packages

setup(
    name="htmlihunter",
    version="1.5.1",
    author="Avik Das",
    author_email="developeravikdas@gmail.com",
    description="Advanced HTML Injection & XSS Scanner tool",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/developeravik/HTMLiHunter",
    packages=find_packages(),
    install_requires=[
        "requests",
        "beautifulsoup4",
        "lxml",
        "colorama",
        "selenium",
        "webdriver-manager"
    ],
    entry_points={
        "console_scripts": [
            "htmlihunter=htmlihunter.main:main",  
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
