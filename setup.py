#!/usr/bin/env python

from distutils.core import setup

setup(name='jupyterlab_hdf',
      version='0.1',
      description='Jupyterlab server extension for handling hdf files',
      author='Kitware, Inc',
      author_email='doruk.ozturk@kitware.com',
      url='',
      packages=['jupyterlab_hdf'],
      install_requires=[
          'jupyterlab'
      ]
)
