
# Import statements are ignored atm, you must look after them for yourself

from pycow.decorators import Implements, Class
from pycow.utils import Events, Options, Hash

# Use __all__ to hide classes and functions

__all__ = ["Someclass", "a_function"]

# Classes, subclasses and functions

@Class
class Someclass(object):
	"""
	Docstring of class
	"""
	def __init__(self, something): # PyCow removes 'self' from method declarations
		"""
		Docstring of constructor/method
		"""
		self.something = something + "string literal" # PyCow replaces 'self' with 'this'
	
	def a_method(self, otherthing):
		print self.something + otherthing # 'print' is translated to 'alert'
	
	def another_method(self):
		obj = SomeExtension() # PyCow can infer types of callables (even declared later); here it will place 'new', because SomeExtension is a class
		self.member = "test"

@Class
class SomeExtension(Someclass):
	def __init__(self):
		super(SomeExtension, self).__init__("1234") # PyCow correctly treats the 'super' function of Python; here it's the call to the super constructor
	
	def a_method(self, otherthing):
		super(SomeExtension, self).a_method(otherthing) # Here it's a call to the super class' method
		
		# Note: this.parent has been backported to python, so you could use self.parent(otherthing) here, too.
		
		print otherthing, self.something

def a_function(somevalue = "Default"): # Default values
	"""
	Docstring of function
	
	Note that PyCow removes
			whitespaces.
	
	
	
	And normalizes newlines.
	"""
	test = 2 # PyCow automatically declares local variables
	test = 4 # once
	print test+    2 # Because PyCow parses semantics only, it will ignore whitespaces (but avoid to do something like that anyways)

obj = Someclass("a lengthy ")

obj.a_method("test") # PyCow's type inference does not include types of variables (atm)

obj = SomeExtension()

obj.a_method(" sub")

a_function() # PyCow does not put "new" here, because a_function is a simple function

@Implements(Options)
@Class
class ClassWithOptions(object):
	"""
	A class with implements Options using the `Implements` decorator.
	This is MooTools functionality ported to Python.
	"""
	
	# Note: In Python semantics, this declares a class-bound member, but MooTools
	# sees this as object-bound members. The Class decorator will convert all
	# class-bound members to object-bound members on instantiation.
	options = {
		"name": "value",
		"foo": "bar",
	}
	
	def __init__(self, options):
		self.setOptions(options)
		print self.options["foo"], self.options["name"]
	
	# Static methods supported
	@staticmethod
	def somestatic(input):
		print "Static " + input

# Variable scope
global x # Because of the 'global' statement
x = "hello again" # PyCow does not declare x as local here

def another_function():
	global x
	x = "go ahead" # and here
	return x

# Standard statements

if True: # If statement
	print "Welcome"
	if False:
		pass
	else:
		print "Nested if"
else:
	print "You're not welcome..."

i = 0
while i < 3 and not False: # While statement
	print i
	i += 1 # Assignment operator

print "---"

for j in xrange(3): # For statement (xrange)
	print j

print "----"

for i in xrange(1,4): # For statement (xrange; with start)
	print i
	for j in xrange(i,4,2): # For statement (xrange; nested; with start and step)
		print j

print "-----"

for j in xrange(4,1,-1): # For statement (xrange; with start and step backwards)
	print j

i = [1,2,3]
for j in i: # For statement (simple variable)
	print j

for j in ["a","b","c"+"d"]: # For statement (arbitrary expression)
	print j

for key, value in {"a": 1, "b": 2}.iteritems(): # For statement (dictionary)
	print key, value

f = lambda x: x*2 # Lambda functions

a = [1,2,3,f(2)] # List expression

print a[1:3] # Slicing

b = {} # Empty dictionary

# Dictionary with strings and numbers as indices
b = {"a": 1, "b": 2,
	 1: "x", 2: "y",
	 "-test-": 1+2, "0HAY0": "a"+"B"}

# Accessing subscript (simple string)
print b["a"]

# Accessing subscript (other string; assignment)
b["-test-"] = 3

# Accessing subscript (number)
print b[1]

# Deleting from map
del b["a"]

# Modulo operator on strings, i.e. sprintf
print "Demo %d %s %.2f" % (b["-test-"], "abc", 0.123456)

# Operator precedence test
print (1 > 2) and ((2 * 3) > 8) # removes all parentheses
print 1 * (2 + 4) * -(1 + 2) # keeps all parentheses
print (True and True) and False or False

# isinstance
print isinstance([], list)
print isinstance(Hash(), Hash)
