# ofpy
Command line to OmniFocus script, via email or Dropbox and Hazel

## Installation

### Using pip

1. Install as usual from PyPI.
2. Put a file in your `$PATH` with your preferred Python version.
    * I'm using `/usr/local/bin/ofpy` as an example, change `OFPY_DEST` if needed
3. Make it executable.

#### Python3 Example:
```bash
pip3 install ofpy

OFPY_DEST=/usr/local/bin/ofpy
OFPY_PATH=$(python3 -c 'import ofpy; print(str(ofpy.__path__[0]) + "/ofpy.py")')

echo -e '#!/bin/sh'"\n/usr/bin/env python3 $OFPY_PATH"' "$@"' > $OFPY_DEST
chmod u+x $OFPY_DEST
```

#### Python2 Example:
```bash
pip install ofpy

OFPY_DEST=/usr/local/bin/ofpy
OFPY_PATH=$(python -c "import os; import ofpy; print(os.path.join(os.getcwd(), ofpy.__path__[0], 'ofpy.py'))")

echo -e '#!/bin/sh'"\n/usr/bin/env python $OFPY_PATH"' "$@"' > $OFPY_DEST
chmod u+x $OFPY_DEST
```
It should ignore the `python3` shebang in `ofpy.py` if done this way. If not, edit the shebang.

### Manually
Download or `git clone`

```bash
cd ofpy/ofpy
chmod u+x ofpy.py
ln -s $PWD/ofpy.py /usr/local/bin/ofpy
```
Set up to default to Python3 -- edit the shebang in `ofpy.py` if you need Python2.

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

More details at http://n8henrie.com/2014/09/ofpy
