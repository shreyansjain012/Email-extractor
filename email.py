#! /usr/bin/python3
import re, pyperclip

#email regex
emailRegex = re.compile(r'''(
	[a-zA-Z0-9._%+-]+	#username
	@			#@ symbol
	[a-zA-Z0-9.-]+		#domain name
	\.[a-zA-Z]{2,5} 	#dot something
	)''', re.VERBOSE)

#find matches in clipboard
text = str(pyperclip.paste())
matches = []
for email in emailRegex.findall(text):
	matches.append(email)

#paste matches in clipboard
if len(matches) > 0:
	pyperclip.copy('\n'.join(matches))
	print('\n'.join(matches))
else:
	print('No email addresses found')

