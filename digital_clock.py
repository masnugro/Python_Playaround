# This is done in Pythonista3
from scene import *
from datetime import datetime

class Clock (Scene):
	def setup(self):
		r = min(self.size) / 2 * 0.9
		Rect = ui.Path.rounded_rect(0, 0, r*2, r*2, 30)
		Rect.line_width = 6
		shadow = ('black', 0, 0, 15)
		self.face = ShapeNode(Rect, 'white', 'gold', shadow=shadow)
		self.face.position = self.size / 2
		self.add_child(self.face)
		self.time_label = LabelNode('00:00:00', font=('Lato', r*0.3))
		self.date_label = LabelNode('', font=('Helvetica', r*0.12))
		self.date_label.color = ('#aaaaaa')
		self.date_label.position = (self.size.w / 2, self.size.h / 2 - r*0.25)
		self.add_child(self.date_label)
		self.time_label.color = 'black'
		self.face.add_child(self.time_label)
		self.did_change_size()
		
	def did_change_size(self):
		self.face.position = self.size/2
		
	def update(self):
		t = datetime.now()
		self.time_label.text = t.strftime('%H:%M:%S')
		self.date_label.text = t.strftime('%A, %d %B %Y')
		
run(Clock())
