import os

# count the number of music files in a directory
def mcount(dir):

	# can't walk over it, so we find nothing
	if (not os.path.isdir(dir)):
		return 0
		
	i = 0

	# check each file in dir
	for wd in os.walk(dir):
		for name in wd[2]:
			if (mcount_valid_ext(os.path.splitext(name)[1])):
				i += 1
				
	return i

# is ext a valid extension
def mcount_valid_ext(ext):
	ext = str(ext).lower()
	
	# these are valid file extensions
	valid   = ['.mp3', '.wma', '.m4a', '.flac', '.wv']

	return (ext in valid)
	
# total number of music files
total = 0

# list of directories in which to count music
dirlist = open('dirs', 'rb').readlines()

# consider each directory
for dir in dirlist:
	dir = dir.strip()
	
	total += mcount(dir)
		
print 'you have', total, 'music files on your computer'