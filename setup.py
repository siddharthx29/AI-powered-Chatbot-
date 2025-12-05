from setuptools import setup, find_packages

setup(
    name="pc_ai_lib",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests"
    ],
    author="Siddharth MV",
    description="Python library for PC Build & Troubleshooting AI",
    url="https://github.com/yourusername/pc_ai_lib",
    python_requires='>=3.9',
)
