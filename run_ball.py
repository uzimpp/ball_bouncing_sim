import turtle
import ball
import random

num_balls = int(input("Number of balls to simulate: "))
turtle.speed(0)
turtle.tracer(0)
turtle.hideturtle()
canvas_width = turtle.screensize()[0]
canvas_height = turtle.screensize()[1]
print(canvas_width, canvas_height)
ball_radius = 0.05 * canvas_width
turtle.colormode(255)
color_list = []
xpos = []
ypos = []
vx = []
vy = []
ball_color = []

# create random number of balls, num_balls, located at random positions within the canvas; each ball has a random velocity value in the x and y direction and is painted with a random color
for i in range(num_balls):
    xpos.append(random.randint(-1*canvas_width + ball_radius, canvas_width - ball_radius))
    ypos.append(random.randint(-1*canvas_height + ball_radius, canvas_height - ball_radius))
    vx.append(2*random.uniform(-1, 1))
    vy.append(2*random.uniform(-1, 1))
    ball_color.append((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

dt = 1 # time step
while (True):
    turtle.clear()
    for i in range(num_balls):
        ball.draw_ball(ball_color[i], ball_radius, xpos[i], ypos[i])
        ball.move_ball(i, xpos, ypos, vx, vy, dt)
        ball.update_ball_velocity(i, xpos, ypos, vx, vy, dt, canvas_width, canvas_height, ball_radius)
    turtle.update()

# hold the window; close it by clicking the window close 'x' mark
turtle.done()
