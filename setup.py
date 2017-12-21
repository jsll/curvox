#!/usr/bin/env python

from distutils.core import setup

setup(name="curvox",
      version='1.0',
      description=
      """
      Python library with utilities for converting pointclouds, meshes,
      and voxel grids between ros messages, files matrices, objects
      """,
      author='David Watkins',
      author_email='davidwatkins@cs.columbia.edu',
      url='https://github.com/crlab/curvox',
      packages=['curvox'],
      dependency_links=[
        'https://github.com/crlab/binvox-rw-py/tarball/master#egg=binvox-rw-1.0',
        'https://github.com/ShapeCompletion3D/python-pcl/tarball/master#egg=python-pcl-0.3',
        'https://github.com/CRLab/MeshLabXML/tarball/master#egg=meshlabxml-2017.9',
        'https://github.com/GPflow/GPflow/tarball/master#egg=gpflow-1.1.0'
      ],
      install_requires=[
        "numpy >= 1.8",
        "binvox-rw >= 1.0",
        "plyfile >= 0.4",
        'python-pcl >= 0.2',
        'scipy',
        'matplotlib',
        'pymcubes',
        'meshlabxml >= 2017.9',
        'pyhull',
        'gpflow'
      ])
