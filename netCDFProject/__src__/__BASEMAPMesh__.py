import numpy,os

class CDFCHECK(object):
    def __new__(cls,datainit):
        retobj = object.__new__(cls)
        return retobj
    def __init__(self,datainit):
        self.__dat = datainit
        self.__lstvar = list(self.__dat.variables.keys())
        self.__dvar = self.__dat.variables
    def __str__(self):
        return "FUNCTION IS CREATED FOR NETCDF CHECKING"
    def __call__(self):
        mAll = [xf for xf in dir(CDFCHECK) if callable(getattr(CDFCHECK,xf)) and not xf.startswith("__")]
        return mAll
    def __getstate__(self):
        raise TypeError("[X] PICKLED DENIED")
    def _VARIABLE_KEYS(self):
        return self.__lstvar
    def _KEY_INFO(self,params:str):
        return self.__dvar[params]
    def _KEY_VARIABLES(self,params:str):
        return list(self.__dvar[params].__dict__)
    def _KEY_VAR_RETURN(self,params:str):
        gAtt = self._KEY_VARIABLES(params)
        for xl in gAtt: yield xl,self.__dvar[params].__dict__.get(xl)
    def _KEY_DETAILED(self,params:str):
        __repr = ""
        gInfo = list(self._KEY_VAR_RETURN(params))
        gLen = len(gInfo)
        for xr in range(gLen): __repr += f"{gInfo[xr][0]}: {gInfo[xr][1]}"+"\n"+"---"*7+"\r\n"
        return __repr
    def _ALL_DETAILED(self):
        for xl in range(len(self.__lstvar)):
            print(self.__lstvar[xl]+"\n"+"---"*7+"\n"+str(self._KEY_DETAILED(self.__lstvar[xl]))+"\n")

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

bmap = _IMPORTLIB("BASEMAP")._LAUNCH()
np = _IMPORTLIB("NUMPY")._LAUNCH()
plt = _IMPORTLIB("MATPLOT")._LAUNCH()

class BASEMESH(object):
    def __new__(cls,lati,loni,datai,defm):
        retobj = object.__new__(cls)
        return retobj
    def __init__(self,lati,loni,datai,defm):
        self.__lat = lati
        self.__lon = loni
        self.__dat = datai
        self.__mnd = defm
        self.__bmp = bmap(projection="cyl",resolution="c")
    def __str__(self):
        return "FUNCTION IS CREATED FOR BASEMAP"
    def __call__(self):
        return
    def __getstate__(self):
        raise TypeError("[X] PICKLED DENIED")
    def _ARRANGE_COOR(self):
        clon,clat = np.meshgrid(self.__lon,self.__lat)
        return clon,clat
    def _ARRANGE_WRLD(self):
        parr = np.arange(-90,91,30.)
        merr = np.arange(0,360,60.)
        return parr,merr
    def _GET_MAP(self,
                 cntclr:str="black",
                 lwdth:int=0.6,
                 clwdth:str="0.6",
                 prclr:str="0.6",
                 dmap:str="gist_heat",
                 cntwdth:int=2,
                 lnstyl:str="--",
                 fgsize:tuple=(12,7),
                 lcolor:str="Linen",
                 ocolor:str="#CCFFFF"):
        clon,clat = self._ARRANGE_COOR()
        parr,merr = self._ARRANGE_WRLD()
        try:
            llname = self.__mnd.long_name
        except:
            llname = "N/A"
        try:
            lunit = self.__mnd.units
        except:
            lunit = "N/A"
        fig = plt.figure(figsize=fgsize)
        self.__bmp.drawcoastlines(color=clwdth,linewidth=lwdth)
        self.__bmp.fillcontinents(color=cntclr,alpha=0.3)
        self.__bmp.drawstates()
        self.__bmp.drawcountries(color=prclr,linewidth=lwdth,linestyle=lnstyl)
        self.__bmp.drawlsmask(land_color=lcolor,ocean_color=ocolor)
        self.__bmp.drawcounties()
        self.__bmp.drawparallels(parr,
                                 labels=[1,0,0,1],
                                 fontsize=10,
                                 dashes=[1,1],
                                 linewidth=0.25,
                                 color=prclr)
        self.__bmp.drawmeridians(merr,
                                 labels=[1,0,0,1],
                                 fontsize=10,
                                 dashes=[1,1],
                                 linewidth=0.25,
                                 color=prclr)
        tempf = self.__bmp.pcolormesh(clon,clat,self.__dat,cmap=dmap)
        colrb = self.__bmp.colorbar(tempf,"right",size="2%",pad="2%")
        colrb.set_label(f"DENSITY - {str(lunit)}")
        plt.tight_layout()
        plt.title(llname,fontsize=18)
        plt.draw()
        plt.show()
            
            
