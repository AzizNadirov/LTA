# Dekoratorlar - 2

from time import time


def timer(limit):
	def inner_timer(func):
		def wraper(*args, **kwargs):
			start_time = time()
			r = func(*args, **kwargs)
			end_time = time()
			diff = end_time - start_time
			if diff > limit:
				raise ValueError("Your function so heavy...")
			else:
				print(f"The Function taken: {diff}s")
				return r
		return wraper
	return inner_timer


@timer(limit=10)
def million(n, m, b, v):
	l = []
	for i in range(10**8):
		if i % n == 0:
			l.append(i)
	return sum(l)



print(million(3, 8, 3,3))






