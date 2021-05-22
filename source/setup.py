from setuptools import setup

setup(
    name="image_preprocessing",
    version="",
    packages=[
        "scripts",
        "networks",
        "validation",
        "validation.file",
        "validation.file.interfaces",
        "validation.interfaces",
        "data_access",
        "data_access.files",
        "data_access.files.tests",
        "data_access.files.interfaces",
        "data_access.files.implementations",
        "data_access.interfaces",
        "image_representation",
        "image_representation.test",
        "image_representation.interfaces",
        "image_representation.implementations",
    ],
    package_dir={"": "source"},
    url="",
    license="",
    author="Andreas Scharf",
    author_email="",
    description="",
    install_requires=["PyContracts"],
)