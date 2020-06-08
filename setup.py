import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ping-overseer",
    version="0.0.4",
    author="Jeff Tadashi Moy",
    author_email="jeff@jefftadashi.com",
    description="Mass ping monitoring module!",
    install_requires=[            
          'python-nmap',
          'jefftadashi_utils',
    ],
    license="gpl-3.0",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JeffTadashi/ping-overseer",
    packages=setuptools.find_packages(),
    scripts=['ping-overseer/ping-overseer'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)