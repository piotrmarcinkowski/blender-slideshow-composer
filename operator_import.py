import bpy
from . import preferences

class ImportFiles(bpy.types.Operator, preferences.ImportPreferences):
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
        self.create_strips()
        return {'FINISHED'}

    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}

    def create_strips(self):
        """ Creates strips for imported files """
        frame_current = bpy.context.scene.frame_current
        previous_strip = None
        previous_transform_strip = None

        for file in self.files:
            frame_start = frame_current
            frame_end = frame_current + self.image_strip_frames
            current_strip = self.create_strip(
                path=file['name'],
                frame_start=frame_start,
                frame_end=frame_end,
                channel=1)

            current_transform_strip = self.create_transform_strip(
                frame_start=frame_start,
                frame_end=frame_end)

            current_strip.mute = True

            if self.generate_ken_burns_effect:
                bpy.ops.slideshow_composer.ken_burns_effect('EXEC_DEFAULT')

            if previous_transform_strip is not None:
                self.create_cross(
                    first_strip=previous_transform_strip,
                    second_strip=current_transform_strip)

            frame_current = frame_end + 1 - self.strips_cross_frames
            previous_strip = current_strip
            previous_transform_strip = current_transform_strip

    def create_strip(self, path, frame_start, frame_end, channel):
        file_list = [{'name': path}]

        bpy.ops.sequencer.image_strip_add(
            directory=self.directory,
            files=file_list,
            show_multiview=False,
            frame_start=frame_start,
            frame_end=frame_end,
            channel=channel)

        return bpy.context.selected_sequences[0];

    def create_transform_strip(self, frame_start, frame_end):
        bpy.ops.sequencer.effect_strip_add(frame_start=frame_start, frame_end=frame_end, type='TRANSFORM')
        return bpy.context.selected_sequences[0];

    def create_cross(self, first_strip, second_strip):
        bpy.ops.sequencer.select_all(action="DESELECT")
        first_strip.select = True
        second_strip.select = True

        bpy.ops.sequencer.effect_strip_add(
            frame_start=second_strip.frame_start,
            frame_end=second_strip.frame_start + self.strips_cross_frames,
            type='CROSS'
        )

# if __name__ == "__main__":
#    bpy.utils.register_class(ImportFiles)
