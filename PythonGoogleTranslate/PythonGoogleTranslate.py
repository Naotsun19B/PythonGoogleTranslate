# -*- coding: utf-8 -*-
import googletrans
from googletrans import Translator
import sys
import codecs

args = sys.argv

if len(args) < 2:
	sys.exit(1)

mode = args[1];

# t : Translate.
# args = [script filename] [mode specifier] [input-output filename] [source language code] [dest language code].
if mode == 't':
	if len(args) < 5:
		sys.exit(2)

# d : Detect Language.
# l : Get Language Codes.
# args = [script filename] [mode specifier] [input-output filename].
elif mode == 'd' or mode == 'l':
	if len(args) < 3:
		sys.exit(2)

# Not a provided mode specifier.
else:
	sys.exit(1)

filename = args[2]
with codecs.open(filename, 'r', 'utf8', 'ignore') as input:
	
	text = input.read()
	input.close()

	with codecs.open(filename, 'w', 'utf8', 'ignore') as output:

		translator = Translator()

		# Translate.
		if mode == 't': 
			source = args[3]
			dest = args[4]
			translated = translator.translate(text, src=source, dest=dest);
			output.write(translated.text)

		# Detect Language.
		elif mode == 'd':
			detected = translator.detect(text)
			output.write(detected.lang)

		# Get Language Codes.
		elif mode == 'l':
			for language in googletrans.LANGUAGES:	
				output.write(language)
				output.write(",\n")

		output.close()