class BASEMESHSPEC(object):
    def __new__(cls,
                lati,
                loni,
                datai,
                defm,
                lllat:int,
                lllon:int,
                urlat:int,
                urlon:int):
        retobj = object.__new__(cls)
        return retobj
    def __init__(self,
                 lati,
                 loni,
                 datai,
                 defm,
                 lllat:int,
                 lllon:int,
                 urlat:int,
                 urlon:int):
        self.__lat = lati
        self.__lon = loni
        self.__dat = datai
        self.__mnd = defm
        self.__lla = lllat
        self.__lll = lllon
        self.__urt = urlat
        self.__url = urlon
        self.__bmp = bmap(projection="cyl",
                          llcrnrlat=self.__lla,
                          llcrnrlon=self.__lll,
                          urcrnrlat=self.__urt,
                          urcrnrlon=self.__url,
                          resolution="c")
    def __str__(self):
        return "FUNCTION IS CREATED FOR BASEMAP"
    def __call__(self):
        return
    def __getstate__(self):
        raise TypeError("[X] PICKLED DENIED")
    def _ARRANGE_COOR(self):
        clon,clat = np.meshgrid(self.__lon,self.__lat)
        return clon,clat
    def _ARRANGE_WRLD(self):
        parr = np.arange(-90,91,30.)
        merr = np.arange(0,360,60.)
        return parr,merr
    def _GET_MAP(self,
                 cntclr:str="black",
                 lwdth:int=0.6,
                 clwdth:str="0.6",
                 prclr:str="0.6",
                 dmap:str="gist_heat",
                 cntwdth:int=2,
                 lnstyl:str="--",
                 fgsize:tuple=(12,7),
                 lcolor:str="Linen",
                 ocolor:str="#CCFFFF"):
        clon,clat = self._ARRANGE_COOR()
        parr,merr = self._ARRANGE_WRLD()
        try:
            llname = self.__mnd.long_name
        except:
            llname = "N/A"
        try:
            lunit = self.__mnd.units
        except:
            lunit = "N/A"
        fig = plt.figure(figsize=fgsize)
        self.__bmp.drawcoastlines(color=clwdth,linewidth=lwdth)
        self.__bmp.fillcontinents(color=cntclr,alpha=0.3)
        self.__bmp.drawstates()
        self.__bmp.drawcountries(color=prclr,linewidth=lwdth,linestyle=lnstyl)
        self.__bmp.drawlsmask(land_color=lcolor,ocean_color=ocolor)
        self.__bmp.drawcounties()
        self.__bmp.drawparallels(parr,
                                 labels=[1,0,0,1],
                                 fontsize=10,
                                 dashes=[1,1],
                                 linewidth=0.25,
                                 color=prclr)
        self.__bmp.drawmeridians(merr,
                                 labels=[1,0,0,1],
                                 fontsize=10,
                                 dashes=[1,1],
                                 linewidth=0.25,
                                 color=prclr)
        tempf = self.__bmp.pcolormesh(clon,clat,self.__dat,cmap=dmap)
        colrb = self.__bmp.colorbar(tempf,"right",size="2%",pad="2%")
        colrb.set_label(f"DENSITY - {str(lunit)}")
        plt.tight_layout()
        plt.title(llname,fontsize=18)