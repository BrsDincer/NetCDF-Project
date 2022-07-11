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