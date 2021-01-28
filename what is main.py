when we create own custom (personal) module in python then there is use main.py .
Let me explain :

jb hm koi bhi module import krte h python me to by default __init__ .py name ka file bn jata h . 

so there are two scenario:
 1- python file which are well  organised to be imported  as modules . ( in this case __init__.py comes into play ).
 
 2- python file ( single file structure )which can be run directly by command line .  (so for runinng th file in  command line we use main.py).   
 
 Example: we will find the area of a rectangle, square, and circle? 
 so lets suppose you created separate .py files for all (rectangle, circle,square) & store in module src .
 
 so file tree will look like this :
 
 +---src
|   |   circle.py
|   |   rectangle.py
|   |   square.py
|   |   __init__.py
|   |   


so it wont work on command line . so we will store this src file let say folder name areA_finder & add a file main.py  

after that tree would look like this :


  area_finder
|   readme.md
|   __main__.py
|   
+---src
|   |   circle.py
|   |   rectangle.py
|   |   square.py
|   |   __init__.py
|   | 

Content of main.py :

  
print("____-menu_____") 
print("1: to find area of square \n\ 
2: to find area of rectangle\n\ 
3: to find area of circle") 

ch = int(input()) 

if ch == 1: 
	from src.square import square 
	print("enter side") 
	s = int(input()) 
	print ("the area is ", square(s)) 

if ch == 2: 
	from src.rectangle import rectangle 
	print("enter length and breadth") 
	l = int(input()) 
	b = int(input()) 
	print("the area is ", rectangle(l, b)) 

if ch == 3: 
	from src.circle import circle 
	print("enter radius") 
	r = int(input()) 
	print("the area is ", circle(r)) 


now we run on commad prompt / terminal 
$ Pyhton areA_finder

Output: 

____-menu_____ 
1: to find area of square  
2: to find area of rectangle 
3: to find area of circle
1
enter side 
5 
the area is 25


So what happens when we execute the command. Python looks for a file named __main__.py to start its execution automatically. 
If it doesn’t find it it will throw an error . 











