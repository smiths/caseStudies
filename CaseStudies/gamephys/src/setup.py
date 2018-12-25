from setuptools import setup, find_packages

setup(name='Tamias2D',
      version='0.1',
      description='A physics engine',
      packages=find_packages(),
      install_requires=[
          'collision',
          'matplotlib',
          'pygame',
          'scipy',
          'pytest',

      ],
      tests_require=['pytest'],
      zip_safe=False)
