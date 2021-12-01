
# Import Module
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window

# Ablak Méretének beállítása
Window.size = (500,500)

# Widget osztály készítése
class MyLayout(Widget):

    # textbox törlése
    def clear(self):
        self.ids.calc_input.text = ""

    # Gombok bemenetének ellenőrzése
    def button_input(self,button):
        # if text input is zero clear the textbox
        if self.ids.calc_input.text=="0":
            self.ids.calc_input.text=""
        self.ids.calc_input.text+=f'{button}'

    # Kimenet: eredmény
    def equal(self):
        try:
            result = eval(self.ids.calc_input.text)
            self.ids.calc_input.text = str(result)
        except :
            self.ids.calc_input.text = "Error"

    # Utolsó szám törlése
    def remove_character(self):
        self.ids.calc_input.text = self.ids.calc_input.text[:-1]

    # Minusz hozzáadása a szám előtt
    def plus_minus(self):
        if len(self.ids.calc_input.text)>0:
            if self.ids.calc_input.text[0]!="-":
                self.ids.calc_input.text = "-"+self.ids.calc_input.text
            else:
                self.ids.calc_input.text = "-"+self.ids.calc_input.text


# Calculator App Object elkészítése
class CalculatorApp(App):

    def build(self):
        return MyLayout()


CalculatorApp().run()