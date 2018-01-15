import bpy


class SlideshowComposerPanel(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Slideshow Composer panel"
    bl_idname = "slideshow_composer.seqencer_panel"
    bl_category = "Slideshow"
    bl_space_type = 'SEQUENCE_EDITOR'
    bl_region_type = 'UI'

    @staticmethod
    def has_sequencer(context):
        return (context.space_data.view_type in {'SEQUENCER', 'SEQUENCER_PREVIEW'})

    @classmethod
    def poll(cls, context):
        #return cls.has_sequencer(context) and (act_strip(context) is not None)
        return True

    def draw(self, context):
        
        user_preferences = context.user_preferences
        addon_prefs = user_preferences.addons[__package__].preferences
    
        layout = self.layout

        row = layout.row()
        row.prop(addon_prefs, "imageStripFrames")

        row = layout.row()
        operator_props = row.operator("slideshow_composer.import_files")
        operator_props.imageStripFrames = addon_prefs.imageStripFrames

