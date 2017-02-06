#! /usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import subprocess
import sys

parser = argparse.ArgumentParser(description='svg2png.py - Converts a SVG file to a PNG file using Inkscape.')
parser.add_argument('-i', '--input', dest='input', type=str, help="SVG input file")
parser.add_argument('-o', '--output', dest='output', type=str, nargs='?', help="PNG output file", default=None)

if len(sys.argv) > 1:
    args = parser.parse_args()


    output = args.output or args.input + '.png'
    inkscape_cmd = '/usr/bin/inkscape -z -f {in_file} -e "{out_file}"'

    cmd = inkscape_cmd.format(in_file=args.input, out_file=output)
    code = subprocess.call(cmd, shell=True)

    if code > 0:
        print("error in executing the command:")
        print(cmd)
else:
    parser.print_help()