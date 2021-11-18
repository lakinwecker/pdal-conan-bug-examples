Instructions
============
1. Install python/poetry
2. Use poetry to install conan/python deps
```
poetry shell
poetry install
```
3. Use invoke to setup profile/install conan deps
```
invoke conanprofile
invoke installdeps
```
4. Use invoke to setup cmake/build
```
invoke cmake
invoke build
```
5. Run resulting example code:
```
./build/release/bin/example
```

Observe that the static one has this output:
```
➜ ./build/release/bin/example
Printing available plugins!
Done!
```

While the shared one has this output (which is correct)
```
➜ ./build/release/bin/example
Printing available plugins!
Available Plugin: filters.approximatecoplanar
Available Plugin: filters.assign
Available Plugin: filters.chipper
Available Plugin: filters.cluster
Available Plugin: filters.colorinterp
Available Plugin: filters.colorization
Available Plugin: filters.covariancefeatures
Available Plugin: filters.crop
Available Plugin: filters.csf
Available Plugin: filters.dbscan
Available Plugin: filters.decimation
Available Plugin: filters.delaunay
Available Plugin: filters.dem
Available Plugin: filters.divider
Available Plugin: filters.eigenvalues
Available Plugin: filters.elm
Available Plugin: filters.estimaterank
Available Plugin: filters.faceraster
Available Plugin: filters.ferry
Available Plugin: filters.fps
Available Plugin: filters.gpstimeconvert
Available Plugin: filters.greedyprojection
Available Plugin: filters.groupby
Available Plugin: filters.hag_delaunay
Available Plugin: filters.hag_dem
Available Plugin: filters.hag_nn
Available Plugin: filters.head
Available Plugin: filters.hexbin
Available Plugin: filters.icp
Available Plugin: filters.info
Available Plugin: filters.iqr
Available Plugin: filters.litree
Available Plugin: filters.lloydkmeans
Available Plugin: filters.locate
Available Plugin: filters.lof
Available Plugin: filters.mad
Available Plugin: filters.merge
Available Plugin: filters.miniball
Available Plugin: filters.mongo
Available Plugin: filters.mortonorder
Available Plugin: filters.neighborclassifier
Available Plugin: filters.nndistance
Available Plugin: filters.normal
Available Plugin: filters.optimalneighborhood
Available Plugin: filters.outlier
Available Plugin: filters.overlay
Available Plugin: filters.planefit
Available Plugin: filters.pmf
Available Plugin: filters.poisson
Available Plugin: filters.projpipeline
Available Plugin: filters.radialdensity
Available Plugin: filters.randomize
Available Plugin: filters.range
Available Plugin: filters.reciprocity
Available Plugin: filters.relaxationdartthrowing
Available Plugin: filters.reprojection
Available Plugin: filters.returns
Available Plugin: filters.sample
Available Plugin: filters.separatescanline
Available Plugin: filters.shell
Available Plugin: filters.skewnessbalancing
Available Plugin: filters.smrf
Available Plugin: filters.sort
Available Plugin: filters.splitter
Available Plugin: filters.stats
Available Plugin: filters.streamcallback
Available Plugin: filters.tail
Available Plugin: filters.transformation
Available Plugin: filters.voxelcenternearestneighbor
Available Plugin: filters.voxelcentroidnearestneighbor
Available Plugin: filters.voxeldownsize
Available Plugin: readers.bpf
Available Plugin: readers.ept
Available Plugin: readers.faux
Available Plugin: readers.gdal
Available Plugin: readers.ilvis2
Available Plugin: readers.las
Available Plugin: readers.memoryview
Available Plugin: readers.obj
Available Plugin: readers.optech
Available Plugin: readers.pcd
Available Plugin: readers.ply
Available Plugin: readers.pts
Available Plugin: readers.qfit
Available Plugin: readers.sbet
Available Plugin: readers.terrasolid
Available Plugin: readers.text
Available Plugin: readers.tindex
Available Plugin: writers.bpf
Available Plugin: writers.ept_addon
Available Plugin: writers.gdal
Available Plugin: writers.gltf
Available Plugin: writers.las
Available Plugin: writers.null
Available Plugin: writers.ogr
Available Plugin: writers.pcd
Available Plugin: writers.ply
Available Plugin: writers.raster
Available Plugin: writers.sbet
Available Plugin: writers.text
Done!
```
