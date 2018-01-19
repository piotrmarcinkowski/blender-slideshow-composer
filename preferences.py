import bpy

class SlideshowComposerPreferences(bpy.types.AddonPreferences):
    # this must match the addon name, use '__package__'
    # when defining this in a submodule of a python package.
    bl_idname = __package__

    image_strip_frames = bpy.props.IntProperty(
            name = "Image strip frames",
            description="Number of frames each imported image strip will last",
            default = 90,
            min = 5
            )

    strips_cross_frames = bpy.props.IntProperty(
        name="Strips cross effect frames",
        description="Number of frames the cross effect between two strips will last",
        default=10,
        min=5
    )

    def draw(self, context):
        layout = self.layout
        layout.label(text="Slideshow Composer preferences")
        layout.prop(self, "image_strip_frames")
        layout.prop(self, "strips_cross_frames")

