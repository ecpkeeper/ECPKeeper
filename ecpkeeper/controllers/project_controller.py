from tkinter import *


class ProjectController:

    @staticmethod
    def setup(footprint_tab):
        upper_frame = UpperFrame(footprint_tab)
        bottom_frame = BottomFrame(footprint_tab)

        upper_frame.pack(side="top", expand=True, fill="x")
        bottom_frame.pack(side="bottom", expand=True, fill="x")


class UpperFrame(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        # DistributorsView(Frame)


class BottomFrame(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

