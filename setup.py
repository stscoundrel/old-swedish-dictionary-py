import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="old-swedish-dictionary",
    version="1.0.0",
    author="stscoundrel",
    description="Old Swedish Dictionary for Python. From K.F. Söderwall's Medieval Swedish",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/stscoundrel/old-swedish-dictionary-py",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.9",
    package_data={"": ["**/*.json"]},
)
