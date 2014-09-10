# ofpy
Command line to OmniFocus script, via email or Dropbox and Hazel

## Installation
download or `git clone`

```bash
cd ofpy
cp .ofpy_config ~/.ofpy_config
cd ofpy
chmod u+x ofpy.py
sudo ln -s $PWD/ofpy.py /usr/local/bin/ofpy
```

Edit `~/.ofpy_config` and fill in your values.

## Usage
Inline from the command line.

`ofpy "This is my first task."`

Inline from the command line without quotes (watch out for apostrophes and quotes)

`ofpy This is my second task.`

Input task in your favorite editor (set in config, defaults to vim).

`ofpy`

More details at http://n8henrie.com/
