Blender Slideshow Composer
==========================

General information
-------------------
This is a Blender addon that can be used to generate slideshow presentations consisted of images and videos. It uses [Ken Burns effect](https://en.wikipedia.org/wiki/Ken_Burns_effect) to make nice-looking move effects of imported images. 

Can I use it for my project?
----------------------------
This addon was created for my own needs of creating holiday family movies. I'm releasing the source code - do whatever you want with it. Any contribution to this repository is highly welcome :)   

How to use it
-------------
Once installed, the plugin adds a menu to import files to the VSE Movie Clip Editor. The most common usage of this plugin is to import all image/movie files from a single directory. The files are ordered by name. Additionally, sub-folders are searched for files - that gives more control on import order, eg. files can be arranged in sub-folders that correspond to movie chapters. The following image shows example import result - image and movie strips are added to VSE editor along with appropriate cross effects.

![Imported strips example](docs/imported_strips.png)

Other options
--------------------
When using import option, transitions between strips are automatically generated. The generated transition can be changed for selected strip by using context menu. In order to add the context menu follow the steps:
1. Open up User Preferences -> Input tab
2. Expand Sequencer -> Sequencer (Global)
3. Create new Call Menu entry
5. Enter wm.call_menu in the first field
6. Enter slideshow_composer.main_menu as a name
7. Assign a key eg. Shift + Q

![Menu Key Shortcut](docs/blender_menu_shortcut.png)

Used libraries and 3rd party code
---------------------------------
* https://github.com/JacquesLucke/code_autocomplete

Additional Tools
-----
In tools folder there is a script to prepare files before importing to VSE. Use it if you want to

* Stabilize video files, remove camera shaking (requires [ffmpeg](https://www.ffmpeg.org/))
* Fix aspect ratio of images (requires [imagemagick](https://www.imagemagick.org/))
