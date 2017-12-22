bl_info = {
    "name": "SlideShow Composer",
    "description": "Helps creating slide shows from pictures/videos",
    "author": "Piotr Marcinkowski",
    "version": (0, 1, 0),
    "blender": (2, 78, 0),
    "location": "sequencer",    
    "wiki_url": "",    
    "category": "VSE"
}

import bpy
import os
from .menus import SlideShowMainMenu
from .operators import ImportFiles

def register():
    bpy.utils.register_class(SlideShowMainMenu)
    bpy.utils.register_class(ImportFiles)

def unregister():
    bpy.utils.unregister_class(SlideShowMainMenu)
    bpy.utils.unregister_class(ImportFiles)
