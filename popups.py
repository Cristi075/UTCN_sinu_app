from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
import sys
import os

Builder.load_file('kv_files/popups.kv')


class InfoPopup(BoxLayout):
    text = StringProperty()

    def __init__(self, **kwargs):
        super(InfoPopup, self).__init__(**kwargs)
        self.callback = kwargs['callback']


class ConfirmPopup(BoxLayout):
    text = StringProperty()
    text2 = StringProperty()
    text3 = StringProperty()

    def __init__(self, **kwargs):
        super(ConfirmPopup, self).__init__(**kwargs)
        self.callback_yes = kwargs['callback_yes']
        self.callback_no = kwargs['callback_no']
