#!/usr/bin/env python

import sys
import os.path
from pycow import translate_file

if len(sys.argv) < 2:
	print "=> PyCow - Python to JavaScript with MooTools converter <="
	print "Usage: %s [OPTION]... filename.py" % (os.path.basename(sys.argv[0]))
	print "Options:"
	print " -o filename   Set the output file name (default: filename.py.js)"
	print " -n namespace  Enclose module in namespace"
	print " -W            Omit warning comments in output"
	sys.exit()

in_filename = ""
out_filename = ""
namespace = ""
warnings = True

i = 1
while i < len(sys.argv):
	arg = sys.argv[i]
	if arg == "-o":
		if i+1 >= len(sys.argv):
			print "Error parsing command line: Missing parameter for option '-o'."
			sys.exit(1)
		out_filename = sys.argv[i+1]
		i += 1
	elif arg == "-n":
		if i+1 >= len(sys.argv):
			print "Error parsing command line: Missing parameter for option '-n'."
			sys.exit(1)
		namespace = sys.argv[i+1]
		i += 1
	elif arg == "-W":
		warnings = False
	else:
		in_filename = arg
	i += 1

if in_filename == "":
	print "Error parsing command line: Missing input file."
	sys.exit(1)

translate_file(in_filename, out_filename, namespace=namespace, warnings=warnings)
