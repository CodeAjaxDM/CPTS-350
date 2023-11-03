from pyeda.inter import *
from functools import reduce


def init_bdd1():
	""" 
		Creates the initial graph BDD for the project 
	"""
	initialized = False
	for i in range(0, 32):
		for j in range(0, 32):
			if (i + 3) % 32 == j % 32 or (i + 8) % 32 == j % 32:
				if initialized:
					bdd1 = create_bool_formula(i, j) | bdd1
				else: 
					bdd1 = create_bool_formula(i, j)
					initialized = True
	return expr2bdd(bdd1)

def init_prime():
	""" 
		Creates the initial BDD for the prime set
	"""
	prime = [3,5,7,11,13,17,19,23,29,31]
	initialized = False
	for i in range(0, 32):
		if i in prime:
			if initialized:
				bdd_prime = var_expression('x', create_variable(i)) | bdd_prime
			else: 
				bdd_prime = var_expression('x', create_variable(i))
				initialized = True
	return expr2bdd(bdd_prime)

def init_even():
	""" 
		Creates the initial BDD for the even set
	"""
	initialized = False
	for j in range(0, 32):
		if j % 2 == 0:
			if initialized:
				bdd_even = var_expression('y', create_variable(j)) | bdd_even
			else: 
				bdd_even = var_expression('y', create_variable(j)) 
				initialized = True
	return expr2bdd(bdd_even)


def create_bool_formula(i, j):
	""" 
		Creates a boolean formula based on the binary representation
		of the numbers given

		args:
			values i and j to create x and y variables in the boolean formula respectively
	"""
	expression1 = var_expression('x', create_variable(i))
	expression2 = var_expression('y', create_variable(j))
	return expression1 & expression2

def var_expression(variable_name, array):
	"""
		Creates an expression out of a boolean array over the input variable name

		args:
			variable name: the name you wish the variable encoding to be over
			array: the boolean array to encode

	"""
	bdd_vars = bddvars(variable_name, 5)
	bdd_vars = [variable if n else ~variable for variable, n in zip(bdd_vars, array)]
	return reduce(lambda m, n: m & n, bdd_vars)

def create_variable(number):
	"""
		Converts a number into an array of boolean values

		args:
			number: the base 10 number you wish to binary encode into boolean
	"""
	return [(number & 1 << n) for n in range(4, -1, -1)]


def compose(r1, r2):
	"""
		Takes two graphs, and returns the composition of them
	"""
	x = bddvars('x', 5)
	y = bddvars('y', 5)
	z = bddvars('z', 5)
	for i in range(0, 4):
		r1 = r1.compose({x[i]: z[i]})
		r2 = r2.compose({y[i]: z[i]})
	rr = r1 & r2
	return rr.smoothing(z)


def create_Rstar(g):
	"""
		Takes in a graph, and generates the transitive closure of it
	"""
	Rstar = g
	while True:
		h = Rstar
		Rstar = h | compose(g, h)
		if Rstar.equivalent(h):
			return Rstar

def tests(g, prime, even, rr):
	result_string = ""
	if g(27,3) == False:
		result_string += "test 1 failed\n"
	if g(16,20) == True:
		result_string += "test 2 failed\n"
	if even(14) == False:
		result_string += "test 3 failed\n"
	if even(13) == True:
		result_string += "test 4 failed\n"
	if prime(7) == False:
		result_string += "test 5 failed\n"
	if prime(2) == True:
		result_string += "test 6 failed\n"
	if rr(27,6) == False:
		result_string += "test 7 failed\n"
	if rr(27,9) == True:
		result_string += "test 8 failed\n"
	if result_string == "":
		result_string += "all tests passed"


	return result_string
def main():
	g = init_bdd1()
	prime = init_prime()
	even = init_even()
	rr = compose(g,g)
	rrstar = create_Rstar(rr)

	x = bddvars('x', 5)
	y = bddvars('y', 5)

	banana = even or rrstar
	apple = banana.smoothing(y)
	fish = (not prime) or apple
	temp = not fish
	result = not (temp.smoothing(x))

	print(tests(g, prime, even, rr))

if __name__ == "__main__":
	main()