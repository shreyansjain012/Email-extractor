import re, pyperclip
#TODO: email regex
emailRegex = re.compile(r'''(
	[a-zA-Z0-9._%+-]+	#username
	@			#@ symbol
	[a-zA-Z0-9.-]+		#domain name
	(\.[a-zA-Z]{2,5}) 	#dot something
	)''', re.VERBOSE)

#TODO: find matches in clipboard



#TODO: paste matches in clipboard


