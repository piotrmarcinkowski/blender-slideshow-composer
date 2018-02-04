import bpy
import random
from . import preferences
from . import keyframes

class KenBurnsEffect(bpy.types.Operator, preferences.KenBurnsEffectPreferences):
    bl_idname = "slideshow_composer.ken_burns_effect"
    bl_label = "Ken Burns Effect"
    bl_description = "Generate random Ken Burns effect on image transform strips"
    bl_options = {'REGISTER', 'UNDO'}

    replace = bpy.props.BoolProperty(
        name="Replace existing sequence effect",
        description="Remove previous sequence effect and generate new one",
        default=False
    )

    class Animation:
        def __init__(self, sequence):
            self.sequence = sequence
            self.reverse = bool(random.getrandbits(1))

        def get_data_path(self):
            raise NotImplementedError("Override and return data_path")

        def set_up_first_keyframe(self):
            raise NotImplementedError("Override and set appropriate property's value before creating a keyframe")

        def set_up_second_keyframe(self):
            raise NotImplementedError("Override and set appropriate property's value before creating a keyframe")

        def get_initial_scale(self):
            return 1.0

        def generate(self):
            if self.reverse:
                self.set_up_second_keyframe()
            else:
                self.set_up_first_keyframe()
            data_path=self.get_data_path()
            self.create_keyframe(data_path=data_path, frame=self.sequence.frame_start)
            if self.reverse:
                self.set_up_first_keyframe()
            else:
                self.set_up_second_keyframe()
            seq_last_frame = self.sequence.frame_start + self.sequence.frame_duration - 1;
            self.create_keyframe(data_path=data_path, frame=seq_last_frame)

        def create_keyframe(self, data_path, frame):
            self.sequence.keyframe_insert(data_path=data_path, frame=frame, group=KenBurnsEffect.get_fcurves_group_name())
            # last added fcurve's keyframe_points interpolation
            bpy.context.scene.animation_data.action.fcurves[-1].keyframe_points[0].interpolation = "LINEAR"

    class ScaleAnimation(Animation):
        def get_data_path(self):
            return 'scale_start_x'

        def set_up_first_keyframe(self):
            self.sequence.scale_start_x = 1.0

        def set_up_second_keyframe(self):
            self.sequence.scale_start_x = 1.3

    @classmethod
    def poll(self, context):
        # Check if image transform strip is selected
        return len(bpy.context.selected_sequences) == 1 and \
               bpy.context.selected_sequences[0].type == 'TRANSFORM' and \
               bpy.context.selected_sequences[0].input_1.type == 'IMAGE'

    def execute(self, context):
        self.generate_effect()
        return {'FINISHED'}

    def generate_effect(self):
        """ Generate Ken Burns effect for selected transform strip """
        transform_strip = bpy.context.selected_sequences[0]
        transform_strip.use_uniform_scale = True
        group = KenBurnsEffect.get_fcurves_group_name()

        seq = bpy.context.selected_sequences[0]
        image_width = seq.input_1.elements[0].orig_width

        # remove previously generated effect keyframes
        if self.replace is True:
            keyframes.delete_keyframes(seq, group=group)

        animation = KenBurnsEffect.ScaleAnimation(seq)
        animation.generate()

    def generate_random_value(self, min, max):
        return random.uniform(min, max)

    @staticmethod
    def get_fcurves_group_name():
        return 'KenBurnsEffect'

# if __name__ == "__main__":
#    bpy.utils.register_class(ImportFiles)
