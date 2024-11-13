import turtle

class Ball():
	def __init__(self, ball_color, ball_size, xpos, ypos, vx, vy):
		self.__color = ball_color
		self.__size = ball_size
		self.__x = xpos
		self.__y = ypos
		self.__vx = vx
		self.__vy = vy

	@property
	def color(self):
		return self.__color

	@color.setter
	def color(self, color):
		self.__color = color

	@property
	def size(self):
		return self.__size

	@size.setter
	def size(self, size):
		self.__size = size

	@property
	def x(self):
		return self.__x

	@x.setter
	def x(self, x):
		self.__x = x

	@property
	def y(self):
		return self.__y

	@y.setter
	def y(self, y):
		self.__y = y

	def draw_ball(self):
		turtle.penup()
		turtle.color(self.__color)
		turtle.fillcolor(self.__color)
		turtle.goto(self.__x,self.__y - self.__size)
		turtle.pendown()
		turtle.begin_fill()
		turtle.circle(self.__size)
		turtle.end_fill()
	
	def move_ball(self, dt):
		self.__x += self.__vx*dt
		self.__y += self.__vy*dt
	
	def update_ball_velocity(self, canvas_width, canvas_height):
		if abs(self.__x) > (canvas_width - self.__size):
			self.__vx = -self.__vx
			return 1

		if abs(self.__y) > (canvas_height - self.__size):
			self.__vy = -self.__vy
			return 1





