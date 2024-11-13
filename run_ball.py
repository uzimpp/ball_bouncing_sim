import turtle
import ball
import random

class BouncingSimulator():
	def __init__(self, n_balls):
		turtle.speed(0)
		turtle.tracer(0)
		turtle.hideturtle()
		turtle.colormode(255)
		self.__n_balls = n_balls
		self.__canvas_width = turtle.screensize()[0]
		self.__canvas_height = turtle.screensize()[1]
		self.__ball = []
		self.__size = 0.05 * self.__canvas_width
		for _ in range(n_balls):
			self.__create_new_ball()
			

	def __create_new_ball(self):
		x = random.uniform(-1 * self.__canvas_width + self.__size, self.__canvas_width - self.__size)
		y = random.uniform(-1 * self.__canvas_height + self.__size, self.__canvas_height - self.__size)
		vx = 10 * random.uniform(-1.0, 1.0)
		vy = 10 * random.uniform(-1.0, 1.0)
		# vx = 10 * random.uniform(-0.5, 0.5)
		# vy = 10 * random.uniform(-0.5, 0.5)
		ball_color = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
		self.__ball.append(ball.Ball(ball_color, self.__size, x, y ,vx, vy))
		self.__n_balls += 1

	def __draw_border(self):
		turtle.penup()
		turtle.goto(-self.__canvas_width, -self.__canvas_height)
		turtle.pensize(10)
		turtle.pendown()
		turtle.color((0, 0, 0))
		for i in range(2):
			turtle.forward(2 * self.__canvas_width)
			turtle.left(90)
			turtle.forward(2 * self.__canvas_height)
			turtle.left(90)

	def run(self):
		self.__draw_border()
		while (True):
			turtle.clear()
			self.__draw_border()
			for ball in self.__ball:
				ball.draw_ball()
				ball.move_ball(dt)
				# This commented is for creating new ball every times aa ball bounce
				# Just like a tiktok vids !!! :D
				if ball.update_ball_velocity(self.__canvas_width, self.__canvas_height):
					print("Bounce !!")
					# print(self.__n_balls)
					# self.__create_new_ball()
			turtle.update()

dt = 1 # time step

num_balls = int(input("Number of balls to simulate: "))
simulator = BouncingSimulator(num_balls)
simulator.run()

turtle.done()
