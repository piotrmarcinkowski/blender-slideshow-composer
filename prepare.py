import os
import argparse
import os.path
import subprocess
import re


class Operation:
    """ Base class for every operation """

    def get_valid_file_extensions(self):
        return []

    def is_file_valid(self, path):
        supported_extensions = self.get_valid_file_extensions()
        extension = os.path.splitext(path)[1][1:].lower()
        return extension in supported_extensions

    def apply(self, path):
        pass


class StabilizeOperation(Operation):
    """ Performs stabilization of movie files """
    output_file_prefix = 'stabilized'

    def get_valid_file_extensions(self):
        return {'mp4', 'avi', 'mov', 'mkv'}

    def is_file_valid(self, path):
        return Operation.is_file_valid(self, path) and not re.match('.+_{}.+'.format(self.output_file_prefix), path)

    def apply(self, path):
        if self.is_file_valid(path):
            if args.verbose:
                print('Stabilizing file: {}'.format(path))
            (dir, file) = os.path.split(path)
            (root, ext) = os.path.splitext(file)
            output_file = "".join([root, '_', self.output_file_prefix, ext])
            output_path = os.path.join(dir, output_file)
            subprocess.call("ffmpeg -i {} -vf vidstabdetect=stepsize=6:shakiness=8:accuracy=9:result=transform_vectors.trf -f null -".format(path).split(' '))
            subprocess.call("ffmpeg -i {} -vf vidstabtransform=input=transform_vectors.trf:zoom=1:smoothing=30,unsharp=5:5:0.8:3:3:0.4 -vcodec libx264 -preset slow -tune film -crf 18 -acodec copy {}".format(path, output_path).split(' '))
        else:
            if args.verbose:
                print('Skipping file: {}'.format(path))


operations = {'stabilize': StabilizeOperation()}

parser = argparse.ArgumentParser(description='Applies various operations on media files')
parser.add_argument('operation', help='Operation to perform on files', choices=operations.keys())
parser.add_argument('-v', '--verbose', help='Prints more output', action='store_true')
parser.add_argument('--dir', action='store', default='.', help='specifies the input folder (default: current folder)')

args = parser.parse_args()

if args.verbose:
    print('Performing operation:{} on directory:{}'.format(args.operation, args.dir))

# traverse directory and apply chosen operation on files
operation = operations[args.operation]
for root, dirs, files in os.walk(args.dir):
    path = root.split(os.sep)
    for file in files:
        abs_path = os.path.join(root, file)
        operation.apply(abs_path)





