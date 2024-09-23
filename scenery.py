"""
This program was designed to fulfill the requirements of Activity 1 of the GCIS 123 class. As instructed the program will prompt the
user for information on how he/she wants to design his/her cake. With the information that the user gave the program will then draw
a table, a cake, a candle and some decorations.
"""
import turtle
import random
t = turtle.Turtle()
"""
The first 4 functions in our program ask for the users input. These functions are very important to the program as the rest of the 
program would not work without the users input. They return the users input to the main function when they are called upon, where 
the input is then tranfered to the parameters of the diffrent function that require the users input
"""
def get_table_specifications():
    t_color=input("Enter color of table: ")
    t_length=int(input("Enter length of table: "))
    t_height=int(input("Enter height of table: "))
    tabletop_thickness=int(input("Enter thickness of table top: "))
    t_width=int(input("Enter width of table top: "))
    leg_thickness=int(input("Enter thickness of legs: "))
    return t_color, t_length, t_height, tabletop_thickness, t_width, leg_thickness

def get_cake_specifications():
    width = int(input("Enter the fixed width for all layers: "))
    layers = []
    """
    To get the necessary information for the 5 required layers we have created a list in which the color and the height of each layer are
    stored.
    """
    for i in range(1, 6):
        height = int(input(f"Enter the height for layer {i}: "))
        color = input(f"Enter the color for layer {i}: ")
        layers.append((height, color))  
    return width, layers


def get_candle_spec():
    c_width = int(input("width of candle: "))
    c_height = int(input("height of candle: "))
    c_color = input("color of the candle: ")
    f_color = input("color of the flame: ")
    f_length = int(input("enter size of flame [max 7]: "))
    return c_height, c_color, c_width, f_color, f_length

def get_ball_specs():
    num_balls = int(input("number of balls [choose more for fun!]"))
    ball_specs = []
    for nb in range(num_balls):
        ball_size = int(input(f"ball size {nb + 1}: "))
        ball_color = input("Pick a color: ")
        ball_specs.append((ball_size, ball_color))
    return ball_specs

"""
This function is defined to draw the legs of the table. With the help of the user information the proportions of the table legs are
determined. When called upon in the main function it will draw 4 legs in 4 diffrent positions. These positons depend on the user input
regarding the proportions of the rest of the table
"""
def legs(color,height,thickness,startpos):
    t.penup()
    t.goto(startpos,0)
    t.right(90)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    t.forward(height)
    t.right(90)
    t.forward(thickness)
    t.right(90)
    t.forward(height)
    t.end_fill()
    t.right(90)
"""
This function defines the proportions of the tabletop and is therefore dependant on some user input. 
"""
def tabletop(color,length,thickness,width):
    t.penup()
    t.goto(0,0)
    t.fillcolor(color)
    t.pencolor(color)
    t.pendown()
    t.begin_fill()
    t.forward(length/2)
    t.left(90)
    t.forward(thickness)
    t.left(90)
    t.forward(length)
    t.left(90)
    t.forward(thickness)
    t.left(90)
    t.forward(length/2)
    t.end_fill()
    t.penup()
    t.left(180)
    t.forward(length/2)
    t.right(90)
    t.forward(thickness)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    t.right(45)
    t.forward(width)
    t.right(45)
    # The value "0.7071067812" = cos (45) and it is necessary to obtain the lenght of the back edge of the table
    t.forward(length-(width*0.7071067812*2))
    t.right(45)
    t.forward(width) 
    t.end_fill()
    t.penup()
    t.right(45)
    t.forward(thickness)
    t.right(90)
    t.forward(length/2)
    t.right(180)

"""
This function defines the shape and size of the candle.
"""
def draw_candle(c_height, c_color, c_width, top_y):
    t.penup()
    t.goto(-c_width / 2, top_y)  
    t.pendown()
    t.color(c_color)
    t.pencolor(c_color)
    t.begin_fill()
    #To not repeat the code here we have used a loop to draw the candle
    for dc in range(2): 
        t.forward(c_width)
        t.left(90) 
        t.forward(c_height)
        t.left(90)
    t.end_fill()
