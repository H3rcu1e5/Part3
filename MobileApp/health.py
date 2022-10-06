import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class health(GridLayout):
	def __init__(self,**kwargs):
	
		super(health, self).__init__()
		self.cols = 2
		
		self.add_widget(Label(text = 'Health Concern Message'))
		self.hm = TextInput()
		self.add_widget(self.hm)
        
        self.submit = Button(text = 'Send')
        self.press.bind(on_press = self.click_me)
        self.add_widget(self.press)
        
        
		
class parentApp(App):
		def build(self):
			return health()
			
if __name__ =="__main__":
	parentApp().run()
	