from tkinter import *
from tkinter import ttk

# Please implement
def button_pressed_handler(event):
    print(event.widget["text"] + " Button pressed")

# Please implement
def button_released_handler(event):
    print(event.widget["text"] + " Button released")

def main():
    root = Tk()

    # position the GUI at the center of your screen
    # get GUI dimensions
    windowWidth = root.winfo_reqwidth()
    windowHeight = root.winfo_reqheight()

    # move center of gui to center of screen
    positionRight = int(root.winfo_screenwidth() / 2 - windowWidth / 2)
    positionDown = int(root.winfo_screenheight() / 2 - windowHeight / 2)

    # positions the window in the center
    root.geometry("+{}+{}".format(positionRight, positionDown))

    # attach buttons to the root window
    button1 = ttk.Button(root)
    button2 = ttk.Button(root)
    button3 = ttk.Button(root)
    button4 = ttk.Button(root)
    button5 = ttk.Button(root)

    # set the text of the buttons
    button1["text"] = "Python"
    button2["text"] = "Perl"
    button3["text"] = "C++"
    button4["text"] = "Java"
    button5["text"] = "C#"

    # create a style for each button
    button_style1 = ttk.Style()
    button_style2 = ttk.Style()
    button_style3 = ttk.Style()
    button_style4 = ttk.Style()
    button_style5 = ttk.Style()

    # configure a button style for each button, e.g., "Times New Roman", 20
    button_style1.configure("button1.TButton", foreground="red", font=("Times New Roman", 20))
    button_style2.configure("button2.TButton", foreground="blue", font=("Times New Roman", 20))
    button_style3.configure("button3.TButton", foreground="red", font=("Times New Roman", 20))
    button_style4.configure("button4.TButton", foreground="blue", font=("Times New Roman", 20))
    button_style5.configure("button5.TButton", foreground="red", font=("Times New Roman", 20))

    # set buttons to have their own styles
    button1.configure(style="button1.TButton")
    button2.configure(style="button2.TButton")
    button3.configure(style="button3.TButton")
    button4.configure(style="button4.TButton")
    button5.configure(style="button5.TButton")

    # bind all the buttons to the event handlers, including "<Button-1>", "<Button-3>", "<ButtonRelease-1>", and "<ButtonRelease-3>"
    button1.bind_class("TButton", "<Button-1>", button_pressed_handler)  # One Event - Button1 Clicked
    button1.bind_class("TButton", "<ButtonRelease-1>", button_released_handler)  # One Event - Button1 Released
    button1.bind_class("TButton", "<Button-2>", button_pressed_handler)  # One Event - Button2 Clicked
    button1.bind_class("TButton", "<ButtonRelease-2>", button_released_handler)  # One Event - Button2 Released
    button1.bind_class("TButton", "<Button-3>", button_pressed_handler)  # One Event - Button3 Clicked
    button1.bind_class("TButton", "<ButtonRelease-3>", button_released_handler)  # One Event - Button3 Released
    button1.bind_class("TButton", "<Button-4>", button_pressed_handler)  # One Event - Button4 Clicked
    button1.bind_class("TButton", "<ButtonRelease-4>", button_released_handler)  # One Event - Button4 Released
    button1.bind_class("TButton", "<Button-5>", button_pressed_handler)  # One Event - Button5 Clicked
    button1.bind_class("TButton", "<ButtonRelease-5>", button_released_handler)  # One Event - Button5 Released

    # display the buttons using pack layout
    button1.pack(side=TOP)
    button2.pack(side=TOP)
    button3.pack(side=TOP)
    button4.pack(side=TOP)
    button5.pack(side=TOP)

    root.mainloop()

if __name__ == "__main__":
    main()