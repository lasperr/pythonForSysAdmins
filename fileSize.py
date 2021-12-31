import os
import sys

script = sys.argv[0]

def print_usage():
	print(f' >> {sys.stderr}, "Usage: python3 {script} DIR"')
	sys.exit(1)
def filesizes(path):
	for dirpath, dirnames, filenames in os.walk(path):
		for filename in filenames:
			filepath = os.path.join(dirpath, filename)
			_bytes = os.path.getsize(filepath)
			print (f'{_bytes}, {filepath}')
def main(argv):
	if not len(argv) == 1:
		print_usage()
	path = argv[0]
	filesizes(path)
if __name__ == '__main__':
	main(sys.argv[1:])