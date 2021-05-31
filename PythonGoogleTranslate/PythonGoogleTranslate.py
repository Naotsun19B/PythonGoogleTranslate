# -*- coding: utf-8 -*-
from googletrans import Translator
import sys
import codecs

args= sys.argv
is_translate_mode = False

print(args)

# t : Translate.
# args = [script filename] [mode specifier] [input-output filename] [source language code] [dest language code].
if args[1] == 't':
	is_translate_mode = True
	if len(args) < 5:
		sys.exit(2)

# d : Detect Language.
# args = [script filename] [mode specifier] [input-output filename].
elif args[1] == 'd':
	is_translate_mode = False
	if len(args) < 3:
		sys.exit(2)

# Not a provided mode specifier.
else:
	sys.exit(1)

with codecs.open(args[2], 'r', 'utf8', 'ignore') as input:
	
	text = input.read()
	input.close()

	with codecs.open(args[2], 'w', 'utf8', 'ignore') as output:

		translator = Translator()

		# Translate.
		if is_translate_mode == True: 
			translated = translator.translate(text, src=args[3], dest=args[4]);
			output.write(translated.text)

		# Detect Language.
		else: 
			detected = translator.detect(text)
			output.write(detected.lang)

		output.close()