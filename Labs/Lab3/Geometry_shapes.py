from __future__ import annotations
import math

class Shape:
    """This is a shape class that contains elements and methods that are similar in different
    shape classes"""
    
    def __init__(self, x_pos: float|int, y_pos: float|int) -> list: # Defining the classes attributes
        self.x_pos = x_pos # x and y positions from the center point of a shape.
        self.y_pos = y_pos

    @property # x position
    def x_pos(self) -> float|int: # initializing a getter to which will return a private variable  
        """ x position centre point getter"""
        return self._x_pos

    @x_pos.setter # setter for error handling on x axis position
    def x_pos(self,value: float|int):
        """x position centre point setter"""
        if isinstance(value, str): # makes sure that imputed value is not a string
            raise TypeError(f"x position must be a float value, not {type(value)}") # creating a custom error message
        self._x_pos = value
       
    @property
    def y_pos(self) -> float|int: # repeating the same process for the y center point
        """y position centre point getter"""
        return self._y_pos

    @y_pos.setter # repeating the same process for the y axis
    def y_pos(self,value: float|int):
        """y position centre pont setter"""
        if isinstance(value, str): # makes sure that imputed value is not a string
            raise TypeError(f"y position must be a float value, not {type(value)}")
        self._y_pos = value
    
    
    def __eq__(self, other) -> bool: # boolean as the answer can only be true or false
        """ operator overload to compare if two shape areas are == to each other """
        if type(self) == type(other):
            return self.area == other.area # returns true if is correct
        return False # if the instance is not correct returns false

        
    def __lt__(self, other) -> bool:
        """operator overload to compare if shape area is < to another shape area"""
        if type(self) == type(other):
            return self.area < other.area
        return False

    def __gt__(self, other) -> bool:
        """operator overload to compare if shape area is > to another shape area"""
        if type(self) == type(other):
            return self.area > other.area
        return False
        
    def __le__(self, other) -> bool:
        """operator overload to compare if shape area is <= to another shape """
        if type(self) == type(other):
            return self.area <= other.area
        return False

    def __ge__(self, other) -> bool:
        """operator overload to compare if shape area is >= to another shape"""
        if type(self) == type(other):
            return self.area >= other.area
        return False
    
    
    def translate(self,x_other:int|float, y_other:int|float) -> int|float: 
        """ Moves the x and y position to another point """
        if not isinstance (x_other, (int, float)): # raises a Valueerror if one value is entered as a string
            raise ValueError("translate entries must be a float or a int value")
        if not isinstance (y_other, (int, float)): # raises a Valueerror if one value is entered as a string
            raise ValueError("translate entries must be a float or a int value")
        self.x_pos += x_other  # adds the amount entered to the position to adjust the original position
        self.y_pos += y_other
        

class Circle(Shape):
    """This is a Circle class. It contains functions and methods that are only relevant to a circle"""
    def __init__(self, x_pos:int|float, y_pos:int|float, radius:int|float) -> list:
        super().__init__(x_pos, y_pos,)
        self.radius = radius # radius is relevant to a circle

    def __str__(self) ->str:
        """__str method to produce a user friendly string instead of a class object"""
        return "This is a Circle with position x of " + str(self.x_pos) + ", position y of  " + str(self.y_pos) + ", and a radius of of " + str(self.radius) 
        # overrides so that this string can be viewed when the object is called within the class
    def __repr__(self) -> str:
        """This is a __repr. It will give the developer a visual string instead of a class object when it is called """
        return "Circle (x = " + str(self.x_pos) + ", y =  " + str(self.y_pos) + ", radius = " + str(self.radius) + ")"
        # It does not contain as much information as the __str method as the developer already has a reasonable idea of what the programs code is about
    

    @property # radius is a property for just the circle element. The x and y positions are already provided from the mother class Shape
    def radius(self) -> float|int:
        """getter for radius property"""
        return self._radius

    @radius.setter
    def radius(self,value: float|int) -> float|int:
        """radius setter. This contains custom error messages if the set instances are not met"""
        if isinstance(value, str): # makes sure that imputed value is not a string
            raise TypeError(f"Radius must be a float or int value, not {type(value)}")
        if (value < 0):
            raise ValueError("radius must be a positive number, not a negative") # raises an error if a negative number is entered
        self._radius = value

    @property
    def area(self) -> float:
        """defines area of a circle"""
        return math.pi*(self.radius)**2 # using math.pi along with the equation for an area of a circle

    @property
    def circumference(self) -> float:
        """defines the circumference of a circle"""
        return 2*math.pi*self.radius # using math.pi again to calculate with the equation for finding a circles circumference

    # methods
    @property
    def is_unit_circle(self) -> True:
        """method to check if a circle is a unit circle. (a unit circle has a radius of 1)"""
        if self._radius == 1:
           return "This is a Unit circle" # will return true if radius is == 1. Then it will print the message
        return "This is not a Unit circle"

    def is_inside(self, x_test, y_test,):
        """ method to check when two x and y points are entered, if they are within the circles that has been defined
        - The method here shows that if the points entered are on the boundary of the circle, that means it is not within the circle. """
        distance = math.sqrt((self.x_pos - x_test)**2 + (self.y_pos - y_test)**2) # using the euclidean distance equation.
        if distance < self.radius: # Then if the euclidean distance is less than radius it will return true.
            return True
        return False 



