import tkinter as tk

from framework.GUI.tkinter.components.Component import Component


class Frame(Component):
    def add(self, parent, options):
        self.object = tk.Frame(parent, options)
        return self
