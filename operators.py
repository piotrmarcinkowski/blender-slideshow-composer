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
        description="Number of frames each imported image strip will last",
        default=90,
        min=30)

    strips_cross_frames = bpy.props.IntProperty(
        name="Strips cross effect frames",
        description="Number of frames the cross effect between two strips will last",
        default=10,
        min=5
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

        for file in self.files:
            frame_start = frame_current
            frame_end = frame_current + self.image_strip_frames
            current_strip = self.create_strip(
                path=file['name'],
                frame_start=frame_start,
                frame_end=frame_end,
                channel=1)

            self.create_transform(
                frame_start=frame_start,
                frame_end=frame_end)

            if previous_strip is not None:
                self.create_cross(
                    first_strip=previous_strip,
                    second_strip=current_strip)

            frame_current = frame_end + 1 - self.strips_cross_frames
            previous_strip = current_strip

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

    def create_transform(self, frame_start, frame_end):
        bpy.ops.sequencer.effect_strip_add(frame_start=frame_start, frame_end=frame_end, type='TRANSFORM')

    def create_cross(self, first_strip, second_strip):
        bpy.ops.sequencer.select_all(action="DESELECT")
        first_strip.select = True
        second_strip.select = True
        # The order in which strips are selected determines which direction the cross effect will be applied.
        # There was no way to change the order the strips are stored in bpy.context.selected_sequences (read only?).
        # Instead if their order is incorrect the direction of added effect is controlled by use_reverse_frames property.
        use_reverse_frames = bpy.context.selected_sequences[0].frame_start > bpy.context.selected_sequences[
            1].frame_start;
        bpy.ops.sequencer.effect_strip_add(
            frame_start=second_strip.frame_start,
            frame_end=second_strip.frame_start + self.strips_cross_frames,
            type='CROSS'
        )
        effect_strip = bpy.context.selected_sequences[0];
        effect_strip.use_reverse_frames = use_reverse_frames

# if __name__ == "__main__":
#    bpy.utils.register_class(ImportFiles)
