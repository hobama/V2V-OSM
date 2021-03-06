from setuptools import setup

setup(name='vtovosm',
      version='0.1',
      description='Simulate Vehicle-to-vehicle communication on street networks obtained from OpenStreetMap',
      url='https://github.com/Dosenpfand/thesis_code',
      author='Markus Gasser, Thomas Blazek',
      author_email='markus.gasser@student.tuwien.ac.at, tblazek@nt.tuwien.ac.at',
      license='GPLv3+',
      packages=['vtovosm'],
      install_requires=['geopandas>=0.2.1',
                        'matplotlib>=2.0.2',
                        'networkx>=1.11,<2.0',
                        'numpy>=1.12.1',
                        'osmnx>=0.5.1,<0.6',
                        'requests>=2.14.2',
                        'scipy>=0.19.0',
                        'Shapely>=1.6.4'],
      test_suite='nose.collector',
      tests_require=['nose'])
