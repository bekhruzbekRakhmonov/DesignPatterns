import functools

def memoize(fn):
	known = {}

	@functools.wraps(fn)
	def memoizer(*args):
		if args not in known:
			known[args] = fn(args[0])
		return known[args]

	return memoizer


# @memoize
def fibonacci(n):
    '''Returns the nth number of the Fibonacci sequence'''
    assert(n >= 0), 'n must be >= 0'
    return n if n in (0, 1) else fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(100))