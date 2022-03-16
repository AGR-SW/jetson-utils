
import setuptools
# with open("README.md", "r") as fh:
#     long_description = fh.read()
pkg = setuptools.find_packages()
print(pkg)
setuptools.setup(
    name="jetson_utils",  # Replace with your own username
    version="0.0.4",
    author="Jai-Chang.Park(Dreamwalker)",
    author_email="jaichang@angel-robotics.com",
    description="Jetson Utility",
    long_description="# Jetson Utils",
    long_description_content_type="text/markdown",
    # url="https://github.com/pypa/sampleproject",
    packages=pkg,
    classifiers=["Programming Language :: Python :: 3",
                 "License :: OSI Approved :: MIT License",
                 "Operating System :: OS Independent", ],
    python_requires='>=3.6',
    install_requires=["jetson-stats", ],
    license='Apache',
    py_modules=['jetson_utils']
)
