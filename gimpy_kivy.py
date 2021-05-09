#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  1 22:47:47 2021

@author: martin
"""

import os
import json
import matplotlib.pyplot as plt
from skimage.io import imread
from kivy.app import App
from kivy.factory import Factory
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.carousel import Carousel
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg

class SaveDialog(Popup):
    def save_file(self, path):
        savepath = os.path.join(path, self.ids.dialog_savename.text)
        if not savepath.endswith('.json'):
            savepath += '.json'
        print(savepath)
        return savepath

class LoadDialog(Popup):
    pass
        
class ImageDirDialog(Popup):
    pass

class SettingsScreen(Screen):
    def __init__(self, **kwargs):
        super(SettingsScreen, self).__init__(**kwargs)
        
    def on_pre_enter(self):
        Window.size = (400, 500)
        
        # add box layout to avoid issue with
        # button spanning multiple columns
        overall = BoxLayout(orientation="vertical")
        layout = GridLayout(rows=9, cols=2)
        self.entries = []
        
        # loop to add all labels and buttons
        for i in range(8):
           lbl = Label(text=f"Class {i}")
           entry = TextInput(multiline=False)
           layout.add_widget(lbl)
           layout.add_widget(entry)
           self.entries.append(entry)
           
        load_btn = Button(text="Load")
        save_btn = Button(text="Save")
        start_btn = Button(text="Annotate", size_hint=(1.0, 0.2))
        
        # bind buttons to callbacks
        load_btn.bind(on_release=self.open_load_dialog)
        save_btn.bind(on_release=self.open_save_dialog)
        start_btn.bind(on_release=self.choose_image_dir)
        
        # add widgets to layouts
        layout.add_widget(load_btn)
        layout.add_widget(save_btn)
        overall.add_widget(layout)
        overall.add_widget(start_btn)
        self.add_widget(overall)
        
    def open_save_dialog(self, instance):
        # set up the saving file window
        saving = Factory.SaveDialog()
        saving.open()

    def save_settings(self):
        print('running save settings function')
        
        # save the data
        d = dict((i, e.text) for i, e in enumerate(self.entries))
        with open(self.savepath, "w") as f:
            json.dump(d, f)
    
    def open_load_dialog(self, instance):
        loading = Factory.LoadDialog()
        loading.open()
        
    def load_settings(self, fname):
        print("running load settings function")
        
        # load the data
        with open(fname, 'r') as f:
            data = json.load(f)
        for entry, val in zip(self.entries, data.values()):
            entry.text = val
            
    def choose_image_dir(self, instance):
        choose = Factory.ImageDirDialog()
        choose.open()
    
    def start_annotate(self, instance):
        # bind classes to the key presses
        for i, e in enumerate(self.entries):
            pass
        
        # open filechooser for directory
        # display images in the carousel

class ViewerScreen(Screen):
    def __init__(self, **kwargs):
        super(ViewerScreen, self).__init__(**kwargs)
    
    def on_pre_enter(self):
        Window.size = (700, 700)
        
        # get image filenames and info
        os.chdir(self.imgdir)
        self.imglist = [i for i in os.listdir() if i.endswith('.tif')]
        self.img_idx = 0
        
        # package widgets
        carousel = Carousel(direction="right")
        for im in self.imglist:
            img = imread(im)[self.img_idx]
            plt.imshow(img, cmap="viridis")
            plt.axis("off")
            plt.tight_layout()
            carousel.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        self.add_widget(carousel)

class gimpyApp(App):
    
    def build(self):
        sm = ScreenManager()
        sm.add_widget(SettingsScreen(name="settings"))
        sm.add_widget(ViewerScreen(name="viewer"))
        sm.current = "settings"
        # self.imgdir = None
        return sm
    
    def rename_file(self):
        pass

if __name__ == "__main__":
    gimpyApp().run()
