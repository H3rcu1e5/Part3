import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class login(GridLayout):
	def __init__(self,**kwargs):
	
		super(login, self).__init__()
		self.cols = 2
		
		self.add_widget(Label(text = 'Username'))
		self.u_name = TextInput()
		self.add_widget(self.u_name)
		
		self.add_widget(Label(text = 'Password'))
		self.p_word = TextInput()
		self.add_widget(self.p_word)
        
        self.submit = Button(text = 'Submit')
        self.press.bind(on_press = self.click_me)
        self.add_widget(self.press)
        
        
		
class parentApp(App):
		def build(self):
			return login()
			
if __name__ =="__main__":
	parentApp().run()
	
	