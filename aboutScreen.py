from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

Builder.load_file('kv_files/aboutScreen.kv')


class AboutScreen(Screen):

    def __init__(self, **kwargs):
        super(AboutScreen, self).__init__(**kwargs)
        self.callback = kwargs['callback']

        self.aboutLines = [] # A list containing the lines that will be displayed here. Just some stupid stuff
        self.aboutLines.append({'text': 'About', 'font_size': 30})
        self.aboutLines.append({'text': '', 'font_size': 20})
        self.aboutLines.append({'text': 'Sinu data extractor', 'font_size': 20})
        self.initialize_items()
        self.append_items()

    def initialize_items(self):
        # Actually putting the stupid stuff in
        self.aboutLines.append({'text': 'V0.2.2 alpha', 'font_size': 15})
        self.aboutLines.append({'text': 'Made by Cristi075', 'font_size': 15})
        self.aboutLines.append({'text': '', 'font_size': 15})
        self.aboutLines.append({'text': 'This code is so bad the Java Garbage Collector should delete it the moment it stops running', 'font_size': 15})

    def append_items(self):
        for line in self.aboutLines:
            self.ids.list.data.append(line)
            #self.ids.list.adapter.data.append(line)

    def back(self):
        self.callback()
