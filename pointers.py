#behaves as a pointer would.
class ref:
	def __init__(self, obj):
		self.obj = obj
	def get(self):
		return self.obj
	def set(self, obj):
		self.obj = obj