import bpy

class SlideShowMainMenu(bpy.types.Menu):
    bl_label = "SlideShow Composer"
    bl_idname = "slideshow_composer.main_menu"

    def draw(self, context):
        user_preferences = context.user_preferences
        addon_prefs = user_preferences.addons[__package__].preferences
        layout = self.layout

        layout.operator_context = 'INVOKE_DEFAULT'
        layout.operator('slideshow_composer.import_files', icon='SEQUENCE', text='Import files')
        operator_props = layout.operator('slideshow_composer.ken_burns_effect', icon='SEQUENCE', text='Ken Burns effect')
        operator_props.ken_burns_transformation_x_max = addon_prefs.ken_burns_transformation_x_max
        operator_props.ken_burns_transformation_y_max = addon_prefs.ken_burns_transformation_y_max
        operator_props.ken_burns_transformation_scale_max = addon_prefs.ken_burns_transformation_scale_max
        operator_props.ken_burns_transformation_rotation_max = addon_prefs.ken_burns_transformation_rotation_max
        operator_props.ken_burns_combined_effect_probability = addon_prefs.ken_burns_combined_effect_probability

if __name__ == "__main__":
   bpy.utils.register_class(SlideShowMainMenu)