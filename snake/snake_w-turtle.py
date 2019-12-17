# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 19:51:01 2019

@author: Rowland Zhang
"""

# imports
import turtle
import time
import math
import random

class Coordinate:
    def __init__(self, x, y): # two dashes
        self.x = x
        self.y = y
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def setCor(self, x, y):
        self.x = x
        self.y = y

# window setup
def window_setup():
    w = turtle.Screen()
    w.title("Classic Snake")
    w.bgcolor("skyBlue")
    w.setup(width=screen_width, height=screen_height)
    w.tracer(0) # turns off screen update
    return w

# snake head
def make_snake_head(): 
    h = turtle.Turtle()
    h.shape("square")
    h.speed(0) #animation speed? fastest
    h.color("black")
    h.penup() #imagin lifting pen up, not tracing a line
    h.goto(0, 0)
    h.direction = "stop"
    return h

# food
def make_snake_food():
    f = turtle.Turtle()
    f.shape("circle")
    f.speed(0)
    f.color("Honeydew")
    f.penup()
    # position foor with random_food later
    return f

# global var
screen_width = 600
screen_height = 600
tick_time = 0.1
step_size = 5
last_loc = Coordinate(0, 0)
food_eaten = 0

window = window_setup()
food = make_snake_food()
head = make_snake_head()

def go_up():
    head.direction = "up"
def go_down():
    head.direction = "down"
def go_left():
    head.direction = "left"
def go_right():
    head.direction = "right"

def move():
    # update last tick location
    last_loc.setCor(head.xcor(), head.ycor())
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + step_size)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - step_size)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - step_size)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + step_size)

def bounds_check():
    x = head.xcor()
    y = head.ycor()
    # print(str(window.screensize()[0]) + ", " + str(window.screensize()[1]))
    if (-screen_width/2 < x < screen_width/2) and (-screen_height/2 < y < screen_height/2):
        # print("still on screen")
        return True
    print("%d - %d" % (last_loc.getX(), last_loc.getY()))
    head.goto(last_loc.getX(), last_loc.getY())
    print("ouh, my head")
    head.direction = "stop"
    
    if head.direction == "up":
        pass
    if head.direction == "down":
        pass
    if head.direction == "left":
        pass
    if head.direction == "right":
        pass

mouth_range = 5
# check if the snake head is onto of food    
def food_check():
    head_x = head.xcor()
    head_y = head.ycor()
    food_x = food.xcor()
    food_y = food.ycor()
    delt_x = head_x - food_x
    delt_y = head_y - food_y
    distance = math.sqrt(delt_x**2 + delt_y**2)
    if distance < mouth_range:
        global food_eaten
        food_eaten = food_eaten + 1
        print("Yum! Score = %d" % food_eaten)
        # pseudo generate new food
        random_food()
    
def random_food():
    x = random.randint(-screen_width/2, screen_width/2)    
    y = random.randint(-screen_height/2, screen_height/2)
    position_food(x, y)
    
# we will be using the same food object, moving it to new locations to simulate new food
def position_food(x, y):
    food.goto(int(x), int(y))
    
game_puased = False
# pause the game
def puase():
    head.
    head.direction = "stop"
    pass

# resume from pause, if called without puase then does nothing
def resume():
    if not game_puased:
        return
    

# key binding
def key_bind():
    window.listen()
    window.onkeypress(go_up, "w") # note: onkeypress seems to not allow a method with parameters
    window.onkeypress(go_left, "a")
    window.onkeypress(go_down, "s")
    window.onkeypress(go_right, "d")
    
    window.onkeypress(pause, "p")
    window.onkeypress(resume, "r")

def main():
    # global variable initializing methods call on variable declaration
    #window_setup()
    #make_snake_head()
    
    key_bind()
    random_food() # initialize a food location
    
    # main game loop
    while True:
        window.update()
        move()
        food_check()
        bounds_check()
        time.sleep(tick_time)
    
    window.mainloop() # is essentially replaced by the infinite update loop

# calling main function
main()
