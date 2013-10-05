#!/usr/bin/env python3

from setuptools import setup, find_packages
from setuptools.command.install import install
from subprocess import Popen

from pmclient import tools
from pmclient.setup_support import install_user_tool_symlink

version = '0.3.1'

def pre_install():
    try:
        Popen('lsb_release')
    except FileNotFoundError:
        print("lsb_release doesn't seem to be available. Please make sure "
              "that it's installed.")
        raise

    # The setuptools requirements check should catch this, but an exception
    # about a missing shared library might be confusing.
    print("Verifying that PySecure exists.")

    try:
        import pysecure
    except:
        print("PySecure can not be loaded. Please make sure that it's "
              "installed, along with its dependencies.")
        raise

def post_install():
    print("")
    install_user_tool_symlink('pmclient.tools.pm_config')
    install_user_tool_symlink('pmclient.tools.pm_push_dpkg')
    install_user_tool_symlink('pmclient.tools.pm_push_pacman')

    from pmclient.tools.pm_config import start_config
    start_config()

class custom_install(install):
    def run(self):
        pre_install()
        install.run(self)
        post_install()

setup(name='pmclient',
      version=version,
      description="A client for the Package Backup package-list backup service.",
      long_description="A client for the Package Backup package-list backup service.",
      classifiers=['Development Status :: 3 - Alpha',
                   'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
                   'Environment :: Console',
                   'Programming Language :: Python :: 3.0'
                  ],
      keywords='package-list packagelist backup packagebackup package-backup',
      author='Dustin Oprea',
      author_email='myselfasunder@gmail.com',
      url='https://github.com/dsoprea/PmClient',
      license='GPL2',
      packages=['pmclient'],
      include_package_data=True,
      zip_safe=True,
      install_requires=[
        'requests',
        'pysecure'
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      cmdclass={'install': custom_install
               },
      )

