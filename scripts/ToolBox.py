#!/usr/bin/python3
import rospy
import roslaunch
import tkinter as tk
import mpu9250
launch = roslaunch.scriptapi.ROSLaunch()

root = tk.Tk()
root.title("Tool Box")

v = tk.IntVar()
v.set(0)

Options = [
    ('Mpu9250 Test'),
    ('Thruster Test'),
    ('Camera Test, TODO')
]

def ShowChoice():
    print(v.get())

tk.Label(root,
        text="""Select a Tool""",
        justify = tk.LEFT,
        padx = 20).pack()

for val, option in enumerate(Options):
    tk.Radiobutton(root,
                   text = option,
                   indicatoron = 0,
                   width = 20,
                   padx = 20,
                   variable=v,
                   command = ShowChoice,
                   value = val).pack(anchor=tk.W)
    if val == 0:
        node = roslaunch.core.Node(mpu9250, test.launch)
        launch.launch(node)

root.mainloop()

