from setuptools import setup

setup(
   name='KMeans',
   version='1.0',
   description='K-means algorithm in action!',
   author='Edgaras Lopatovas',
   author_email='lopatovas@gmail.com',
   packages=['KMeans'],
   install_requires=['numpy', 'pandas', 'matplotlib', 'sklearn']
)