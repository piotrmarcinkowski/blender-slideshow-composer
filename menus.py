import bpy

class SlideShowMainMenu(bpy.types.Menu):
    bl_label = "SlideShow Composer"
    bl_idname = "slideshow_composer.main_menu"

    def draw(self, context):
        layout = self.layout

        selection = bpy.context.selected_sequences

        layout.operator('slideshow_composer.import_files', icon='SEQUENCE', text='Import files')
    
#if __name__ == "__main__":
#    bpy.utils.register_class(SlideShowMainMenu)