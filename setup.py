from setuptools import setup, find_packages


# ## pk5
# setup(
#     name="pk5",
#     version="0.1",
#     # packages=find_packages(),
#     packages=find_packages(
#         # where="src",
#         # include=["kk*"],  # alternatively: `exclude=['additional*']`
#     ),
#     package_dir={"": "src"},
# )


# ## pkgg
# setup(
#     name="pkgg",
#     version="0.1",
#     # packages=find_packages(),
#     packages=find_packages(
#         # where="src",
#         # include=["kk*"],  # alternatively: `exclude=['additional*']`
#     ),
#     # package_dir={"": "pk3"}
#     # package_dir={"": "src"},
# )


# pk7
setup(
    name="pk7",
    version="0.4",
    # packages=find_packages(),
    packages=find_packages(
        where="src",
        # include=["*"],  # alternatively: `exclude=['additional*']`
    ),
    package_dir={"": "src"},
)
