from setuptools import setup

setup(
    name='Flask Time API',
    version='1.0',
    long_description=__doc__,
    packages=['demoflasktimeapi'],
    include_package_data=True,
    zip_safe=False,
    install_requires=['Flask']
)