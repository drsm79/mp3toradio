# mp3 to radio
This script takes a set of files and creates a "radio station" for the Music Thing Modular Radio Music eurorack module.

This module has various [requirements][] on the format and on card layout of the files, so a script seemed like a good idea. 

## Install

This project uses [pipenv][]. Go install that then:

```
pipenv install
pipenv shell
```

This script uses [pydub][], you may need to install it's dependencies (ffmpeg).

## Usage

Convert all music (mp3, ogg, wav...) files in a directory with:

```
python convert -d directory
```

multiple directories can be specified, and will be output into a single directory:

```
python convert -d directory1 -d directory2
```

Convert specific files with:

```
python convert -f file1.mp3 -f file2.ogg
```

By default the script creates and fills the `channel` directory in the current working dir. You can override that with:

```
python convert -f file1.mp3 -f file2.ogg -o 16
```

[requirements]: https://github.com/TomWhitwell/RadioMusic/wiki/SD-Card%3A-Format-%26-File-Structure
[pipenv]: https://www.kennethreitz.org/essays/announcing-pipenv
[pydub]: https://github.com/jiaaro/pydub
