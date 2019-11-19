import setuptools

setuptools.setup(
    name='py_etherscan_api',
    version='0.8.1',
    packages=['etherscan'],
    url='https://github.com/daboooooo/py-etherscan-api',
    license='MIT',
    author='daboooooo',
    author_email='dabo@dforce.network',
    description='Python Bindings to Etherscan.io API',
    install_requires=[
        'requests>=2.20.0',
    ],
    classifiers=[
        "Programming Language :: Python :: 3"
    ]
)
