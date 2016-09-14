import sys

class Executor:

	def __init__(self, turtle, stepLength = 100, turnAngle = 90):
		self.turtle = turtle
		self.stepLength = stepLength
		self.turnAngle = turnAngle
		self._is_terminated = False
		
	def execute(self, cmd, params):
		self._last_repeateable_cmd = self.nothing
		try:
			method = getattr(self, cmd)
			self._last_repeateable_cmd = method(params)
		except:
			print("execution error:", sys.exc_info())

	
	def nothing(self, f):
		self.turtle.forward(0)
		return None

	def left(self, f):
		self.turtle.left(self.turnAngle * f)
		return left

	def right(self, f):
		self.turtle.right(self.turnAngle * f)
		return right
		
	def forward(self, f):
		self.turtle.forward(self.stepLength * f)
		return forward

	def circle(self, f):
		self.turtle.circle(self.stepLength * f)
		return None

	def undo(self, f):
		self.turtle.undo()
		return undo
		
	def repeatLast(self, f):
		self._last_repeateable_cmd(1)
		return None
		
	def aBitMore(self, f):
		self._last_repeateable_cmd(0.2)
		return None
		
	def terminate(self, f):
		self._is_terminated = True
		
	def is_terminated(self):
		return self._is_terminated