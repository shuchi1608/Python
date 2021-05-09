from kivy.config import Config
Config.set('kivy', 'keyboard_mode', 'systemandmulti')
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class SampleGrid(GridLayout):
    def __int__(self,**kwargs):
        super(SampleGrid, self).__init__()
        self.cols=2 
        self.add_widget(Label(text="Student Name:"))
        self.add_widget(self.s_name)
        self.s_name=TextInput()
      
        self.add_widget(Label(text="Student Marks:"))
        self.add_widget(self.s_marks)
        self.s_marks=TextInput()
        
        self.add_widget(Label(text="Student Gender:"))
        self.add_widget(self.s_gender)
        self.s_gender=TextInput()
        
        self.press=Button(text="Click me ")
        self.press.bind(on_press=self.click_me)
        self.add_widget(self.press)
        
        
    def click_me(self,instance):
        print("Name of Student"+self.s_name.text)
        print("Name of Student"+self.s_marks.text)
        print("Name of Student"+self.s_gender.text)
        
class SampleApp(App):
    def build(self):
        return SampleGrid()
  
    
if __name__=="__main__":
    SampleApp().run()
    
    
    
    
    
    
    
    