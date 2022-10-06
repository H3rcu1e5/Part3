import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class breeds(GridLayout):
	def __init__(self,**kwargs):
	
		super(breeds, self).__init__()
		self.cols = 2
		
		self.add_widget(Label(text = 'Breeds Message'))
		self.br = TextInput()
		self.add_widget(self.br)
        
        self.submit = Button(text = 'Send')
        self.press.bind(on_press = self.click_me)
        self.add_widget(self.press)
        
        
		
class parentApp(App):
		def build(self):
			return breeds()
			
if __name__ =="__main__":
	parentApp().run()
	
	