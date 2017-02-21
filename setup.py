# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='travis-ci-python',
    version='0.1.1',
    url='https://github.com/mstuttgart/codigo-avulso-test-tutorial',
    license='MIT License',
    author='Marcelo Santos',
    author_email='marcelosantosadm@gmail.com',
    keywords='tutorial test unittest',
    description=u'Travis CI e teste unitário em Python',
    packages=find_packages(),
    install_requires=[],
    test_suite='test',
)
