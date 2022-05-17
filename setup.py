from setuptools import setup

setup(
    name='startme-ex-boot',
    version='0.1',
    url='https://github.com/yaroslaff/startme-ex-boot',

    description='Example plugin for startme',
    long_description='Example plugin module for startme',
    author='Yaroslav Polyakov',
    author_email='yaroslaff@gmail.com',

    license='Apache Software License',

    packages=['startme.mods.exboot'],
    zip_safe=False,
)

