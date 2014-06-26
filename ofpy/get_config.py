import configparser
import os.path
import shutil

def main():
    config = configparser.ConfigParser()

    home_dir = os.path.expanduser('~')
    config_file = os.path.join(home_dir, '.ofpy_config')
    if not os.path.exists(config_file):
         try:
            shutil.copy2('../.ofpy_config', config_file)
            print('Config file did not exist, so I copied a template '
                'to ~/.ofpy_config. Please edit with your config.')
        except Exception as e:
            print(e)
            print("It doesn't look like you have a config file, but "
                "I wasn't able to copy the template for you.")

    else:
        config.read(config_file)
        return config
    return False
