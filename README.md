# ofpy
Command line to OmniFocus script, via email or Dropbox and Hazel

## Installation

### Using pip

`sudo pip3 install ofpy`

You may be able to get away without `sudo` if you're using a [Homebrew](http://brew.sh/ "Homebrew — The missing package manager for OS X") Python installation on OSX.

Obviously replace `pip3` with `pip` if you're still using python2 or if python3 is the default on your system (e.g. Arch).

### Manually

You should also be able to just `chmod` and symlink to `ofpy.py` without difficulty -- that's how I as doing it for the first several versions. That said, if you're doing a manual installation, I'll assume you know what you're doing. In general:

1. Download or `git clone`
2. Add a [shebang](http://en.wikipedia.org/wiki/Shebang "Shebang") to `ofpy.py`, e.g. `#! /usr/bin/env python3`
3. Do something along the lines of 

```bash
cd ofpy/ofpy
chmod u+x ofpy.py
ln -s $PWD/ofpy.py /usr/local/bin/ofpy
```

### Configuration

1. Run `ofpy` without arguments. You should see a logging message about creating `~/.ofpy_config`.
2. Edit `~/.ofpy_config` and fill in your values.

## Usage
Inline from the command line.

`ofpy "This is my first task."`

Inline from the command line without quotes (watch out for apostrophes and quotes)

`ofpy This is my second task.`

Compose the task in your favorite CLI editor (set in config, defaults to vim).

`ofpy`

## Troubleshoting

### Installation

Double check permissions, e.g. `ls -l /usr/local/bin/ofpy`.



More details at http://n8henrie.com/2014/09/ofpy
