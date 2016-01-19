from setuptools import setup

setup(
    name='lektor-surge',
    version='0.2+',
    author=u'A. Jesse Jiryu Davis',
    author_email='jesse@emptysquare.net',
    license='MIT',
    py_modules=['lektor_surge'],
    install_requires=['Lektor'],
    url='https://github.com/ajdavis/lektor-surge',
    entry_points={
        'lektor.plugins': [
            'surge = lektor_surge:SurgePlugin',
        ]
    }
)
