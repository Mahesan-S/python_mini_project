import turtle
import random
if __name__ == '__main__':
    print(' ')

# color = ['red','blue','green','orange']
color = ['red', 'blue', 'green', 'yellow', 'orange', 'purple', 'pink', 'brown', 'black', 'white', 'gray', 'cyan', 'magenta', 'teal', 'navy', 'olive', 'maroon', 'gold', 'silver', 'indigo']


input_range = int(input('give the range '))
bg_color = ['black','white']
res = int(input('balck (0) white (1)'))
val = bg_color[res]


# ----------------------------screen function
win = turtle.Screen()
win.setup(500,500)
win.title('random')
# win.tracer(0)
win.bgcolor(val)

# -----------------------------------------give the shape,function
square = turtle.Turtle()
square.pendown()
square.goto(-50,0)
square.speed(8)

# square.circle(50)
# square.hideturtle()

for i in range(input_range):
    res = random.randint(0, 19)
    new = color[res]
    square.color(new)

    square.forward(100+10)

    res = random.randint(0, 19)
    new = color[res]
    square.color(new)

    square.right(80+50)

    res = random.randint(0,19)
    new = color[res]
    square.color(new)



    square.fillcolor("light green")
    square.begin_fill()

    square.circle(70)


# ----------------------------------------------update the screen
while True:
    win.update()
    # turtle.done()

