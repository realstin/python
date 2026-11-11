# LIBRARY AND MODULES

A library is a toolbox for developers. It helps you avoid implementing everything yourself from scratch by providing prewritten, reusable code, such as functions, classes, and data structures, that you can use in your project. It can contain many modules.

A module is like a file containing functions that you can import and use in your project. For example, the `math` module provides functions such as `sqrt()` for finding square roots.

If you want to use functions from a module, import it by using `import` followed by the name of the module, such as `math`.
 
### import math     
To use it, you can write `math.sqrt(36)`. This will return 6.

Sometimes module names may look long, so Python provides a simple way to shorten them.

### import math as m 
To use it, you can write `m.sqrt(36)`. The shorthand `m` is called a module alias.

Also, sometimes you may not need to import everything from a module. If you want specific functions, you can do it like this:

### from math import radians, sin, cos
This helps you import only the functions you need. It also helps you use them directly in your code without the `math` prefix or a module alias, but you should use it carefully.
               OR
 ### from module_name import name1 as alias1, name2 as alias2

If you want to import everything so you can use it without a prefix, you can do this:

### from module_name import *  
The asterisk (*) helps you do that, but it is discouraged if you want to build clean, easily readable, and understandable code.
