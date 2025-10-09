import math

class Circle:
    def __init__(self,radius):
        self.radius=radius
    
    def compute_area(self,radius):
        self.area=math.pi*self.radius**2
        print(f"the area of the circle is {self.area}")
        return self.area
     
    # Dunder method __repr__ pour l'affichage avec print(circle1)
    def __repr__(self):
        return f"Circle(radius={self.radius})"
    
    # Dunder method __call__ pour afficher l’objet en l'appelant comme une fonction
    def __call__(self):
        print(f"Circle with a radius of {self.radius}")

# add two circles together, and return a new circle with the new radius - use a dunder method
    def __add__(self, other):
      return Circle(self.radius+other.radius)

# compare two circles to see which is bigger, and return a Boolean - use a dunder method
    def __gt__(self, other):
        return self.radius > other.radius # return True or False

# compare two circles and see if there are equal, and return a Boolean- use a dunder metho
    def __eq__(self, other):
        return self.radius == other.radius # return True or False


    def __lt__(self, other):
        return self.radius < other.radius    


# tests 
circle1=Circle(3)
# print(circle1) 
circle1() #dunder method call : ok
circle1.compute_area(circle1.radius)
circle2=Circle(4)
newCircle= circle1 + circle2
newCircle()
# print(dir(circle1))
print(newCircle<circle2) # return False
print(circle2>circle1)  #return True


# Tri dans une liste
circles = [newCircle,circle1, circle2]
sorted_circles = sorted(circles)
print(sorted_circles)


