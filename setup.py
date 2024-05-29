from setuptools import setup, find_packages

setup(
    name='create_venv',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'create_venv = create_venv:create_venv',  # This allows the function to be run as a command line script
        ],
    },
    install_requires=[
        # Add any dependencies here
    ],
    author='David Hankinson',
    author_email='davidmhankinson@outlook.com',
    description='A simple interactive virtual environment creator',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/david-hankinson/create_venv',
)