import optparse, os

# count the number of files with a valid_extension in dir (and its subdirectories)
def mcount(dir, valid_extensions):
	i = 0
	
	for wd in os.walk(dir):
		for filename in wd[2]:
			if (os.path.splitext(filename)[1][1:] in valid_extensions):
				i += 1

	return i
		
def main():
	p = optparse.OptionParser(description='Counts the number of music files in a directory',
						      prog = 'mcount',
							  version = 'mcount 0.1')
	p.add_option('-f', help='file containing list of music file extensions (comma seperated list)')
	p.add_option('-e', help='comma seperated list of file extensions', default ='mp3,wma,m4a,flac,wv')
	p.add_option('-q', action='store_true', default = False, help='quiet mode')
	
	options, arguments = p.parse_args()
	
	valid_extensions = []
	
	# get any extensions added from the cmd line
	if (options.e is not None):
		valid_extensions += options.e.split(',')
	
	# get any stored in a defined file
	if (options.f is not None and os.path.exists(options.f)):
		valid_extensions += map(lambda x: x.strip(), open(options.f, 'rb').readlines())
	
	# get rid of dupes
	valid_extensions = list(set(valid_extensions))

	# what directories to search through
	if (len(arguments) == 0):
		dirs = [os.getcwd()]
	else:
		# we take all the directories which actually exist
		dirs = filter(lambda x: os.path.exists(x), arguments)
		
	# count the number of music files
	total = reduce(lambda x, y: x + mcount(y, valid_extensions), dirs, 0)
	
	# not quiet mode
	if (not options.q):
		print p.version, 'by dcchut'
		print 'searched', len(dirs), 'folder(s),', total, 'music files found',
	else:
		print total

if __name__ == '__main__':
	main()