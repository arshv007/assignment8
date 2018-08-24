#Ques1
class circle:
    def __init__ (self,r):
        self.radius=r
    def getArea(self):
        self.area=3.14*self.radius*self.radius
        return self.area
    def getCircumference(self):
        self.c=2*3.14*self.radius
        return self.c
r=int(input("Enter radius "))
c1=circle(r)
print("Area:",c1.getArea())
print("Circumference:", c1.getCircumference())

#Ques2
class student:
    def __init__(self,x,y):
        self.name=x
        self.rollno=y
    def setAge(self,z):
        self.age=z
    def setMarks(self,v):
        self.marks=v
    def display(self):
        print("Name:",self.name)
        print("Roll No.:",self.rollno)
        print("Age:",self.age)
        print("Marks:",self.marks)
x=input("Enter name: ")
y=int(input("Enter rollno: "))
z=int(input("Enter age"))
v=int(input("Enter marks:"))
s1=student(x,y)
s1.setAge(z)
s1.setMarks(v)
s1.display() 

#Ques3
class Temperature:
    def convertFahrenheit(self,c):
        f=((c*9)/5)+32
        return f
    def convertCelsius(self,f):
        c=(f-32)/1.8
        return c
t=Temperature()
t1=int(input("Enter temperature in Celcius :"))
t2=int(input("Enter temperature in Fahrenheit:"))
print(t1,"in Fahrenheit is",t.convertFahrenheit(t1),"and",t2,"in Celclius is",t.convertCelsius(t2))


#Ques4
class MovieDetails:
    def add(self,name,year,rating):
        self.artistname=name
        self.yearofrelease=year
        self.rating=rating
    def display(self):
        print("Artist Name: ",self.artistname,"\nYear of release:",self.yearofrelease,"\nRating:",self.rating)
    
m=MovieDetails()
name=input("Enter name of artist: ")
year=int(input("Enter year of release :"))
rating=int(input("Enter rating: "))
m.add(name,year,rating)
m.display()

#Ques5
class Animal:
    def animal_attribute(self):
        print("Attribute is: Tiger")
class Tiger(Animal):
    def tiger_attr(self):
        print(" ")
a=Animal()
t=Tiger()
t.animal_attribute() 

#Ques6
'''
The output will be

A B
A B

'''

#Ques7
class shape:
    def __init__(self,l,b):
        self.length=l
        self.breadth=b
    def area(self):
        self.area=self.length*self.breadth
        return self.area
class rect(shape):
    def __init__(self,l,b):
        self.length=l
        self.breadth=b
class square(shape):
    def __init__(self,s):
        self.length=s
        self.breadth=s
r=rect(20,4)
s=square(8)
print("Area of rectangle:",r.area(),"and area of square:",s.area())
