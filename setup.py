from setuptools import setup, find_packages
import sys, os

version = '1.0'

setup(name='fpost',
      version=version,
      description="Flask Post",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Narayanaperumal Gurusamy',
      author_email='gnperumal@gmail.com',
      url='',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
          'SQLAlchemy<=0.7.8',
          'Flask>=0.10',
          'Flask-SQLAlchemy>=1.0',
          'sqlalchemy-migrate>=0.7.2'
      ],
      entry_points={
            'console_scripts':[
                  'fpost = fpost.scripts.server:main',
                  'fpost_db = fpost.scripts.db:main'
            ]
      },
      )
