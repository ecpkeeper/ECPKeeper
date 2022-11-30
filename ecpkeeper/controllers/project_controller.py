from tkinter import *


class ProjectController:

    @staticmethod
    def setup(footprint_tab):
        """Setup Project Controller"""
        upper_frame = UpperFrame(footprint_tab)
        bottom_frame = BottomFrame(footprint_tab)

        upper_frame.pack(side="top", expand=True, fill="x")
        bottom_frame.pack(side="bottom", expand=True, fill="x")


class UpperFrame(Frame):
    def __init__(self, parent):
        """Setup Upper Frame"""
        Frame.__init__(self, parent)


class BottomFrame(Frame):
    def __init__(self, parent):
        """Setup Bottom Frame"""
        Frame.__init__(self, parent)

