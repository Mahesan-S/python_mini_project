import turtle
import random as ran

color = ['red', 'blue', 'green', 'yellow', 'orange', 'purple', 'pink', 'brown', 'gray', 'cyan', 'magenta', 'teal', 'navy', 'olive', 'maroon', 'gold', 'silver', 'indigo']
change_ball_color = ran.randint(0,17)
paddle_set = int(-270)
screen_size = int(-225)

score = int(0)
# -------------------------------window screen
win = turtle.Screen()
win.setup(500,600) # 1-> width  2->height
win.bgcolor('black')
win.title('hit game')
win.tracer(0)
# -----------------------------------paddele function
paddle = turtle.Turtle()
paddle.color('white')
paddle.shape('square')
paddle.shapesize(stretch_wid=.5,stretch_len=5)
paddle.penup()
paddle.speed(0)
paddle.goto(0,-260)


# ---------------------------------paddle function key
def paddle_move_left():
    if paddle.xcor()<=-200:
        paddle.setx(paddle.xcor()+20)

    else:   
        paddle.setx(paddle.xcor()-20)


def paddle_move_right():
    if paddle.xcor()>=200:
        paddle.setx(paddle.xcor() - 20)

    else:
        paddle.setx(paddle.xcor() + 20)

# ------------------------------------listen key function
win.listen()
win.onkeypress(paddle_move_left,'Left')
win.onkeypress(paddle_move_right,'Right')

# -----------------------------------ball function
ball = turtle.Turtle()
# ball.circle(10)
ball.shape('circle')
ball.color('pink')
ball.penup()
ball.dx = .09
ball.dy = .09

# -----------------------------------------score function
pen = turtle.Turtle()
pen_color = ['black','white']
pen.color('white')
pen.penup()
pen.goto(0,270)
pen.hideturtle()
pen.write('hit :- 0 ',align="center",font=("Ariel",15,"italic",))

# -----------------------------window update screen
while True:
    win.update()
    # ---------------------------ball movement
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # -----------------------------collaide in wall
    if ball.xcor() > 230:
        # ball.setx(240)
        ball.dx *= -1

        change_ball_color = ran.randint(0, 17)
        ball.color(color[change_ball_color])

    if ball.xcor() < -230:
        # ball.setx(-240)
        ball.dx *= -1

        change_ball_color = ran.randint(0, 17)
        ball.color(color[change_ball_color])

    if ball.ycor() < -300:
        # ball.sety(-280)
        ball.dy *= -1

        change_ball_color = ran.randint(0, 17)
        ball.color(color[change_ball_color])

    if ball.ycor() > 280:
        # ball.setx(280)
        ball.dy *= -1

        change_ball_color = ran.randint(0, 17)
        ball.color(color[change_ball_color])

#     ------------------------------------collie with paddle

    if ball.ycor() < -240 and ball.xcor() < paddle.xcor()+50 and ball.xcor() > paddle.xcor()-50:

        ball.dy *= -1

        change_ball_color = ran.randint(0, 17)
        ball.color(color[change_ball_color])

        pen.clear()
        score += 1
        pen.write('hit :- {}'.format(score), align="center", font=("Ariel", 15, "italic",))

        change_ball_color = ran.randint(0, 17)
        paddle.color(color[change_ball_color])

        # --------------------------------paddle up function
        # paddle_up = paddle_set + 30
        # paddle.sety(paddle_up)

        # --------------------------------ball speed up function

        # ball.dx += .03
        # ball.dy += .03

        # ---------------------------------speed up function of high score

        if score > 10 or score > 20 or score > 25:
            ball.dx += .5
            ball.dy += .5
        #   --------------------------------window screee color function
        # if score%2 == 0:
        #     win.bgcolor('black')
        #     pen.clear()
        #     pen.color(pen_color[1])
        # else:
        #     win.bgcolor('white')
        #     pen.clear()
        #     pen.color(pen_color[0])


    #     -----------------------------------------game over function

    if ball.ycor() < -280:
        ball_spany = ran.randint(100, 150)
        ball_spanx = ran.randint(-180, 180)
        ball.setx(ball_spanx)
        ball.sety(ball_spany)
        ball.color('pink')
        pen.clear()
        pen.write('hit :- 0 ', align="center", font=("Ariel", 15, "italic",))

        # --------------------------------paddle reset function
#         paddle.sety(paddle_set)
#         paddle.color('white')
#
#         # ------------------------------ball reset function
#         ball.dx = .09
#         ball.dy = .09
#
# #         -----------------------------reset bg color
#         win.bgcolor('black')


