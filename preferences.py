import bpy

class SlideshowComposerPreferences(bpy.types.AddonPreferences):
    # this must match the addon name, use '__package__'
    # when defining this in a submodule of a python package.
    bl_idname = __package__

    imageStripFrames = bpy.props.IntProperty(
            name = "Image strip frames",
            description="Number of frames the images will get while importing to sequencer",
            default = 90,
            min = 5
            )

    def draw(self, context):
        layout = self.layout
        layout.label(text="Slideshow Composer preferences")
        layout.prop(self, "imageStripFrames")

