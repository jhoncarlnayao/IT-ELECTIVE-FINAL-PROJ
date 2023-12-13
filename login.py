import tkinter as tk

def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "admin" and password == "123":
        accgranted.config(text="Access Granted!", fg="green")
        warning.config(text="")
        contbutton.config(width=8, height=5)  # Adjust the width as needed
        contbutton.pack(side="left", padx=10)
    else:
        accgranted.config(text="Access Denied", fg="red")
        warning.config(text="Incorrect username or password. Please try again.", fg="red")

def exit_program():
    mainwindow.destroy()

def continue_function():
    mainwindow.destroy()
    import PetAdaptionPlatform
    

mainwindow = tk.Tk()
mainwindow.title("Pet Companion Hub")
mainwindow.geometry("500x300")

background_color = "#ecf0f1"
accent_color = "#3498db"
button_color = "#2ecc71"
button_hover_color = "#27ae60"

mainwindow.configure(bg=background_color)

fontt = ("Arial", 12, "bold")

header_label = tk.Label(mainwindow, text="Pet Companion Hub", font=fontt, bg=accent_color, fg="white", pady=10)
header_label.pack(fill="x")

content_frame = tk.Frame(mainwindow, padx=20, pady=10, bg=background_color)
content_frame.pack(fill="both", expand=True)

welcometext = tk.Label(content_frame, text="Welcome to the Pet Companion Hub! Connect with your furry friends.", font=("Arial", 10), justify="center", bg=background_color)
welcometext.pack(pady=5)

username_label = tk.Label(content_frame, text="Username:", font=("Arial", 10), bg=background_color)
username_label.pack()
username_entry = tk.Entry(content_frame, font=("Arial", 10))
username_entry.pack(pady=2)

password_label = tk.Label(content_frame, text="Password:", font=("Arial", 10), bg=background_color)
password_label.pack()
password_entry = tk.Entry(content_frame, show="*", font=("Arial", 10))
password_entry.pack(pady=5)

loginbutton = tk.Button(content_frame, text="Login", command=login, font=("Arial", 12, "bold"), bg=button_color, fg="white", padx=10, pady=5, activebackground=button_hover_color)
loginbutton.pack(side="left", padx=1)

exitbutton = tk.Button(content_frame, text="Exit", command=exit_program, font=("Arial", 12, "bold"), bg="#e74c3c", fg="white", padx=10, pady=5, activebackground="#c0392b")
exitbutton.pack(side="right", padx=10)

accgranted = tk.Label(content_frame, text="", font=("Arial", 12, "bold"), fg="red", bg=background_color)
accgranted.pack()

warning = tk.Label(content_frame, text="", font=("Arial", 10), fg="red", bg=background_color)
warning.pack()

contbutton = tk.Button(content_frame, text="Continue", command=continue_function, font=("Arial", 12, "bold"), bg=button_color, fg="white", padx=10, pady=8, activebackground=button_hover_color, height=3, width=8)

footer_label = tk.Label(mainwindow, text="- Connecting Hearts, One Paw at a Time!", font=("Arial", 8), fg="#e74c3c", bg=background_color)
footer_label.pack(fill="x")

mainwindow.mainloop()
