import bpy

class ImportFiles(bpy.types.Operator):
    bl_idname = "slideshow_composer.import_files"
    bl_label = "SC.Import files"
    bl_description = "Import audio/video files creating VSE strips"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(self, context):
        return True

    def execute(self, c):
        print("Executed, just executing")

    def invoke(self, c, e):
        print("Invoked, taking user input")
        
#if __name__ == "__main__":
#    bpy.utils.register_class(ImportFiles)