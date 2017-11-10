from distutils.core import setup
from distutils.core import Extension
from distutils.command.build_ext import build_ext as _build_ext

import sys, shutil

# Tested processor types & boards
supported_processors = ["sun7i", "sun8i"]
supported_boards = ["orangepizero", "orangepipcplus", "micro", "lime2", "lime", "nanopiduo"]

try:
	input = raw_input
except NameError:
	pass


def print_yellow(text):
	"""
	Print text in yellow :)
	:param text: String to be colored
	:return: Colored text
	"""

	return '\033[0;33m' + text + '\033[0m'

def print_red(text):
	"""
	Print text in yellow :)
	:param text: String to be colored
	:return: Colored text
	"""

	return '\033[0;31m' + text + '\033[0m'

def print_warning_processor():
	"""
	Print confirmation dialog
	:return:
	"""
	print (print_yellow("Warning! ") + "Detected and target processor mismatch. ")


	var = input("Do you want to continue [Y/n]? ")
	if var == 'Y' or var == 'y':
		return
	else:
		print ("Abort.")
		sys.exit(1)

def print_warning_board():
	"""
	Print confirmation dialog
	:return:
	"""
	print (print_yellow("Warning! ") + "Detected and target boards mismatch. Pinmapping of " + print_yellow("A20-OLinuXino-MICRO ") + "is used. " + print_red("Pinmapping might be false or not compatible to your borad! ") + "Only recommended for experienced Users!" )


	var = input("Do you want to continue [Y/n]? ")
	if var == 'Y' or var == 'y':
		shutil.copy2('pyA20/gpio/mapping/micro.h', 'pyA20/gpio/mapping.h')
		return
	else:
		print ("Abort.")
		sys.exit(1)

def check_processor():
	"""
	Detect processor type
	:return:
	"""
	cpuinfo = open("/proc/cpuinfo", 'r')
	for line in cpuinfo:
		if "Hardware" in line:
			processor = line.split(": ")[1].rstrip()

			if "sun4i" in processor:
				print ("Detected processor: " + print_yellow(processor) + " (Probably Allwinner A10)")

			elif "sun5i" in processor:
				print ("Detected processor: " + print_yellow(processor) + " (Probably Allwinner A13)")

			elif "sun7i" in processor:
				print ("Detected processor: " + print_yellow(processor) + " (Probably Allwinner A20)")

			elif "sun8i" in processor:
				print ("Detected processor: " + print_yellow(processor) + " (Probably Allwinner H2+/H3)")

			else:
				print ("Detected processor: " + print_yellow("unknown"))


			if processor not in supported_processors:
				print_warning_processor()

			return

	print ("No processor detected")
	print_warning_processor()

def check_board():
	"""
	Detect board type (added by chwe17)
	"""
	boardinfo = open("/etc/armbian-image-release", 'r')
	for line in boardinfo:
		if "BOARD" in line:
			board = line.split("=")[1].rstrip()
			#OrangePi Boards
			if "orangepizero" in board:
				print ("Detected board: OrangePi Zero")
				shutil.copy2('pyA20/gpio/mapping/orangepizero.h', 'pyA20/gpio/mapping.h')

			elif "orangepipcplus" in board:
				print ("Detected board: OrangePi Pc Plus")
				shutil.copy2('pyA20/gpio/mapping/orangepipcplus.h', 'pyA20/gpio/mapping.h')

			#Olimex Boards
			elif "micro" in board:
				print ("Detected board: A20-OLinuXino-MICRO")
				shutil.copy2('pyA20/gpio/mapping/micro.h', 'pyA20/gpio/mapping.h')

			elif "lime2" in board:
				print ("Detected board: A20-OLinuXIno-LIME2")
				shutil.copy2('pyA20/gpio/mapping/lime2.h', 'pyA20/gpio/mapping.h')

			elif "lime" in board:
				print ("Detected board: A20-OLinuXIno-LIME")
				shutil.copy2('pyA20/gpio/mapping/lime.h', 'pyA20/gpio/mapping.h')
			#FriendlyArm Boards
			elif "nanopiduo" in board:
				print ("Detected board: NanoPi Duo")
				shutil.copy2('pyA20/gpio/mapping/nanopiduo.h', 'pyA20/gpio/mapping.h')

			else:
				print ("Unknown board")
				
			if board not in supported_boards:
				print_warning_board()

			return

	print ("Unknown Board")
	print_warning_board()


class build_ext(_build_ext):
	def run(self):
		check_processor()
		check_board()
		_build_ext.run(self)


modules = [
	Extension('pyA20.gpio.gpio', sources=['pyA20/gpio/gpio_lib.c', 'pyA20/gpio/gpio.c']),

	Extension('pyA20.i2c', sources=['pyA20/i2c/i2c_lib.c', 'pyA20/i2c/i2c.c']),

	Extension('pyA20.spi', sources=['pyA20/spi/spi_lib.c', 'pyA20/spi/spi.c']),

	Extension('pyA20.gpio.connector', sources=['pyA20/gpio/connector/connector.c']),

	Extension('pyA20.gpio.port', sources=['pyA20/gpio/port/port.c']),

]

setup(
	name='pyA20',
	version='0.2.1',
	author='Stefan Mavrodiev',
	author_email='support@olimex.com',
	url='https://www.olimex.com/',
	license='MIT',
	packages=['pyA20', 'pyA20.gpio'],
	description='Control GPIO, I2C and SPI',
	long_description=open('README.txt').read() + open('CHANGES.txt').read(),
	classifiers=['Development Status :: 3 - Alpha',
				'Environment :: Console',
				'Intended Audience :: Developers',
				'Intended Audience :: Education',
				'License :: OSI Approved :: MIT License',
				'Operating System :: POSIX :: Linux',
				'Programming Language :: Python',
				'Topic :: Home Automation',
				'Topic :: Software Development :: Embedded Systems'
	],
	ext_modules=modules,
	cmdclass={'build_ext': build_ext}
)
