#duck typing
class duck:
	def __init__(self,ide):
		self.ide=ide
		self.ide.execute()
class pycharm:
	def execute(self):
		print("compiling")
class myeditor:
	def execute(self):
		print("spell checking")
ide=myeditor()
ide=pycharm()
obj=duck(ide)