from setuptools import setup, find_packages

# change the name here and rename cli module
name = 'zero-traffic-cli'
n = name.replace('-', '_')

setup(
    name=name,
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            f'{name}={n}:main',
        ],
    },
    install_requires=[],
)
