import sys       # Needed for argument parsing
sys.argv = [""]  #
import shlex
import argparse

# TODO: work on this
class LfParser:
    def parse_links(text):
        splitted = shlex.split(text)
        parser = argparse.ArgumentParser()
        parser.add_argument("file")
        parser.add_argument("-I", action="store_true")
        parser.add_argument("-i", action="store_true")
        parser.add_argument("-o", action="store_true")
        parser.add_argument("-O", action="store_true")
        parser.add_argument("-b", type=str)
        parser.add_argument("-e", type=str)
        parser.add_argument("-l", type=str)
        args = parser.parse_args(splitted)
        return args