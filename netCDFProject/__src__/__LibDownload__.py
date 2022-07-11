import os

class _IMPORTLIB(object):
    def __new__(cls,desiredparams:str):
        retobj = object.__new__(cls)
        return retobj
    def __init__(self,desiredparams:str):
        self.__dsr = desiredparams.upper()
    def __str__(self):
        return "FUNCTION IS CREATED FOR IMPORT LIBRARIES"
    def __call__(self):
        return
    def __getstate__(self):
        raise TypeError("[X] PICKLED DENIED")
    def _LAUNCH(self):
        if isinstance(self.__dsr,str):
            if self.__dsr == "IGR":
                from warnings import filterwarnings
                filterwarnings("ignore",category=DeprecationWarning)
                filterwarnings("ignore",category=FutureWarning)
                filterwarnings("ignore",category=UserWarning)
            elif self.__dsr == "NETCDF":
                try:
                    from netCDF4 import Dataset
                    return Dataset
                except:
                    os.system("pip install netCDF4")
                    from netCDF4 import Dataset
                    return Dataset
            elif self.__dsr == "MATPLOT":
                try:
                    import matplotlib.pyplot as plt
                    return plt
                except:
                    os.system("pip install matplotlib")
                    import matplotlib.pyplot as plt
                    return plt
            elif self.__dsr == "NUMPY":
                try:
                    import numpy as np
                    return np
                except:
                    os.system("pip install numpy")
                    import numpy as np
                    return np
            elif self.__dsr == "MAP":
                try:
                    import matplotlib.animation as anm
                except:
                    os.system("pip install matplotlib")
                    import matplotlib.animation as anm
                try:
                    from IPython.display import HTML
                except:
                    os.system("pip install ipython")
                    from IPython.display import HTML
                try:
                    import cartopy as ccr
                    import cartopy.crs as ccrs
                except:
                    os.system("pip install Cartopy")
                    import cartopy as ccr
                    import cartopy.crs as ccrs
                return anm,HTML,ccr,ccrs
            elif self.__dsr == "BASEMAP":
                try:
                    from mpl_toolkits.basemap import Basemap
                    return Basemap
                except:
                    os.system("pip install basemap")
                    os.system("pip install basemap-data")
                    from mpl_toolkits.basemap import Basemap
                    return Basemap
            else:
                raise AttributeError("[?] UNACCEPTABLE INPUT")