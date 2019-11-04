# If you see `xxxxxxxx.so.x: cannot open shared object file: No such file or directory` on runtime
You need to add the libraries into your deplyment package.

`retrieve_so.sh` (for linux/mac) or `retrieve_so.bat` (for windows) with appropriate `necessry_libraries.txt`, `addtional_packages.txt` can get the libraries

# Examples
## 1. opencv-python-headless
This pip package needs `libglib-2.0.so.0` and `libgthread-2.0.so.0`.

### necessry_libraries.txt
```
# Necessary libraries needed to make pip modules work fine.
libgthread-2.0.so.0
libglib-2.0.so.0
```

### addtional_packages.txt
```
# Additional packages in order to get libraries which are described in necessary_libraries.txt
libglib2.0-0
```

## 2. xgboost / lightgbm
These pip package may need `libgomp.so.1` according to the following issues.

  - https://github.com/Azure/azure-functions-python-worker/issues/514
  - https://github.com/Azure/azure-functions-python-worker/issues/493

### necessry_libraries.txt
```
# Necessary libraries needed to make pip modules work fine.
libgomp.so.1
```

### addtional_packages.txt
```
# Additional packages in order to get libraries which are described in necessary_libraries.txt
libgomp1
```

# Internal process of the scripts
This is just FYI.

The scripts execute following steps.

  1. Launch docker container `mcr.microsoft.com/azure-functions/python`.
  1. Copy `necessry_libraries.txt` and `addtional_packages.txt` into the container.
  1. Install the packages, which is descrived in `necessry_libraries.txt`, into the container.
  1. Copy the libraries, which is descrived in `addtional_packages.txt` and installed by the previous step, from the container to `./lib` in your local PC.
  1. Shutdown and remove the container.
