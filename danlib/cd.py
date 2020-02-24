from os.path import expanduser, abspath
from os import chdir, getcwd

class OnDir:
    """
    Context manager for pushing a change in the working directory and going back when done.
    """

    def __init__(self, new_path):
        self.new_path = abspath(expanduser(new_path))

    def __enter__(self):
        self.saved_path = getcwd()
        chdir(self.new_path)

    def __exit__(self, etype, value, traceback):
        chdir(self.save_path)
