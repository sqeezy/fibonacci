import sys
import time
from fibonacci import *

def test(i):
	start = time.time()
	print fibonacci(i)
	end = time.time()
	print i
	print end-start

if __name__ == '__main__':
	test(int(sys.argv[1]))
