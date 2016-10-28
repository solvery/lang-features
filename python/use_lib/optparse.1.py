#!/usr/bin/env python

from optparse import OptionParser


def main():
	"""The main body of the program."""

	parser = OptionParser()

	parser.add_option('-k', '--ksv', dest='ksv',
		help='use a specific KSV expressed in hexadecimal',
		metavar='KSV', default=None)
	
	parser.add_option('-t', '--test', action='store_true', 
		dest='do_test', default=False, 
		help='generate source and sink keys and test they work')

	(options, args) = parser.parse_args()

	# if asked to do a test, do one and exit
	if options.do_test:
		do_test("")
		return

	# generate a ksv if necessary
	if options.ksv is not None:
		ksv = int(options.ksv, 16)
	else:
		print "no kvs"

def do_test(key_matrix):
	"""Perform a self-test."""

	print('Performing self test.')

# run the 'main' function if this file is being executed directly
if __name__ == '__main__':
	main()
