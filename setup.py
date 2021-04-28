from setuptools import setup, find_packages

setup(
    name="Tinder Date Automation",
    version="1.0.0",
    description="The bot which decides to like or dislike a tinder date, depends on you prefers.",
    author="Maxim Ammosov, Aleksandr Yalejnik, Aleksandr Kasian, Daniil Silenok",
    packages=find_packages(),
    install_requires=[
        'beautifulsoup4==4.9.3',
        'cached-property==1.5.2',
        'certifi==2020.12.5',
        'chardet==4.0.0',
        'cycler==0.10.0',
        'decorator==4.4.2',
        'idna==2.10',
        'imageio==2.9.0',
        'kiwisolver==1.3.1',
        'lxml==4.6.3',
        'matplotlib==3.4.1',
        'networkx==2.5.1',
        'numpy==1.20.2',
        'opencv-python==4.5.1.48',
        'path==15.1.2',
        'Pillow==8.2.0',
        'pyparsing==2.4.7',
        'python-dateutil==2.8.1',
        'PyWavelets==1.1.1',
        'PyYAML==5.4.1',
        'requests==2.25.1',
        'robobrowser==0.5.3',
        'scikit-image==0.18.1',
        'scipy==1.6.3',
        'six==1.15.0',
        'soupsieve==2.2.1',
        'tifffile==2021.4.8',
        'urllib3==1.26.4',
        'Werkzeug==1.0.1'
    ],
    entry_points={
        'console_scripts': [
            'validation = application.validation_entry',
        ]
    }
)