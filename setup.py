from setuptools import setup

setup(name='Grigsby Python Package',
      version='0.1',
      description='Read a matrix and run BLAST searches',
      url='TBD',
      author='Courtney Grigsby',
      author_email='courtney.grigsby@selu.edu',
      license='MIT',
      packages=['grigsbypyhtonpackage'],
      install_requires=[
          'dendropy',
          'pandas',
          'biopyhton'
      ],
      long_description=open('README.txt').read(),
zip_safe=True)