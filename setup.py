from distutils.core import setup
import glob, py2exe

setup(windows=[{"script":"pwdmngr.py","icon_resources":[(1,"gui/icons/app.ico")]}], 
      data_files=[("data",glob.glob("data/*.*")),
                  ("icons",glob.glob("gui/icons/*.png"))] 
      )