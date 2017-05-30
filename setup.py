from distutils.core import setup

setup(
    name = 'grinder',
    packages = ['grinder'],
    version = '0.1',
    description = 'Dynamic environment deployment tool for SaltStack',
    author = 'FrozenFOXX',
    author_email = 'siliconfoxx@gmail.com',
    url = 'https://github.com/frozenfoxx/grinder',
    download_url = 'https://github.com/frozenfoxx/grinder/archive/0.1.tar.gz',
    keywords = ['salt', 'devops', 'deployment', 'pillar'],
    classifiers = [],
    scripts = [
        'scripts/grinder',
    ],
)
