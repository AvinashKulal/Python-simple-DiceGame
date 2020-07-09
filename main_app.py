from  kivy.app import App
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.properties import ObjectProperty
from kivy.lang.builder import Builder
from random import choice,randint


class VerificationWindow(Screen):

    capture = ObjectProperty(None)
    error_text = ObjectProperty(None)
    entered_capture = ObjectProperty(None)
    key = choice(['AX34F1', 'HU98ER', '98JIU3', '2NO4WE', '883JU3'])


    def on_enter(self, *args):
        self.capture.text =self.key

    def verify_capture(self):

        if self.entered_capture.text=="":
            pass
        elif self.key == self.entered_capture.text:
            wm.current = 'game'
        else:
            self.key = choice(['AX34F1', 'HU98ER', '98JIU3', '2NO4WE', '883JU3'])
            self.capture.text = self.key
            self.error_text.text = """----ENTER PROPER CAPTURE----"""


class GameWindow(Screen):

    player_score = ObjectProperty(None)
    computer_score = ObjectProperty(None)
    dice_score = ObjectProperty(None)
    button_text = ObjectProperty(None)
    attempt_left = ObjectProperty(None)

    def on_enter(self, *args):
        self.player_score.text = '0'
        self.computer_score.text = '0'
        self.dice_score.text = '0'
        self.turn = 0
        self.attempt = 10
        self.won = False
        self.attempt_left.text = 'ATTEMP LEFT 10'
        self.button_text.text = 'USER TURN'

    def roll_dice(self):

        if self.turn == 0 and self.attempt>1 and not(self.won):
            score = randint(1,6)
            self.dice_score.text = str(score)
            sum = score+int(self.player_score.text)
            self.player_score.text = str(sum)
            self.turn = 1
            self.attempt -= 1
            self.attempt_left.text = str(self.attempt)
            self.button_text.text = 'COMPUTER TURN'
        elif self.turn == 1 and self.attempt>1 and not(self.won):
            score = randint(1, 6)
            self.dice_score.text = str(score)
            sum = score + int(self.computer_score.text)
            self.computer_score.text = str(sum)
            self.turn = 0
            self.attempt -= 1

            self.attempt_left.text = str(self.attempt)
            self.button_text.text = 'USER TURN'
        elif not(self.won):
            if int(self.player_score.text)>int(self.computer_score.text):
                self.dice_score.text = "USER WON THE MATCH"

            else:
                self.dice_score.text = 'COMPUTER WON THE MATCH'
            self.player_score.text = ''
            self.computer_score.text = ''
            self.won = True
            self.button_text.text = 'RESET'
            self.attempt_left.text = '0'
        else:
            self.on_enter(None)


class WindowMangaer(ScreenManager):
    pass


kv = Builder.load_file('my.kv')
wm = WindowMangaer()
wm.add_widget(VerificationWindow(name='verify'))
wm.add_widget(GameWindow(name='game'))
wm.current = 'verify'
class MyMainApp(App):
    def build(self):
        return wm


if __name__ == '__main__':
    MyMainApp().run()
