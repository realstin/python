# LIBRARY AND MODULES

a library is a tool box for developers that helps you instead of implementing every thing your self from scratch it comes up with pre-written and reusable codes like functions , classes and data structures you can use in your project it can have many modules 

a module is like a file with those functions so you can import it or bring it to your folder and use it's functions like the module math can provide with you some function like sqrt() to find square roots

if you want to use many functions from a module you import it all by  using <br>import</br> and the name of the module you are importing <br>math</br>
 
### import math     
 to use it you can write like math.sqrt(36)  this will return 6

sometime module names may look big or long so also python provides a simple way to handle it 

### import math as m 
 to use it you can write like m.sqrt(36)   that m you chose to be short hand is called a module alias

 Also some time you may not need to need to import everythig in the module where you want specific  functions you can do it like

 ### from math import radins , sin , cos   
 this helps you  to only import the functions you need  this also helps you to use the functions direct in your code without the prefix math or that alias name of the module but you should use it carefully 
               OR
 ### from module_name import name1 as alias1, name2 as alias2

so if you want to import everything so you can use it without a prefix you can do this

### from module_name import *  
The asterik (*) helps you do that but it is discouraged to build clean , easily readable and understood