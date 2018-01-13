import bpy

class ImportFiles(bpy.types.Operator):
    bl_idname = "slideshow_composer.import_files"
    bl_label = "Import"
    bl_description = "Import all files from a directory"
    bl_options = {'REGISTER', 'UNDO'}

    filepath = bpy.props.StringProperty(subtype="FILE_PATH")
    directory = bpy.props.StringProperty(subtype="FILE_PATH")
    files = bpy.props.CollectionProperty(
        name="File Path",
        type=bpy.types.OperatorFileListElement,
    )

    @classmethod
    def poll(self, context):
        return True

    def execute(self, context):
        print("execute Import files from '{}'".format(self.filepath))
        return {'FINISHED'}

    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}

#if __name__ == "__main__":
#    bpy.utils.register_class(ImportFiles)