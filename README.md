# curvox
Utility functions for pointclouds, meshes, and voxel grids.

mesh_conversions.py has utilities for converting meshes between ply objects, and ros messages.

cloud_conversions.py has utilities for converting pointclouds between numpy arrays, pointcloud objects, and ros messages

pc_vox_utils.py is for generating binvox files from pointclouds.


## Install
```bash
$ wget http://www.patrickmin.com/binvox/linux64/binvox
$ chmod a+x binvox
$ mv binvox $HOME/.local/bin
$ sudo apt install python-pytest
$ pip2 install -r requirements.txt --user
$ python2 setup.py install --user
```

## Tests
A few tests have been written in the `tests` folder. In order to run the test suite
```bash
$ cd tests
$ py.test
```

## Dependencies

- [ros_numpy](https://github.com/eric-wieser/ros_numpy)
