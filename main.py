import sys
import os

from kivy.lang import Builder
from kivy.app import App
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.graphics import Line
from kivy.gesture import GestureDatabase
from kivy.core.window import Window
from kivy.storage.jsonstore import JsonStore

from my_gestures import simplegesture, circle

# The logic of the program
from popups import InfoPopup, ConfirmPopup
from sinu_requests import *
from sinu_parser import *

# noinspection PyUnresolvedReferences
from specSelect import SelectableRecycleBoxLayout, SelectableLabel
from aboutScreen import AboutScreen

# Hack that allows accessing the assets after they're packed into an exe
if getattr(sys, 'frozen', False):
    # noinspection PyProtectedMember
    os.chdir(sys._MEIPASS)

Builder.load_file('kv_files/login.kv')  # load data for login screen
Builder.load_file('kv_files/tableView.kv')  # load data for table viewing screen

Window.softinput_mode = 'pan'

storagePath = 'storedData.json'


class LoginScreen(Screen):

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.gdb = GestureDatabase()

        # add pre-recorded gesture to database
        self.gdb.add_gesture(circle)
        self.sid = 0
        self.popup_info = None
        self.popup_conf = None

    def on_touch_down(self, touch):
        # start collecting points in touch.ud
        # create a line to display the points
        userdata = touch.ud
        userdata['line'] = Line(points=(touch.x, touch.y))
        return super(LoginScreen, self).on_touch_down(touch)

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]
        return super(LoginScreen, self).on_touch_move(touch)

    def on_touch_up(self, touch):
        # touch is over, display informations, and check if it matches known gestures
        g = simplegesture('', list(zip(touch.ud['line'].points[::2], touch.ud['line'].points[1::2])))

        # print match scores between all known gestures
        print("circle:", g.get_score(circle))

        # use database to find the more alike gesture, if any
        g2 = self.gdb.find(g, minscore=0.70)

        print(g2)
        if g2:
            if g2[1] == circle:
                print("circle detected")
                self.manager.current = 'about'

    def on_click(self):
        username = self.ids.username.text
        password = self.ids.password.text
        self.login(username, password)

    def login(self, username, password):
        self.sid = get_sid(username, password)

        if self.sid == 0:  # Login Failed
            content = InfoPopup(callback=self.dismiss_popup)
            content.text = 'Invalid username or password'
            self.popup_info = Popup(title='Error. Login failed', content=content)
            self.popup_info.open()
            return
        else:
            self.ask_permission()

    def go_to_next_screen(self):
        self.manager.get_screen('specSelect').set_sid(self.sid)
        self.manager.get_screen('gradesView').set_sid(self.sid)
        self.manager.current = 'specSelect'

    def dismiss_popup(self):
        self.popup_info.dismiss()

    def ask_permission(self):  # Asks the user if they're okey with storing their credentials
        content = ConfirmPopup(callback_no=self.callback_no, callback_yes=self.callback_yes)
        content.text = 'Do you want your data to be stored locally?'
        content.text2 = 'The next time you open the app you won\'t have to write them again'
        self.popup_conf = Popup(title='Permission', content=content)
        self.popup_conf.open()

    def callback_no(self):  # What happens when the user selects no
        self.popup_conf.dismiss()
        self.go_to_next_screen()

    def callback_yes(self):

        store = JsonStore(storagePath)
        store.put('username', value=self.ids.username.text)
        store.put('password', value=self.ids.password.text)

        self.manager.get_screen('specSelect').store = True
        self.popup_conf.dismiss()
        self.go_to_next_screen()


class SpecSelectScreen(Screen):

    def __init__(self, **kwargs):
        super(SpecSelectScreen, self).__init__(**kwargs)
        self.sid = 0
        self.specs = []
        self.store = False

    def set_sid(self, sid):
        self.sid = sid
        self.specs = get_specialization_strings(self.sid)
        self.set_data([spec['Specialization'] for spec in self.specs])

    def set_data(self, data):
        self.ids.list.data = [{'text': str(x), 'is_selected': True} for x in data]

    def on_click(self):
        selected = self.get_selected()
        selected_specs = [spec for spec in self.specs if spec['Specialization'] in selected]
        if self.store:
            store = JsonStore(storagePath)
            store.put('specs', value=selected_specs)
        self.manager.get_screen('gradesView').set_specs(selected_specs)
        self.manager.current = 'gradesView'

    def get_selected(self):
        items = self.get_items()
        # Not selected... because i can't make the default state of selected to be true.
        # So i'm considering False as selected
        selected = [item['text'] for item in items if not item['selected']]
        return selected

    def clear_data(self):
        self.sid = ''
        self.set_data([])

    def get_items(self):
        list_item = self.ids.list  # The object that holds the list
        container = list_item.ids.container  # The object that contains the labels
        items = [{'text': label.text, 'selected': label.selected} for label in container.children]
        return items


class TableViewScreen(Screen):
    def __init__(self, **kwargs):
        super(TableViewScreen, self).__init__(**kwargs)
        self.sid = 0
        self.specs = []
        self.entries = []  # Received from the server
        self.grades = []  # Labels for our app
        self.popup = None

    def set_sid(self, sid):
        self.sid = sid

    def set_specs(self, specs):
        self.specs = specs

        self.get_grades()

        self.refresh_grades()

    def get_grades(self):
        parser = SinuParser()
        self.entries = []

        for spec in self.specs:
            page = get_grades_page(self.sid, spec["Faculty"], spec["Specialization"])
            results = parser.feed(page)
            for entry in results:
                self.entries.append(entry)

    def set_data(self, data):
        self.ids.table.data = data

    def refresh_grades(self):  # Sync the data from the self.entries list with the displayed labels
        self.grades = []
        for entry in self.entries:
            self.grades.append({
                'key': entry['Disciplina'],
                'value': entry['Nota']
            })

        self.set_data(self.grades)

    def refresh(self):
        self.get_grades()
        self.refresh_grades()

    def clear_data(self):
        self.sid = ''

    def logout(self):
        content = ConfirmPopup(callback_no=self.callback_no, callback_yes=self.callback_yes)
        content.text = 'Are you sure you want to log out?'
        content.text2 = 'Your saved credentials will be wiped if you log out'
        self.popup = Popup(title='Logout', content=content)
        self.popup.open()

    def callback_yes(self):
        self.clear_data()
        self.manager.get_screen('specSelect').clear_data()
        self.manager.current = 'login'
        # Wipe the storage
        store = JsonStore(storagePath)
        if store.exists('username'):
            store.delete('username')
        if store.exists('password'):
            store.delete('password')
        if store.exists('specs'):
            store.delete('specs')
        self.popup.dismiss()

    def callback_no(self):
        self.popup.dismiss()


class MainApp(App):
    screenManager = ScreenManager()
    screenManager.transition.direction = 'down'

    def build(self):
        self.screenManager.add_widget(LoginScreen(name='login'))
        self.screenManager.add_widget(SpecSelectScreen(name='specSelect'))
        self.screenManager.add_widget(TableViewScreen(name='gradesView'))
        self.screenManager.add_widget(AboutScreen(name='about', callback=self.show_login))

        store = JsonStore(storagePath)
        if store.exists('username') and store.exists('password') and store.exists('specs'):
            sid = get_sid(store.get('username')['value'], store.get('password')['value'])
            self.screenManager.get_screen('gradesView').set_sid(sid)
            self.screenManager.get_screen('gradesView').set_specs(store.get('specs')['value'])
            self.screenManager.current = 'gradesView'

        return self.screenManager

    def show_login(self):
        self.screenManager.current = 'login'

if __name__ == '__main__':
    MainApp().run()
