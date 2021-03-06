from kivy.core.window import Window
from kivy.uix.popup import Popup

class BaseDialog(Popup):
    def __init__(self, **kwargs):
        super(BaseDialog, self).__init__(**kwargs)
        self._keyboard = Window.request_keyboard(None, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)
        print(type(self))
            
    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        """
        When keyboard button is released, map the button to a method

        Parameters
        ----------
        keyboard : kivy.core.window.Keyboard
            kivy class to access keyboard key presses
        keycode : tuple
            numeric code for the key and the text of said key

        Returns
        -------
        None.

        """
        text = keycode[1]
        if text == "enter" and "Dialog" in str(type(self)):
            self.ids.action.trigger_action(0.2)
        
