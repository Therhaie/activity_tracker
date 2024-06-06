import tkinter as tk
from tkinter import ttk
from controllers.activity_controller import ActivityController


import customtkinter
import tkinter

#todo encapsulate in class the code to make it more reusable

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme("green")

def main():
    app = customtkinter.CTk()
    app.title("Activity Tracker")
    app.geometry("500x500")

    frame = customtkinter.CTkFrame(master=app,
                                   width=200,
                                   height=200,
                                   corner_radius=20,
                                   bg_color="yellow")
    frame.pack(padx=20, pady=20)
    def func_act1():
        print("button clicked")

    button = customtkinter.CTkButton(master=frame, text="ACT 1", command=func_act1)
    button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    app.mainloop()

if __name__ == "__main__":
    main()



#
# class MainView:
#     def __init__(self, root, controller):
#         self.controller = controller
#         self.root = root
#         self.root.title("Activity Tracker")
#
#         self.name_label = ttk.Label(root, text="Activity Name:")
#         self.name_label.grid(column=0, row=0)
#         self.name_entry = ttk.Entry(root)
#         self.name_entry.grid(column=1, row=0)
#
#         self.start_button = ttk.Button(root, text="Start Activity", command=self.start_activity)
#         self.start_button.grid(column=0, row=1)
#
#         self.end_button = ttk.Button(root, text="End Activity", command=self.end_activity)
#         self.end_button.grid(column=1, row=1)
#
#         self.activities_list = tk.Listbox(root)
#         self.activities_list.grid(column=0, row=2, columnspan=2)
#
#     def start_activity(self):
#         name = self.name_entry.get()
#         if name:
#             activity = self.controller.start_activity(name)
#             self.activities_list.insert(tk.END, f"Started: {activity.name} at {activity.start_time}")
#
#     def end_activity(self):
#         # Logic to end the latest activity
#         pass
