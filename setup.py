#!/usr/bin/env python

from setuptools import setup

setup(name='pyqt5-demo',
      version='1.0',
      description='Demo of a PyQt5 app',
      author='Dariusz Gadomski',
      author_email='dgadomski@ubuntu.com',
      url='https://github.com/dargad/pyqt5-demo',
      packages=['pyqt5demo'],
      install_requires=[
          'PyQt5',
      ],
      entry_points={
          'gui_scripts': ['pyqt5demo=pyqt5demo.hello_world:main']
      },
     )
