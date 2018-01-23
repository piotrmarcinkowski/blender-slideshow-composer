import bpy

class KenBurnsEffectPreferences:
    ken_burns_transformation_x_max = bpy.props.FloatProperty(
        name="Transformation X max",
        description="Ken Burns effect horizontal transformation max value",
        default=2.5,
        min=0,
        max=50
    )

    ken_burns_transformation_y_max = bpy.props.FloatProperty(
        name="Transformation Y max",
        description="Ken Burns effect vertical transformation max value",
        default=2.5,
        min=0,
        max=50
    )

    ken_burns_transformation_scale_max = bpy.props.FloatProperty(
        name="Scale max",
        description="Ken Burns effect scale max value",
        default=1.15,
        max=1.5,
        min=1.0
    )

    ken_burns_transformation_rotation_max = bpy.props.FloatProperty(
        name="Rotation max",
        description="Ken Burns effect rotation max value",
        default=0.0,
        max=5.0,
        min=0.0
    )

    ken_burns_combined_effect_probability = bpy.props.IntProperty(
        name="Combined effect probability (%)",
        description="Probability of applying multiple effects on one image",
        default=10,
        min=0,
        max=100
    )

class SlideshowComposerPreferences(bpy.types.AddonPreferences, KenBurnsEffectPreferences):
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
        box = layout.box();
        box.label(text="Ken Burns effect for images")
        box.prop(self, "ken_burns_transformation_x_max")
        box.prop(self, "ken_burns_transformation_y_max")
        box.prop(self, "ken_burns_transformation_scale_max")
        box.prop(self, "ken_burns_transformation_rotation_max")
        box.prop(self, "ken_burns_combined_effect_probability")