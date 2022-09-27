import flet
from flet import Page, TextField, Row, IconButton, icons

def main(page: Page):
	page.title = "Counter App"
	page.vertical_alignment = "center"
	txt_field= TextField(value="0", width=100, height=50, text_align="right")
	
	def minus_clicked(e):
		text_field.value = int(text_field.value) - 1
		
	def plus_clicked(e):
		text_field.value = int(text_field.value) + 1
		
	page.add(
		Row(
			[
				IconButton(icons.REMOVE, on_click=minus_clicked),
                txt_field,
				IconButton(icons.ADD, on_click=PLUS_clicked),
			].
			alignment="center",
		)
	)
	
	flet.app(target.main, view=flet.WEB_BROWSER)
	
    