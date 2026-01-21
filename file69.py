696969696966969696969696969669

def decor(func):
	def wrapper(*args, **kwargs):
		func()
		print('insie a wrapper')
	return wrapper

def for_decor():
	print('inside a func')

a = for_decor()

decor(a)