class Rectangle(Shape):
    """This class represents a rectangle shape, it contains functions and methods unique to a rectangle"""
    def __init__(self, x_pos:float|int, y_pos:float|int, height:float|int, length:float|int) -> list:
        super().__init__(x_pos, y_pos)
        self.height = height # rectangle has height and length variables
        self.length = length
 
 
    def __str__(self) -> str:
        """Returns a user friendly version string of rectangle properties instead of a class objects"""
        return "This is a Rectangle with x position of " + str(self.x_pos) + " and y position of  " + str(self.y_pos) + ". It has a height of " + str(self.height) + " and a length of " + str(self.length)
    # overrides so that this string can be viewed when the object is printed within the class
    def __repr__(self) -> str:
        """Returns a string version of the class objects for the developer"""
        return "Rectangle (position x = " + str(self.x_pos) + ", position y = "+ str(self.y_pos) + ", length = "+ str(self.length) + ", height =" + str(self.height) + ")" 
    # overrides so that this string can be viewed when the object is printed called within the class

    @property
    def height(self) -> float|int:
        """height property getter of a rectangle"""
        return self._height # defines height as a private property so it can not be adjusted

    @height.setter
    def height(self,value: float|int):
        """height setter. This raises any errors that could be entered """
        if isinstance(value, str): # makes sure that imputed value is not a string
            raise TypeError(f"height must be a float or int value, not {type(value)}") # making sure that a float or int will be entered
        if (value < 0):
            raise ValueError("height must be a positive number, not a negative") # raises an error if a negative number is entered
        self._height = value

    @property
    def length(self) -> float|int:
        """length property getter"""
        return self._length

    @length.setter
    def length(self,value: float|int):
        """length setter for issuing custom error handling"""
        if isinstance(value, str): # makes sure that imputed value is not a string
            raise TypeError(f"length position must be a float or int value, not {type(value)}")
        if (value < 0):
            raise ValueError("length must be a positive number, not a negative") # raises an error if a negative number is entered
        self._length = value




    @property
    def area(self) -> float:
        """rectangle area property"""
        return self.height * self.length

    @property
    def circumference(self) -> float:
        """rectangle circumference property"""
        return (self.length *2) + (self.height * 2)

    @property
    def is_square(self) -> True:
        """method to check if a rectangle is a square
        - a square has equal sides"""
        if self._length == self._height: # if length and height are the same then it is classed as a square
           return "This is a square"
        
        return "This is not a square"

    def is_inside(self, x_pos, y_pos):
        """method to define if newly entered coordinates are within the defined rectangle"""
        x_min = self.x_pos - (self.length / 2) 
        x_max = self.x_pos + (self.length / 2)
        y_min = self.y_pos - (self.height / 2)
        y_max = self.y_pos + (self.height / 2)
        
        if x_min < x_pos < x_max and y_min < y_pos < y_max:
            return True
        return False           