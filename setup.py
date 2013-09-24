#!/usr/bin/python

from setuptools import setup, find_packages

version = '0.1.0'

setup(name='pmclient',
      version=version,
      description="A client for the Package Monitor package-list backup service.",
      long_description="A client for the Package Monitor package-list backup service.",
      classifiers=['Development Status :: 3 - Alpha',
                   'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
                   'Environment :: Console',
                   'Programming Language :: Python :: 3.0'
                  ],
      keywords='package-list packagelist backup packagemonitor package-monitor',
      author='Dustin Oprea',
      author_email='myselfasunder@gmail.com',
      url='https://github.com/dsoprea/PmClient',
      license='GPL2',
      packages=['pmclient'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'requests',
        'snackwich',
        'pysecure'
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
