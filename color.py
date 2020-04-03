import colorama
# Created By Dinar Hamid
# If using Windows, init() will cause anything sent to stdout or stderr
# will have ANSI color codes converted to the Windows versions. Hooray!
# If you are already using an ANSI compliant shell, it won't do anything
# Now regular ANSI codes should work, even in Windows
# Great Thank To https://www.devdungeon.com/content/colorize-terminal-output-python

class ColoR(object):
	def __init__(self):
		colorama.init()
		self.CLEAR_SCREEN = '\033[2J'
		self.RESET = '\033[0m'		# mode 0  = reset
		self.RED = '\033[31m'		# mode 31 = red forground
		self.GREEN = '\033[32m'		# mode 32 = green forground
		self.YELLOW = '\033[33m'	# mode 33 = yellow forground
		self.BLUE = '\033[34m'		# mode 34 = blue forground
		self.MAGENTA = '\033[35m'	# mode 35 = Magenta forground
		self.CYAN = '\033[36m'		# mode 36 = Cyan forground
		self.WHITE = '\033[37m'		# mode 37 = white forground
		# this more color B = bright.
		self.BBlack = '\033[90m'	# mode 90 = Bright Black forground
		self.BRed = '\033[91m'		# mode 91 = Bright Red forground
		self.BGreen = '\033[92m'	# mode 92 = Bright Green forground
		self.BYelow = '\033[93m'	# mode 93 = bright yellow forground
		self.BBlue = '\033[94m'		# mode 94 = bright Blue forground
		self.BMgnt = '\033[95m'		# mode 95 = bright Magenta forground
		self.Bcyan = '\033[96m'		# mode 96 = bright Cyan forground
		self.Bwhite = '\033[97m'	# mode 97 = bright white forground
