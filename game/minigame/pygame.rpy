# https://www.renpy.org/wiki/renpy/frameworks/Renpygame
init python:
   import renpygame
   import renpygame as pygame
   from renpygame.locals import *

   def set_mode():
        if _preferences.fullscreen:
            fsflag = FULLSCREEN
        else:
            fsflag = 0

        screen = renpygame.display.set_mode((800, 600), fsflag, 32)
        return screen
