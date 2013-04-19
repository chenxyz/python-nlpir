# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.7
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.



from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_NLPIR', [dirname(__file__)])
        except ImportError:
            import _NLPIR
            return _NLPIR
        if fp is not None:
            try:
                _mod = imp.load_module('_NLPIR', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _NLPIR = swig_import_helper()
    del swig_import_helper
else:
    import _NLPIR
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


POS_MAP_NUMBER = _NLPIR.POS_MAP_NUMBER
ICT_POS_MAP_FIRST = _NLPIR.ICT_POS_MAP_FIRST
ICT_POS_MAP_SECOND = _NLPIR.ICT_POS_MAP_SECOND
PKU_POS_MAP_SECOND = _NLPIR.PKU_POS_MAP_SECOND
PKU_POS_MAP_FIRST = _NLPIR.PKU_POS_MAP_FIRST
POS_SIZE = _NLPIR.POS_SIZE
GBK_CODE = _NLPIR.GBK_CODE
UTF8_CODE = _NLPIR.UTF8_CODE
BIG5_CODE = _NLPIR.BIG5_CODE
GBK_FANTI_CODE = _NLPIR.GBK_FANTI_CODE

def NLPIR_Init(sDataPath=None, encode=0):
  return _NLPIR.NLPIR_Init(sDataPath, encode)
NLPIR_Init = _NLPIR.NLPIR_Init

def NLPIR_Exit():
  return _NLPIR.NLPIR_Exit()
NLPIR_Exit = _NLPIR.NLPIR_Exit

def NLPIR_ParagraphProcess(*args):
  return _NLPIR.NLPIR_ParagraphProcess(*args)
NLPIR_ParagraphProcess = _NLPIR.NLPIR_ParagraphProcess

def NLPIR_ParagraphProcessA(*args):
  return _NLPIR.NLPIR_ParagraphProcessA(*args)
NLPIR_ParagraphProcessA = _NLPIR.NLPIR_ParagraphProcessA

def NLPIR_GetParagraphProcessAWordCount(*args):
  return _NLPIR.NLPIR_GetParagraphProcessAWordCount(*args)
NLPIR_GetParagraphProcessAWordCount = _NLPIR.NLPIR_GetParagraphProcessAWordCount

def NLPIR_ParagraphProcessAW(*args):
  return _NLPIR.NLPIR_ParagraphProcessAW(*args)
NLPIR_ParagraphProcessAW = _NLPIR.NLPIR_ParagraphProcessAW

def NLPIR_FileProcess(*args):
  return _NLPIR.NLPIR_FileProcess(*args)
NLPIR_FileProcess = _NLPIR.NLPIR_FileProcess

def NLPIR_ImportUserDict(*args):
  return _NLPIR.NLPIR_ImportUserDict(*args)
NLPIR_ImportUserDict = _NLPIR.NLPIR_ImportUserDict

def NLPIR_AddUserWord(*args):
  return _NLPIR.NLPIR_AddUserWord(*args)
NLPIR_AddUserWord = _NLPIR.NLPIR_AddUserWord

def NLPIR_SaveTheUsrDic():
  return _NLPIR.NLPIR_SaveTheUsrDic()
NLPIR_SaveTheUsrDic = _NLPIR.NLPIR_SaveTheUsrDic

def NLPIR_DelUsrWord(*args):
  return _NLPIR.NLPIR_DelUsrWord(*args)
NLPIR_DelUsrWord = _NLPIR.NLPIR_DelUsrWord

def NLPIR_GetUniProb(*args):
  return _NLPIR.NLPIR_GetUniProb(*args)
NLPIR_GetUniProb = _NLPIR.NLPIR_GetUniProb

def NLPIR_IsWord(*args):
  return _NLPIR.NLPIR_IsWord(*args)
NLPIR_IsWord = _NLPIR.NLPIR_IsWord

def NLPIR_GetKeyWords(*args):
  return _NLPIR.NLPIR_GetKeyWords(*args)
NLPIR_GetKeyWords = _NLPIR.NLPIR_GetKeyWords

def NLPIR_GetFileKeyWords(*args):
  return _NLPIR.NLPIR_GetFileKeyWords(*args)
NLPIR_GetFileKeyWords = _NLPIR.NLPIR_GetFileKeyWords

def NLPIR_GetNewWords(*args):
  return _NLPIR.NLPIR_GetNewWords(*args)
NLPIR_GetNewWords = _NLPIR.NLPIR_GetNewWords

def NLPIR_GetFileNewWords(*args):
  return _NLPIR.NLPIR_GetFileNewWords(*args)
NLPIR_GetFileNewWords = _NLPIR.NLPIR_GetFileNewWords

def NLPIR_FingerPrint(*args):
  return _NLPIR.NLPIR_FingerPrint(*args)
NLPIR_FingerPrint = _NLPIR.NLPIR_FingerPrint

def NLPIR_SetPOSmap(*args):
  return _NLPIR.NLPIR_SetPOSmap(*args)
NLPIR_SetPOSmap = _NLPIR.NLPIR_SetPOSmap

def NLPIR_NWI_Start():
  return _NLPIR.NLPIR_NWI_Start()
NLPIR_NWI_Start = _NLPIR.NLPIR_NWI_Start

def NLPIR_NWI_AddFile(*args):
  return _NLPIR.NLPIR_NWI_AddFile(*args)
NLPIR_NWI_AddFile = _NLPIR.NLPIR_NWI_AddFile

def NLPIR_NWI_AddMem(*args):
  return _NLPIR.NLPIR_NWI_AddMem(*args)
NLPIR_NWI_AddMem = _NLPIR.NLPIR_NWI_AddMem

def NLPIR_NWI_Complete():
  return _NLPIR.NLPIR_NWI_Complete()
NLPIR_NWI_Complete = _NLPIR.NLPIR_NWI_Complete

def NLPIR_NWI_GetResult(bWeightOut=False):
  return _NLPIR.NLPIR_NWI_GetResult(bWeightOut)
NLPIR_NWI_GetResult = _NLPIR.NLPIR_NWI_GetResult

def NLPIR_NWI_Result2UserDict():
  return _NLPIR.NLPIR_NWI_Result2UserDict()
NLPIR_NWI_Result2UserDict = _NLPIR.NLPIR_NWI_Result2UserDict
# This file is compatible with both classic and new-style classes.


