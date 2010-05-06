import os

# count the number of music files in a directory
def mcount(dir):
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
	
	# these are valid music files
	valid   = ['.mp3', '.wma', '.m4a', '.flac', '.wv']
	
	# these extensions are never music files
	invalid = ['.jpg', '.ini', '.db', '.txt', '.avi', '.nfo', '.txt', '.rtf', '.jpeg', '.ds_store']
	
	if ext in valid:
		return True
		
	# assume that anything else is a music file, probably a bit optimistic
	return (ext not in invalid)
	
# total number of music files
total = 0

# list of directories in which to count music
dirs = open('dirs', 'rb').readlines()

# consider each directory
for dir in dirs:
	dir = dir.strip()
	
	total += mcount(dir)
		
print 'you have', total, 'music files on your computer'