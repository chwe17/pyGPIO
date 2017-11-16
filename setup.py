from distutils.core import setup
from distutils.core import Extension
from distutils.command.build_ext import build_ext as _build_ext

import sys, shutil


supported_processors = ["sun7i", "sun8i"]

try:
	input = raw_input
except NameError:
	pass

def print_green(text):
	"""
	Print text in yellow :)
	:param text: String to be colored
	:return: Colored text
	"""

	return '\033[0;32m' + text + '\033[0m'	

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


	var2 = input("Do you want to continue [Y/n]? ")
	if var2 == 'Y' or var2 == 'y':
		return
	else:
		print ("Abort.")
		sys.exit(1)

def print_warning_board():
	"""
	Print confirmation dialog
	:return:
	"""
	print (print_yellow("Warning! ") + "Detected and target boards mismatch.")

	var3 = input("Do you want to use the mapping of a supported boards [Y/n]? ")
	if var3 == 'Y' or var3 == 'y':
		shutil.copy2('pyGPIO/gpio/mapping/micro.h', 'pyGPIO/gpio/mapping.h')
		return
	else:
		print ("Abort.")
		sys.exit(1)

def print_correct():
	"""
	Print confirmation dialog
	:return:
	"""

	var4 = input("Correct? [Y/n] ")
	if var4 == 'Y' or var4 == 'y':
		return
	else:
		manual_board_assignment()

def manual_board_assignment():
	print ("Automatic board detection failed or your board is not supported (yet). \nYou can use a pin mapping from one of our supported boards or abort the \ninstallation. " + print_red("This is only recommended for experienced users! ") + "\nPin mapping might be " + print_red("false") + " and the library " + print_red("does not work") +" as expected!")
	print ("[1]  OrangePi Zero")
	print ("[2]  OrangePi Pc Plus")
	print ("[3]  OrangePi Plus 2E")
	print ("[4]  OrangePi Lite")
	print ("[5]  A20-OLinuXino-MICRO")
	print ("[6]  A20-OLinuXIno-LIME")
	print ("[7]  A20-OLinuXIno-LIME2")
	print ("[8]  NanoPi Duo")
	print ("[9]  NanoPi Neo")
	print ("[10] Abort")
	var5 = input("")
	
	if var5 == '1' or var5 == '[1]':
		shutil.copy2('pyGPIO/gpio/mapping/orangepizero.h', 'pyGPIO/gpio/mapping.h')
		return
		
	elif var5 == '2' or var5 == '[2]':
		shutil.copy2('pyGPIO/gpio/mapping/orangepipcplus.h', 'pyGPIO/gpio/mapping.h')
		return
	elif var5 == '3' or var5 == '[3]':
		shutil.copy2('pyGPIO/gpio/mapping/orangepiplus2e.h', 'pyGPIO/gpio/mapping.h')
		return
		
	elif var5 == '4' or var5 == '[4]':
		shutil.copy2('pyGPIO/gpio/mapping/orangepilite.h', 'pyGPIO/gpio/mapping.h')
		return
		
	elif var5 == '5' or var5 == '[5]':
		shutil.copy2('pyGPIO/gpio/mapping/micro.h', 'pyGPIO/gpio/mapping.h')
		return
		
	elif var5 == '6' or var5 == '[6]':
		shutil.copy2('pyGPIO/gpio/mapping/lime.h', 'pyGPIO/gpio/mapping.h')
		return
		
	elif var5 == '7' or var5 == '[7]':
		shutil.copy2('pyGPIO/gpio/mapping/lime2.h', 'pyGPIO/gpio/mapping.h')
		return
		
	elif var5 == '8' or var5 == '[8]':
		var6 = input("Do you want to use your NanoPi Duo with [1] ore without minishield [2]\n(mapping & naming in connector mode is incorrect, no changes by using port)?)")
		if var6 == '2' or var6 == '[2]':				
			shutil.copy2('pyGPIO/gpio/mapping/nanopiduo.h', 'pyGPIO/gpio/mapping.h')
		elif var6 == '1' or var6 == '[1]':
			shutil.copy2('pyGPIO/gpio/mapping/nanopiduo_minishield.h', 'pyGPIO/gpio/mapping.h')
		else:
			print ("Abort.")
			sys.exit(1)
			
	elif var5 == '9' or var5 == '[9]':
		shutil.copy2('pyGPIO/gpio/mapping/nanopiduo.h', 'pyGPIO/gpio/mapping.h')
		return
		
	elif var5 == '10' or var5 == '[10]':
		print ("Abort.")
		sys.exit(1)
		
	else:
		print ("Abort.")
		sys.exit(1)
		
def print_annotation_olimex():
	print ("Pin naming differs from other boards when using port method!")

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
			if "orangepizero" == board:
				print ("Detected board: " + print_green("OrangePi Zero"))
				print_correct()
				shutil.copy2('pyGPIO/gpio/mapping/orangepizero.h', 'pyGPIO/gpio/mapping.h')

			elif "orangepipcplus" == board:
				print ("Detected board: " + print_green("OrangePi Pc Plus"))
				print_correct()
				shutil.copy2('pyGPIO/gpio/mapping/orangepipcplus.h', 'pyGPIO/gpio/mapping.h')
				
			elif "orangepiplus2e" == board:
				print ("Detected board: " + print_green("OrangePi Plus 2E"))
				print_correct()
				shutil.copy2('pyGPIO/gpio/mapping/orangepiplus2e.h', 'pyGPIO/gpio/mapping.h')
				
			elif "orangepilite" == board:
				print ("Detected board: " + print_green("OrangePi Lite"))
				print_correct()
				shutil.copy2('pyGPIO/gpio/mapping/orangepilite.h', 'pyGPIO/gpio/mapping.h')

			#Olimex Boards
			elif "micro" == board:
				print ("Detected board: " + print_green("A20-OLinuXino-MICRO"))
				print_correct()
				shutil.copy2('pyGPIO/gpio/mapping/micro.h', 'pyGPIO/gpio/mapping.h')
				print_annotation_olimex()
				
			elif "lime" == board:
				print ("Detected board: " + print_green("A20-OLinuXIno-LIME"))
				print_correct()
				shutil.copy2('pyGPIO/gpio/mapping/lime.h', 'pyGPIO/gpio/mapping.h')
				print_annotation_olimex()

			elif "lime2" == board:
				print ("Detected board: " + print_green("A20-OLinuXIno-LIME2"))
				print_correct()
				shutil.copy2('pyGPIO/gpio/mapping/lime2.h', 'pyGPIO/gpio/mapping.h')
				print_annotation_olimex()

			#FriendlyArm Boards
			elif "nanopiduo" == board:
				print ("Detected board: " + print_green("NanoPi Duo"))
				print_correct()
				var6 = input("Do you want to use your NanoPi Duo with [1] ore without minishield [2]\n(mapping & naming in connector mode is incorrect, no changes by using port)?)")
				if var6 == '2' or var6 == '[2]':				
					shutil.copy2('pyGPIO/gpio/mapping/nanopiduo.h', 'pyGPIO/gpio/mapping.h')
				elif var6 == '1' or var6 == '[1]':
					shutil.copy2('pyGPIO/gpio/mapping/nanopiduo_minishield.h', 'pyGPIO/gpio/mapping.h')
				else:
					print ("Abort.")
					sys.exit(1)

			elif "nanopineo" == board:
				print ("Detected board: NanoPi Neo")
				print_correct()
				shutil.copy2('pyGPIO/gpio/mapping/nanopineo.h', 'pyGPIO/gpio/mapping.h')					

			else:
				print ("Unknown board")
				manual_board_assignment()
				

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
