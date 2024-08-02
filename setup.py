from setuptools import find_packages , setup

setup(
    name = "Data Scientist AI",
    version =  '0.0.1',
    author= 'TienLe',
    author_email='tle38413@gmail.com',
    install_requires = ['streamlit' , 'pyautogen[gemini]'],
    packages=find_packages()
)