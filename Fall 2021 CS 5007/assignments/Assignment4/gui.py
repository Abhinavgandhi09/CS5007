from tkinter import *
from tkinter import ttk


def button_released_handler(event):
    print(event.widget["text"] + " clicked")


def enter_release_comments_handler(event):
    print("Text entered = " + event.widget.get("1.0", END))


def sports_lambda_handler(widget):
    selected = " is selected"
    deselected = " is deselected"
    if widget.instate(statespec=["selected"]):
        print(widget["text"] + selected)
    else:
        print(widget["text"] + deselected)


def emails_lambda_handler(widget):
    print("Receive emails = " + widget["text"])


def updates_lambda_handler(widget):
    print("Receive updates = " + widget["text"])


def combobox_handler(event):
    print(" Selected = " + event.widget.get())


def enter_release_text_handler(event):
    print("Text entered = " + event.widget.get())

#
# def enter_release_text_handler_pwd(event):
#     print("Text entered =" +  event)


def main():
    # Create Tkinter object
    root = Tk()

    # position the GUI at the center of your screen
    # get GUI dimensions
    windowWidth = root.winfo_reqwidth()
    windowHeight = root.winfo_reqheight()

    # move center of gui to center of screen
    positionRight = int(root.winfo_screenwidth() / 2 - windowWidth)
    positionDown = int(root.winfo_screenheight() / 2 - windowHeight)

    # positions the window in the center
    root.geometry("+{}+{}".format(positionRight, positionDown))
    # root.eval('tk::PlaceWindow . center')

    # window title
    root.title("tk")
    root.resizable(width=True, height=True)

    # configure root frame
    root.rowconfigure(0, weight=1)
    root.rowconfigure(1, weight=1)
    root.rowconfigure(2, weight=1)
    root.rowconfigure(3, weight=1)

    root.columnconfigure(0, weight=1)

    text_input_frame = Frame(root, highlightcolor="pink", highlightbackground="pink", highlightthickness=5)
    input_frame = Frame(root, highlightcolor="cyan", highlightbackground="cyan", highlightthickness=5)
    radio_input_frame = Frame(input_frame, highlightcolor="orange", highlightbackground="orange", highlightthickness=5)
    check_input_frame = Frame(input_frame, highlightcolor="green", highlightbackground="green", highlightthickness=5)
    comments_frame = Frame(root, highlightcolor="red", highlightbackground="red", highlightthickness=5)
    comments_text_frame = Frame(comments_frame, highlightcolor="white", highlightbackground="white",
                                highlightthickness=1)
    button_frame = Frame(root, highlightcolor="blue", highlightbackground="blue", highlightthickness=5)

    # Place frames
    text_input_frame.grid(row=0, column=0, sticky=N + S + E + W)
    input_frame.grid(row=1, column=0, sticky=N+S+E+W)
    radio_input_frame.grid(row=0, column=0, sticky=N+S+W)
    check_input_frame.grid(row=0, column=1, sticky=N+S+E)
    comments_frame.grid(row=2, column=0, sticky=N+S+E+W)
    comments_text_frame.grid(row=1, column=0, sticky=N+S+E+W)
    button_frame.grid(row=3, column=0, sticky=N+S+E+W)

    # Configure rows in sub_frames
    text_input_frame.rowconfigure(0, weight=1)
    text_input_frame.rowconfigure(1, weight=1)
    text_input_frame.rowconfigure(2, weight=1)
    text_input_frame.rowconfigure(3, weight=1)
    text_input_frame.rowconfigure(4, weight=1)
    text_input_frame.rowconfigure(5, weight=0)

    input_frame.rowconfigure(0, weight=1)

    radio_input_frame.rowconfigure(0, weight=1)
    radio_input_frame.rowconfigure(1, weight=0)
    radio_input_frame.rowconfigure(2, weight=0)

    check_input_frame.rowconfigure(0, weight=1)
    check_input_frame.rowconfigure(1, weight=0)
    check_input_frame.rowconfigure(2, weight=0)

    comments_frame.rowconfigure(0, weight=1)
    comments_frame.rowconfigure(1, weight=1)

    # comments_text_frame.rowconfigure(0, weight=1)

    button_frame.rowconfigure(0, weight=1)

    # Configure columns in sub_frames
    text_input_frame.columnconfigure(0, weight=0)
    text_input_frame.columnconfigure(1, weight=1)

    input_frame.columnconfigure(0, weight=1)
    input_frame.columnconfigure(1, weight=1)

    radio_input_frame.columnconfigure(0, weight=1)
    radio_input_frame.columnconfigure(1, weight=1)

    check_input_frame.columnconfigure(0, weight=1)
    check_input_frame.columnconfigure(1, weight=1)

    comments_frame.columnconfigure(0, weight=1)

    # comments_text_frame.columnconfigure(0, weight=1)
    # comments_text_frame.columnconfigure(1, weight=1)

    button_frame.columnconfigure(0, weight=1)
    button_frame.columnconfigure(1, weight=1)

    # Create labels for text input boxes
    uname_label = ttk.Label(text_input_frame)
    fname_label = ttk.Label(text_input_frame)
    lname_label = ttk.Label(text_input_frame)
    pwd_label = ttk.Label(text_input_frame)
    color_label = ttk.Label(text_input_frame)
    acc_options_label = ttk.Label(text_input_frame)
    sports_label = ttk.Label(text_input_frame)
    updates_label = ttk.Label(radio_input_frame)
    notifications_label = ttk.Label(radio_input_frame)
    other_comments_label = ttk.Label(comments_frame)

    # Set label text
    uname_label["text"] = "User Name:"
    fname_label["text"] = "First Name:"
    lname_label["text"] = "Last Name:"
    pwd_label["text"] = "Password:"
    color_label["text"] = "Favorite Color:"
    acc_options_label["text"] = "Account Options:"
    sports_label["text"] = "Sports (like to watch):"
    updates_label["text"] = "Updates: "
    notifications_label["text"] = "Notification Emails:"
    other_comments_label["text"] = "Other Comments:"

    # Create label style
    main_label_style = ttk.Style()
    main_label_style.configure("main_label.TLabel", background="white", foreground="black",
                               font=("Times New Roman", 12))

    small_label_style = ttk.Style()
    small_label_style.configure("small_label.TLabel", background="white", foreground="black",
                                font=("Times New Roman", 10))

    uname_label.configure(style="main_label.TLabel")
    fname_label.configure(style="main_label.TLabel")
    lname_label.configure(style="main_label.TLabel")
    pwd_label.configure(style="main_label.TLabel")
    color_label.configure(style="main_label.TLabel")
    acc_options_label.configure(style="main_label.TLabel")
    sports_label.configure(style="main_label.TLabel")
    updates_label.configure(style="small_label.TLabel")
    notifications_label.configure(style="small_label.TLabel")
    other_comments_label.configure(style="main_label.TLabel")

    # Create text input boxes on text_input_frame
    user_name = ttk.Entry(text_input_frame)
    first_name = ttk.Entry(text_input_frame)
    last_name = ttk.Entry(text_input_frame)
    password = ttk.Entry(text_input_frame, show="*")

    # Bind text box to event
    user_name.bind("<KeyRelease-Return>", enter_release_text_handler)
    first_name.bind("<KeyRelease-Return>", enter_release_text_handler)
    last_name.bind("<KeyRelease-Return>", enter_release_text_handler)
    password.bind("<KeyRelease-Return>", enter_release_text_handler)

    # Create combobox
    color_combobox = ttk.Combobox(text_input_frame)
    color_combobox.state(["readonly"])

    color_combobox["values"] = ["Red", "Orange", "Yellow", "Green", "Blue", "Violet", "Pink", "White", "Black"]

    color_combobox.current(0)

    # Bind combobox
    color_combobox.bind("<<ComboboxSelected>>", combobox_handler)

    # Create radio buttons
    update_control = IntVar()
    email_control = IntVar()

    updates_yes = ttk.Radiobutton(radio_input_frame, value=1, variable=update_control, text="Yes",
                                  command=lambda: updates_lambda_handler(updates_yes))
    updates_no = ttk.Radiobutton(radio_input_frame, value=2, variable=update_control, text="No",
                                 command=lambda: updates_lambda_handler(updates_no))

    emails_yes = ttk.Radiobutton(radio_input_frame, value=1, variable=email_control, text="Yes",
                                 command=lambda: emails_lambda_handler(emails_yes))
    emails_no = ttk.Radiobutton(radio_input_frame, value=2, variable=email_control, text="No",
                                command=lambda: emails_lambda_handler(emails_no))

    # Create checkbutton
    baseball_control = IntVar()
    baseball_control.set(0)

    basketball_control = IntVar()
    basketball_control.set(0)

    football_control = IntVar()
    football_control.set(0)

    hockey_control = IntVar()
    hockey_control.set(0)

    baseball_button = ttk.Checkbutton(check_input_frame, variable=baseball_control, text="Baseball",
                                      command=lambda : sports_lambda_handler(baseball_button))
    basketball_button = ttk.Checkbutton(check_input_frame, variable=basketball_control, text="Basketball",
                                        command=lambda : sports_lambda_handler(basketball_button))
    football_button = ttk.Checkbutton(check_input_frame, variable=football_control, text="Football",
                                      command=lambda : sports_lambda_handler(football_button))
    hockey_button = ttk.Checkbutton(check_input_frame, variable=hockey_control, text="Hockey",
                                    command=lambda : sports_lambda_handler(hockey_button))

    # Create a text area
    comments_text = Text(comments_text_frame, wrap=WORD, height=10, width=50)

    # Bind text widget
    comments_text.bind("<KeyRelease-Return>", enter_release_comments_handler)

    # Create a vertical scrollbar
    text_scrollbar = ttk.Scrollbar(comments_text_frame, command=comments_text.yview, orient=VERTICAL)  # yview moves when scrollbar moves
    comments_text["yscrollcommand"] = text_scrollbar.set

    # Create buttons
    submit_button = ttk.Button(button_frame)
    cancel_button = ttk.Button(button_frame)

    # Set button text
    submit_button["text"] = "Submit"
    cancel_button["text"] = "Cancel"

    # Create button style
    button_style = ttk.Style()

    # Configure the style
    button_style.configure("TButton", foreground="black", font=("Times New Roman", 10))

    # Set the style to the buttons
    submit_button.configure(style="TButton")
    cancel_button.configure(style="TButton")

    # Bind buttons
    submit_button.bind_class("TButton", "<ButtonRelease-1>", button_released_handler)
    cancel_button.bind_class("TButton", "<ButtonRelease-1>", button_released_handler)

    # Position the input boxes
    user_name.grid(row=0, column=1, sticky=N + S + E + W)
    first_name.grid(row=1, column=1, sticky=N + S + E + W)
    last_name.grid(row=2, column=1, sticky=N + S + E + W)
    password.grid(row=3, column=1, sticky=N + S + E + W)

    # Position the combobox
    color_combobox.grid(row=4, column=1, sticky=N+S+E+W)

    # Position the labels
    uname_label.grid(row=0, column=0, sticky=N+S+E+W)
    fname_label.grid(row=1, column=0, sticky=N+S+E+W)
    lname_label.grid(row=2, column=0, sticky=N+S+E+W)
    pwd_label.grid(row=3, column=0, sticky=N+S+E+W)
    color_label.grid(row=4, column=0, sticky=N+S+E+W)
    acc_options_label.grid(row=5, column=0, sticky=N+S+E+W)
    sports_label.grid(row=5, column=1, sticky=N+S+E)
    updates_label.grid(row=0, column=0, sticky=N+S+E+W)
    notifications_label.grid(row=0, column=1, sticky=N+S+E+W)
    other_comments_label.grid(row=0, column=0, sticky=S+E+W)

    # Position radio button
    updates_yes.grid(row=1, column=0, sticky=N+S+E+W)
    updates_no.grid(row=2, column=0, sticky=N+S+E+W)

    emails_yes.grid(row=1, column=1, sticky=N+S+E+W)
    emails_no.grid(row=2, column=1, sticky=N+S+E+W)

    # Position checkboxes
    baseball_button.grid(row=1, column=0, sticky=N+S+E+W)
    basketball_button.grid(row=1, column=1, sticky=N+S+E+W)
    football_button.grid(row=2, column=0, sticky=N+S+E+W)
    hockey_button.grid(row=2, column=1, sticky=N+S+E+W)

    # Position the text box and scrollbar
    # comments_text.grid(row=0, column=0, sticky=N+S+E+W)
    # text_scrollbar.grid(row=0, column=1, sticky=N+S+E+W)
    comments_text.pack(expand=1, fill='both', side='left')
    text_scrollbar.pack(fill="both", side="right")

    # Position the buttons
    submit_button.grid(row=0, column=0, sticky=N+S+E+W)
    cancel_button.grid(row=0, column=1, sticky=N+S+E+W)

    # Prevent program from exiting
    root.mainloop()


if __name__ == "__main__":
    main()
