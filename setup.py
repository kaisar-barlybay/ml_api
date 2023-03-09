import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
  long_description = fh.read()

setuptools.setup(
    name='aes_library',
    version='0.00.01',
    author='Kaisar Barlybay',
    author_email='kaisar.barlybay.sse@gmail.com',
    description='Testing installation of Package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/kaisar-barlybay/ml_api',
    project_urls={
        "Bug Tracker": "https://github.com/kaisar-barlybay/ml_api/issues"
    },
    license='MIT',
    packages=[
        'ml_api',
    ],
    install_requires=[
    ],
)
