# -*- coding: utf-8 -*-
import googletrans
from googletrans import Translator
import sys
import codecs

args = sys.argv

# There are not enough arguments.
if len(args) < 2:
	print("There are not enough arguments.", file=sys.stderr)
	sys.exit(1)

mode = args[1];

# t : Translate.
# args = [script filename] [mode specifier] [input-output filename] [source language code] [dest language code].
if mode == 't':
	if len(args) < 5:
		print("There are not enough arguments.\nargs = [script filename] [mode specifier] [input-output filename] [source language code] [dest language code]", file=sys.stderr)
		sys.exit(3)

# p : Get Pronunciation.
# args = [script filename] [mode specifier] [input-output filename] [language code].
elif mode == 'p':
	if len(args) < 4:
		print("There are not enough arguments.\nargs = [script filename] [mode specifier] [input-output filename] [language code]", file=sys.stderr)
		sys.exit(3)

# d : Detect Language.
# l : Get Language Codes.
# args = [script filename] [mode specifier] [input-output filename].
elif mode == 'd' or mode == 'l':
	if len(args) < 3:
		print("There are not enough arguments.\nargs = [script filename] [mode specifier] [input-output filename]", file=sys.stderr)
		sys.exit(3)

# Not a provided mode specifier.
else:
	print("Not a provided mode specifier.\nFour are supported: t / p / d / l", file=sys.stderr)
	sys.exit(2)

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
			translated = translator.translate(text, src=source, dest=dest)

			if translated.extra_data["possible-translations"] == None:
				print("Translation failed. Please wait for a while and try again.", file=sys.stderr)
				exit(4)
			else:
				output.write(translated.text)

		# Get Pronunciation.
		elif mode == 'p':
			lang = args[3]
			pronunciation = translator.translate(text, src=lang, dest=lang);
			output.write(pronunciation.pronunciation)
				
		# Detect Language.
		elif mode == 'd':
			detected = translator.detect(text)

			if detected.confidence == 0:
				print("Detect language failed. Please wait for a while and try again.", file=sys.stderr)
				exit(4)
			else:
				output.write(detected.lang)

		# Get Language Codes.
		elif mode == 'l':
			for language in googletrans.LANGUAGES:	
				output.write(language)
				output.write(",\n")

		output.close()