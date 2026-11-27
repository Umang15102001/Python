class color:
     def __init__(self,red,green,blue):
         self.red = red
         self.green = green
         self.blue = blue

     def display(self):
        print("Red: ", self.red,"Green: ", self.green,"Blue: ", self.blue)

def display_color(c):
    print("Red: ", c.red)
    print("Green: ", c.green)
    print("Blue: ", c.blue)


color1 = color(255, 130, 67)
display_color(color1)

color1.display()