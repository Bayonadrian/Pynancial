from setuptools import setup, find_packages

with open("Pynancialyst/Readme.md", "r") as f:
    long_description = f.read()

setup(
    name= 'Pynancialyst',
    version= '0.1.1.1',
    description= 'This is a library for financial analysis.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    package_dir= {'': 'Pynancialyst'},
    packages= find_packages(where= 'Pynancialyst'),
    author='Bayonalyst',
    author_email='bayonadrian0313@gmail.com',
    url= 'https://github.com/CloseBayona/Pynancialyst.git',
    license= 'MIT',
    classifiers=['License :: OSI Approved :: MIT License',
                 'Programming Language :: Python :: 3.10', 
                 'Operating System :: OS Independent'],
    install_requires= ['numpy>=1.24.2', 'wincertstore>=0.2'],
    extras_require={
        "dev": ['nose>=1.3.7', 'twine>=4.0.2']
    },
    python_requires='>=3.9'
)