import keyboard
import time
import turtle as t

color = 'red'
x = -280
def go():
    global x, color
    print(x)
    if color == 'green':
        x += 2
    elif color == 'red':
        exit
keyboard.add_hotkey('Space', go)
player = t.Turtle('circle')
player.shapesize(5)
ball = t.Turtle('circle')
ball.up()
ball.shapesize(2)
ball.color('blue')
       
while True:
    start = time.time()
    player.color(color)
    while start + 5 > time.time():
        
        ball.goto(x,-220)
    if color == 'red':
        color = 'green'
    elif color == 'green':
        color = 'red'