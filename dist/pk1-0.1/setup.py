from setuptools import setup, find_packages

setup(
    name="pk1",
    version="0.1",
    # packages=find_packages()
    packages=find_packages(
        where="src",
        include=["kk"],  # alternatively: `exclude=['additional*']`
    ),
    package_dir={"": "src"}
    # package_dir={"": "src"},
)
