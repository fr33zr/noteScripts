import time

escapes = [
	''' \\\ - BackSlash (\\) ''',
	''' \\' - Single-Quote (\') ''',
	''' \\" - Double-Quote (") ''',
	''' \\a - ASCII Bell (BEL) ''',
	''' \\b - ASCII Backspace (BS) ''',
	''' \\f - ASCII Formfeed (FF)''',
	''' \\n - ASCII Linefeed (LF)''',
	''' \\N{name} - Character named name in the Unicode database (Unicode Only)''',
	''' \\r - ASCII Carriage return (CR)''',
	''' \\t - ASCII Horizontal tab (TAB)''',
	''' \\uxxxx - Character with 16-Bit hex-value xxxx (Unicode Only)''',
	''' \\Uxxxxxxxx - Character with 32-Bit hex-value (Unicode Only)''',
	''' \\v - ASCII vertival tab (VT)''',
	''' \\ooo - Character with octal value oo''',
	''' \\xhh - Character with hex value hh''',
]
for escape in escapes:
	print ('\t* ' + escape)
	time.sleep(.5)
