from setuptools import setup, find_packages

setup(
    name="pk5",
    version="0.1",
    # packages=find_packages(),
    packages=find_packages(
        where="src",
        include=["kk*"],  # alternatively: `exclude=['additional*']`
    ),
    # package_dir={"": "pk3"}
    package_dir={"": "src"},
)
