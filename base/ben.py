import flet
from flet import(
	Page,
	TextField,
	FloatingActionButton,
	Column,
	Row,
	Text,
	IconButton,
	OutlinedButton,
	Tabs,
	Tab,
	UserControl,
	Checkbox,
	colors,
	icons,
) 

class Todo(User Control):
        def build(self):
        self.new_task = TextField(hint_text="Add a new task", expand=True)

def main(main: Page):
    page.title="Todo App"
    page.horizontal_alignment = "center"
    
    app = Todo()
    
    page.add(app)
    
flet.app(target=main, view=flet.WEB_BROWSER)
    