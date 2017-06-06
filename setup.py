""" Grinder packaging instructions """

from setuptools import setup, find_packages

setup(
    name='grinder',
    packages=['grinder'],
    version='0.1',
    description='Dynamic environment deployment tool for SaltStack',
    author='FrozenFOXX',
    author_email='siliconfoxx@gmail.com',
    url='https://github.com/frozenfoxx/grinder',
    download_url='https://github.com/frozenfoxx/grinder/archive/0.1.tar.gz',
    keywords=['salt', 'devops', 'deployment', 'pillar'],
    classifiers=[],
    install_requires=[
        'gitpython',
        'pyyaml'
    ],
    scripts=[
        'scripts/grinder',
    ],
    data_files=[
        ('/etc/grinder', ['conf/grinder.conf'])
    ],
)
