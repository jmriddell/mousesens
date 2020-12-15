from setuptools import setup, find_packages


setup(
    name='mousesens',
    version='0.2',
    packages=find_packages(),
    intall_requires=['Click',],
    entry_points='''
        [console_scripts]
        mousesens=mousesens.mousesens:cli
    ''',
)
