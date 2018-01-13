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

    image_strip_frames = bpy.props.IntProperty(
        name="Image strip frames",
        description="How long imported images are displayed during playback",
        default=120,
        min=30)

    @classmethod
    def poll(self, context):
        return True

    def execute(self, context):
        self.create_strips()
        return {'FINISHED'}

    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}

    def create_strips(self):
        """ Creates strips for imported files """
        frame_current = bpy.context.scene.frame_current

        for file in self.files:
            file_list = [{'name': file['name']}]
            bpy.ops.sequencer.image_strip_add(
                directory=self.directory,
                files=file_list,
                show_multiview=False,
                frame_start=frame_current,
                frame_end=frame_current + self.image_strip_frames,
                channel=1)
            frame_current += self.image_strip_frames

#if __name__ == "__main__":
#    bpy.utils.register_class(ImportFiles)