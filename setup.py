from setuptools import setup

setup(
    name='startme-examples',
    version='0.1',
    url='https://github.com/yaroslaff/startme-examples',

    description='Example plugins for startme',
    long_description='Example plugin modules for startme',
    author='Yaroslav Polyakov',
    author_email='yaroslaff@gmail.com',

    license='Apache Software License',


    install_requires=['startme'],
    packages=[
        'startme.mods.ex_boot', 
        'startme.mods.ex_cron'
        ],
    zip_safe=False,
)

