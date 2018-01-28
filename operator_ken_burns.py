import bpy
from . import preferences
from . import keyframes

class KenBurnsEffect(bpy.types.Operator, preferences.KenBurnsEffectPreferences):
    bl_idname = "slideshow_composer.ken_burns_effect"
    bl_label = "Ken Burns Effect"
    bl_description = "Generate random Ken Burns effect on image transform strips"
    bl_options = {'REGISTER', 'UNDO'}

    replace = bpy.props.BoolProperty(
        name="Replace sequence existing effect",
        description="Remove previous sequence effect and generate new one",
        default=False
    )

    @classmethod
    def poll(self, context):
        return len(bpy.context.selected_sequences) == 1 and bpy.context.selected_sequences[0].type == 'TRANSFORM'

    def execute(self, context):
        self.generate_effect()
        return {'FINISHED'}

    def generate_effect(self):
        """ Generate Ken Burns effect for selected transform strip """
        transform_strip = bpy.context.selected_sequences[0]
        transform_strip.use_uniform_scale = True

        seq = bpy.context.selected_sequences[0]

        if self.replace is True:
            keyframes.delete_keyframes(seq)

        seq.scale_start_x = 1.0
        seq.keyframe_insert(data_path='scale_start_x', frame=seq.frame_start)
        # last added fcurve's keyframe_points interpolation
        bpy.context.scene.animation_data.action.fcurves[-1].keyframe_points[0].interpolation = "LINEAR"
        seq.scale_start_x = 1.3
        seq_last_frame = seq.frame_start + seq.frame_duration - 1;
        seq.keyframe_insert(data_path='scale_start_x', frame=seq_last_frame)

# if __name__ == "__main__":
#    bpy.utils.register_class(ImportFiles)
