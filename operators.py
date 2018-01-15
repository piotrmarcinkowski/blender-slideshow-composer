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

    imageStripFrames = bpy.props.IntProperty(
        name="Image strip frames",
        description="Number of frames the images will get while importing to sequencer",
        default=90,
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
            frame_end = frame_current + self.imageStripFrames
            self.create_strip(
                path = file['name'],
                frame_start= frame_current,
                frame_end= frame_end,
                channel = 1)

            self.create_transform(
                frame_start=frame_current,
                frame_end=frame_end)

            frame_current = frame_end + 1

    def create_strip(self, path, frame_start, frame_end, channel):
        file_list = [{'name': path}]

        bpy.ops.sequencer.image_strip_add(
            directory = self.directory,
            files = file_list,
            show_multiview = False,
            frame_start = frame_start,
            frame_end = frame_end,
            channel = channel)

    def create_transform(self, frame_start, frame_end):
        bpy.ops.sequencer.effect_strip_add(frame_start=frame_start, frame_end=frame_end, type='TRANSFORM')

#if __name__ == "__main__":
#    bpy.utils.register_class(ImportFiles)