"""
This function, when called in the main function will draw the flame of the candle on top of the rest of the candle.
"""
def flame(c_height,c_width, f_color, f_length, top_y):
    t.penup()
    #This line defines the position in the middle of the top of the candle
    t.goto(0, top_y + c_height)
    t.pendown()
    t.color(f_color)
    t.begin_fill()
    t.circle(f_length)
    t.end_fill()
"""
This function will draw the diffrent layers of the cake each layer's color and width depending on the user input 
"""
def draw_layer(t, x, y, width, height, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(color)
    t.pencolor(color)
    t.begin_fill()
    # We have again decided to use a loop to make the drawing of the layers easier
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()

"""
This function will draw the table according to the user input
"""
def table(t_color, t_length, t_height, tabletop_thickness, t_width, leg_thickness):
    tabletop(t_color,t_length,tabletop_thickness,t_width)
    leg_offset = t_length / 2 - leg_thickness / 2 
    legs(t_color, t_height, leg_thickness, -leg_offset+leg_thickness/2)  
    legs(t_color, t_height, leg_thickness, leg_offset+leg_thickness/2) 
    legs(t_color, t_height * 0.75, leg_thickness, -leg_offset + t_width) 
    legs(t_color, t_height*0.75, leg_thickness, leg_offset - t_width+leg_thickness)

"""
This function will draw some decorative balls on top of the table. As to not hardcode and limit the number of balls on the cake 
we have decided to randomize the position of the balls on the table.
Unfortunatly a result of this decision is that sometimes the balls will overlap with each other or the candle.
"""
def draw_balls(ball_specs, top_y, width):
    for size, color in ball_specs:
        x_b = random.randint(-width // 2, width // 2)
        y_b = top_y
        t.penup()
        t.goto(x_b, y_b)
        t.pendown()
        t.color(color)
        t.pencolor(color)
        t.begin_fill()
        t.circle(size)
        t.end_fill()

def main():
    #These next 4 lines get the user input into the main function so that we can assign them to the parameters of the other functions
    t_color,t_length, t_height, tabletop_thickness, t_width, leg_thickness = get_table_specifications()
    width, layers = get_cake_specifications()
    c_height, c_color, c_width, f_color, f_length = get_candle_spec()
    ball_specs = get_ball_specs()

    #These lines of code define the scene on which the cake is drawn
    t.screen.bgcolor("lightblue")
    t.screen.title("Customizable Cake")
    t.speed(2)

    #We then switch from the input terminal to the screen
    turtle.Screen

    #First we call the table function to draw the table according to the users input
    table(t_color, t_length, t_height, tabletop_thickness, t_width, leg_thickness)
    
    #Then position the t in the middle of the table so that we can start drawing the layers
    x, y = 0 - width/2, 0 + tabletop_thickness
    """
    To draw the layers of the cake we use loop to access the information that is stored in list we defined and after each 
    layer we adjust the y coordinate according to the height of the previous layer so that the t always start from
    the bottom left of each layer
    """
    for i, (height, color) in enumerate(layers):
        draw_layer(t, x, y, width, height, color)
        y += height 
    
    #Next we adjust the position of the t again so that it is on top of the cake, situated in the middle so that we can start drawing the candle
    t.penup()
    top_y = y 
    t.goto(0, top_y)  
    t.setheading(0)
    t.pendown()

    #We then proceed by drawing the candle and the flame according to the user input
    draw_candle(c_height, c_color, c_width, top_y)
    flame(c_height, c_width, f_color, f_length, top_y)

    #Finally we finish by drawing the ball decoration
    draw_balls(ball_specs, top_y,width)

    #And then we return to the starting point
    t.penup()
    t.goto(0,0)
    t.pendown()
    print("Exit by clicking on the icon ")
    t.screen.exitonclick()

main()
