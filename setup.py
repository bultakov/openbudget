from setuptools import setup

from openbudget import __version__

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name='OpenBudgetAPI',
    version=__version__,
    url='https://github.com/bultakov/openbudget',
    license='MIT',
    author='Ibrohim Bultakov',
    python_requires='>=3.7',
    author_email='bii23.uz@gmail.com',
    description='OpenBudget.uz uchun Asinxron kutubxona!!!',
    keywords=['OpenBudget', 'OpenBudget.uz', 'pypi', 'python', 'AsyncIO'],
    long_description_content_type="text/markdown",
    long_description=long_description,
    classifiers=[
        'Framework :: AsyncIO',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    install_requires=[
        'aiohttp>=3.8.0,<3.9.0',
    ],
    include_package_data=False,
)
