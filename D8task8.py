
class circle():
    def __init__(self,l1,pii):
        # list of number is a radius
        self.l1=l1
        self.pii= pii
    
    def area(self):
        #area of circle =  π r²	// here pi == 3.141 and the
        #the list of numbers as a radius 
        print(f"\nArea of a circle is: {self.pii*self.l1**2}")

    def perimeter(self):
        # perimeter of a circle =2πr 
        print(f"perimeter of circle is: {2*self.pii*self.l1}" )


list1 =[23,52,43,21,34]
for i in list1:
    val = circle(i,3.141)
    val.area() 
    val.perimeter()  