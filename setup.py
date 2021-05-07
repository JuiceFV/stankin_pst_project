from setuptools import setup, find_packages
import pathlib
import pkg_resources

with pathlib.Path('requirements.txt').open() as requirements_txt:
    install_requires = [
        str(requirement)
        for requirement
        in pkg_resources.parse_requirements(requirements_txt)
    ]

setup(
    name="Tinder Date Automation",
    version="1.0.0",
    description="The bot which decides to like or dislike a tinder date, depends on you prefers.",
    author="Maxim Ammosov, Aleksandr Yalejnik, Aleksandr Kasian, Daniil Silenok",
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    entry_points={
        'console_scripts':[
            'bot_start = application.entry',
            'validation = application.validation_entry',
        ]
    }
)