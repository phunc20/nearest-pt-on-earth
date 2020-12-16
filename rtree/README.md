## Installation of python packages
- `pip install geopy`
- `pip install rtree`
  - You might fail to install. See below
  - [must have `spatialindex` first](https://github.com/Toblerity/rtree/issues/88)
  - `pacman -S spatialindex`. Once `spatialindex` installed, try again `pip install rtree`

