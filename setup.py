from setuptools import setup


setup(
    name='mousesens',
    version='0.1',
    py_modules=['mousesens'],
    intall_requires=['Click',],
    entry_points='''
        [console_scripts]
        mousesens=mousesens:cli
    ''',
)
