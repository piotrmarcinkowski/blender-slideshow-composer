import bpy
from . import preferences

class KenBurnsEffect(bpy.types.Operator, preferences.KenBurnsEffectPreferences):
    bl_idname = "slideshow_composer.ken_burns_effect"
    bl_label = "Ken Burns Effect"
    bl_description = "Generate random Ken Burns effect on image transform strips"
    bl_options = {'REGISTER', 'UNDO'}

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
        

# if __name__ == "__main__":
#    bpy.utils.register_class(ImportFiles)
