import argparse
import os
import os.path
from pydub import AudioSegment


def parse_args():
    parser = argparse.ArgumentParser(description='Convert computer music to radio music.')
    parser.add_argument('-f', '--file', action='append', default=[], metavar='FILE', help='convert FILE')
    parser.add_argument('-d', '--directory', action='append', default=[], metavar='DIRECTORY', help='convert all computer music in DIRECTORY to radio music')
    parser.add_argument('-o', '--output', metavar='DIRECTORY', help='populate DIRECTORY, default is `channel`', default='channel')
    return parser.parse_args()


def new_name(f, others):
    """
    Files must be '8:3 format: NOISE.RAW, GOAT.RAW, HPSCHD.RAW'. This creates a
    suitable filename and adds it to a dict of files to convert (also used to
    prevent name clashes).
    """
    name = ''.join([ch for ch in os.path.splitext(os.path.basename(f))[0] if ch.isalnum()][:8]).upper()
    c = 1
    while '{}.RAW'.format(name) in others.keys():
        name = '{}{}'.format(name[:-1 * len(str(c))], c)
        c += 1

    others['{}.RAW'.format(name)] = f


def filter_audio(f):
    """
    Return only pydub supported audio
    """
    ext = os.path.splitext(os.path.basename(f))[1][1:]
    if ext in ['mp3', 'wav', 'raw', 'ogg', 'aif']:
        return f

def copy_audio(input_path, output):
    print 'converting {} and saving to {}'.format(input_path, output)
    audio = AudioSegment.from_file(input_path).set_channels(1)
    audio.export(output, format='raw')

def main():
    args = parse_args()
    the_files = args.file
    for d in args.directory:
        the_files.extend([os.path.join(d, x) for x in os.listdir(d)])
    to_convert = {}
    for f in filter(filter_audio, the_files):
        new_name(f, to_convert)

    if len(to_convert) == 0:
        print 'no music files found in {}'.format(the_files)
    else:
        print '{} music files to convert in {}'.format(len(to_convert), the_files)
    for new, old in to_convert.items():
        copy_audio(old, os.path.join(args.output, new))


if __name__ == '__main__':
    main()
