/* This file was generated with PyCow - the Python to JavaScript translator */

/* from pycow.decorators import Implements, Class */;

/* from pycow.utils import Events, Options, Hash */;

/**
 * Docstring of class
 */
var Someclass = new Class({

	/**
	 * Docstring of constructor/method
	 */
	initialize: function (something) {
		this.something = something + "string literal";
	},

	a_method: function (otherthing) {
		dbgprint(this.something + otherthing);
	},

	another_method: function () {
		var obj = new SomeExtension();
		this.member = "test";
	}
});

var SomeExtension = new Class({
	Extends: Someclass,

	initialize: function () {
		this.parent("1234");
	},

	a_method: function (otherthing) {
		this.parent(otherthing);
		dbgprint(otherthing, this.something);
	}
});

/**
 * Docstring of function
 *
 * Note that PyCow removes
 * whitespaces.
 *
 * And normalizes newlines.
 */
var a_function = function (somevalue) {
	if (!$defined(somevalue)) somevalue = "Default";
	var test = 2;
	test = 4;
	dbgprint(test + 2);
};

var obj = new Someclass("a lengthy ");

/* Warning: Cannot infer type of -> */ obj.a_method("test");

obj = new SomeExtension();

/* Warning: Cannot infer type of -> */ obj.a_method(" sub");

a_function();

/**
 * A class with implements Options using the `Implements` decorator.
 * This is MooTools functionality ported to Python.
 */
var ClassWithOptions = new Class({
	Implements: Options,
	options: {
		name: "value",
		foo: "bar"
	},

	initialize: function (options) {
		/* Warning: Cannot infer type of -> */ this.setOptions(options);
		dbgprint(this.options.foo, this.options.name);
	}
});
ClassWithOptions.somestatic = function (input) {
	dbgprint("Static " + input);
};


x = "hello again";

var another_function = function () {
	x = "go ahead";
	return x;
};

if (true) {
	dbgprint("Welcome");
	if (false)
		/* pass */;
	else
		dbgprint("Nested if");
}
else
	dbgprint("You're not welcome...");

var i = 0;

while (i < 3 && !false) {
	dbgprint(i);
	i++;
}

dbgprint("---");

for (var __iter0_ = new XRange(3); __iter0_.hasNext();) {
	var j = __iter0_.next();
	dbgprint(j);
}
delete __iter0_;

dbgprint("----");

for (var __iter0_ = new XRange(1, 4); __iter0_.hasNext();) {
	i = __iter0_.next();
	dbgprint(i);
	for (var __iter1_ = new XRange(i, 4, 2); __iter1_.hasNext();) {
		j = __iter1_.next();
		dbgprint(j);
	}
	delete __iter1_;
}
delete __iter0_;

dbgprint("-----");

for (var __iter0_ = new XRange(4, 1, -1); __iter0_.hasNext();) {
	j = __iter0_.next();
	dbgprint(j);
}
delete __iter0_;

i = [1, 2, 3];

for (var __iter0_ = new _Iterator(i); __iter0_.hasNext();) {
	j = __iter0_.next();
	dbgprint(j);
}
delete __iter0_;

for (var __iter0_ = new _Iterator(["a", "b", "c" + "d"]); __iter0_.hasNext();) {
	j = __iter0_.next();
	dbgprint(j);
}
delete __iter0_;

for (var __iter0_ = new _Iterator({
			a: 1,
			b: 2
		}); __iter0_.hasNext();) {
	var value = __iter0_.next();
	var key = __iter0_.key();
	dbgprint(key, value);
}
delete __iter0_;

var f = function (x) {return x * 2;};

var a = [1, 2, 3, /* Warning: Cannot infer type of -> */ f(2)];

dbgprint(a.slice(1, 3));

var b = {};

b = {
	a: 1,
	b: 2,
	1: "x",
	2: "y",
	"-test-": 1 + 2,
	"0HAY0": "a" + "B"
};

dbgprint(b.a);

b["-test-"] = 3;

dbgprint(b[1]);

delete b.a;

dbgprint("Demo %d %s %.2f".sprintf(b["-test-"], "abc", 0.123456));

dbgprint(1 > 2 && 2 * 3 > 8);

dbgprint(1 * (2 + 4) * -(1 + 2));

dbgprint((true && true) && false || false);

dbgprint([] instanceof Array);

dbgprint(new Hash() instanceof Hash);

