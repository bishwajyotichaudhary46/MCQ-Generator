from setuptools import find_packages, setup

setup(
    name='mcqgenerator',
    version='0.0.1',
    author='Bishwajyoti Chaudhary',
    author_email="bishwajyotichaudhary46@gmail.com",
    
    install_requires = ["langchain","streamlit", "python-dotenv","PyPDF2"],
    packages= find_packages(),
)