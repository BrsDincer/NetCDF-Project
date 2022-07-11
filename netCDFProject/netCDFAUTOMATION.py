from __src__.__GlobalCreating__ import CREATEGLOBALALL
from __src__.__BASEMAPMesh__ import BASEMESH
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

DST = _IMPORTLIB("NETCDF")._LAUNCH()
"""
EXAMPLE PATH:
GEOS.fp.fcst.tavg1_2d_rad_Nx.20220706_00+20220710_2130.V01.nc4
inst1_2d_lfo_Nx-202206301646output.30331.webform.nc4
tavg1_2d_rad_Nx-202206281101output.1555.webform.nc4
"""
class CDFAKOM(object):
    def __new__(cls,pathdir:str):
        retobj = object.__new__(cls)
        return retobj
    def __init__(self,pathdir:str):
        self.__pth = pathdir
    def __str__(self):
        return "FUNCTION IS CREATED FOR NETCDF PROCESS"
    def __call__(self):
        return
    def __getstate__(self):
        raise TypeError("[X] PICKLED DENIED")
    def _RETURN_DT(self):
        return DST(self.__pth)
    def _CREATE_GLOBAL(self,ncc):
        print("\n"+"[>>] GLOBAL PARAMETERS / CREATING")
        llat,llon,ldat,lnam,xnam = CREATEGLOBALALL(ncc)._GET_GLOBALS()
        print("[+] DONE [+]"+"\n")
        return llat,llon,ldat,lnam,xnam
    def _RETURN_PARAMETERS(self,ncc):
        paramsname = ""
        _,_,_,lnam,_ = CREATEGLOBALALL(ncc)._GET_GLOBALS()
        lenl = len(lnam)
        icon = 0
        paramsname += "[>>] PARAMETERS"+"\n"
        while lenl > 0:
            paramsname += f"""
            {icon}) {lnam[icon]}
    
            """
            lenl -= 1
            icon += 1
        return paramsname
    def _SHOW_PARAMETERS(self):
        ncdat = self._RETURN_DT()
        parname = self._RETURN_PARAMETERS(ncdat)
        return parname
    def _MAP(self):
        ncdat = self._RETURN_DT()
        llat,llon,ldat,lnam,xnam = self._CREATE_GLOBAL(ncdat)
        params = self._SHOW_PARAMETERS()
        print(params)
        userparams = input("[>>] CHOOSE DATA: ")
        BASEMESH(llat[0],llon[0],xnam[str(userparams)],ncdat.variables[str(userparams)])._GET_MAP()
    def _MAPSPEC(self):
        pass
  
    
if __name__ == "__main__":
    inusr = input("\n"+"[>] DATA PATH: ")
    print("[>>] WAIT FOR RESULT")
    CDFAKOM(inusr)._MAP()
