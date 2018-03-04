import bpy
import os.path
from . import preferences
from . import file_utils

class StripsCreator(preferences.StripsCreatorPreferences):
    def create_strips(self, files):
        """ Creates strips for given files """
        frame_current = bpy.context.scene.frame_current
        previous_strip = None
        previous_transform_strip = None

        print("Total files to import: {}".format(len(files)))
        for file in files:
            #temporary
            print("Creating strip for: {}".format(file))
            if not file_utils.is_image(file):
                continue

            frame_start = frame_current
            frame_end = frame_current + self.image_strip_frames
            current_strip = self.create_strip(
                path=file,
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
        if file_utils.is_image(path):
            return self.create_image_strip(path, frame_start, frame_end, channel)
        else:
            return None

    def create_image_strip(self, path, frame_start, frame_end, channel):

        (directory, file) = os.path.split(path)
        file_list = [{'name': file}]

        bpy.ops.sequencer.image_strip_add(
            directory=directory,
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