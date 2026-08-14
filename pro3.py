import tkinter as tk
from tkinter import ttk, messagebox
import json
import os


FILE_NAME = "contacts.json"


# ---------------- LOAD CONTACTS ----------------

def load_contacts():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)

    return []


contacts = load_contacts()


# ---------------- SAVE CONTACTS ----------------

def save_contacts():
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)


# ---------------- REFRESH CONTACT LIST ----------------

def refresh_contacts():

    contact_list.delete(*contact_list.get_children())

    for index, contact in enumerate(contacts):

        contact_list.insert(
            "",
            "end",
            iid=index,
            values=(
                contact["name"],
                contact["phone"],
                contact["email"]
            )
        )


# ---------------- CLEAR INPUT FIELDS ----------------

def clear_fields():

    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)


# ---------------- ADD CONTACT ----------------

def add_contact():

    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()

    if name == "" or phone == "" or email == "":
        messagebox.showerror(
            "Error",
            "Please fill all fields."
        )
        return

    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contacts.append(contact)

    save_contacts()
    refresh_contacts()
    clear_fields()

    messagebox.showinfo(
        "Success",
        "Contact added successfully!"
    )


# ---------------- SELECT CONTACT ----------------

def select_contact(event):

    selected_item = contact_list.selection()

    if not selected_item:
        return

    index = int(selected_item[0])

    contact = contacts[index]

    clear_fields()

    name_entry.insert(0, contact["name"])
    phone_entry.insert(0, contact["phone"])
    email_entry.insert(0, contact["email"])


# ---------------- UPDATE CONTACT ----------------

def update_contact():

    selected_item = contact_list.selection()

    if not selected_item:
        messagebox.showerror(
            "Error",
            "Please select a contact to update."
        )
        return

    index = int(selected_item[0])

    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()

    if name == "" or phone == "" or email == "":
        messagebox.showerror(
            "Error",
            "Please fill all fields."
        )
        return

    contacts[index] = {
        "name": name,
        "phone": phone,
        "email": email
    }

    save_contacts()
    refresh_contacts()
    clear_fields()

    messagebox.showinfo(
        "Success",
        "Contact updated successfully!"
    )


# ---------------- DELETE CONTACT ----------------

def delete_contact():

    selected_item = contact_list.selection()

    if not selected_item:
        messagebox.showerror(
            "Error",
            "Please select a contact to delete."
        )
        return

    index = int(selected_item[0])

    confirmation = messagebox.askyesno(
        "Confirm Delete",
        "Are you sure you want to delete this contact?"
    )

    if confirmation:

        contacts.pop(index)

        save_contacts()
        refresh_contacts()
        clear_fields()

        messagebox.showinfo(
            "Success",
            "Contact deleted successfully!"
        )


# ================= MAIN WINDOW =================

root = tk.Tk()

root.title("Contact Manager")

root.geometry("800x650")

root.resizable(False, False)

root.configure(bg="#101827")


# ================= TITLE =================

title_label = tk.Label(
    root,
    text="📱 Contact Manager",
    font=("Arial", 28, "bold"),
    bg="#101827",
    fg="white"
)

title_label.pack(pady=(25, 5))


subtitle_label = tk.Label(
    root,
    text="Store and manage your contacts easily",
    font=("Arial", 12),
    bg="#101827",
    fg="#9CA3AF"
)

subtitle_label.pack(pady=(0, 20))


# ================= INPUT CARD =================

input_card = tk.Frame(
    root,
    bg="#1F2937",
    padx=25,
    pady=20
)

input_card.pack(
    padx=30,
    fill="x"
)


# Name

tk.Label(
    input_card,
    text="Name",
    font=("Arial", 12, "bold"),
    bg="#1F2937",
    fg="white"
).grid(
    row=0,
    column=0,
    padx=10,
    pady=5,
    sticky="w"
)


name_entry = tk.Entry(
    input_card,
    font=("Arial", 12),
    width=22
)

name_entry.grid(
    row=1,
    column=0,
    padx=10,
    pady=5
)


# Phone

tk.Label(
    input_card,
    text="Phone Number",
    font=("Arial", 12, "bold"),
    bg="#1F2937",
    fg="white"
).grid(
    row=0,
    column=1,
    padx=10,
    pady=5,
    sticky="w"
)


phone_entry = tk.Entry(
    input_card,
    font=("Arial", 12),
    width=22
)

phone_entry.grid(
    row=1,
    column=1,
    padx=10,
    pady=5
)


# Email

tk.Label(
    input_card,
    text="Email Address",
    font=("Arial", 12, "bold"),
    bg="#1F2937",
    fg="white"
).grid(
    row=0,
    column=2,
    padx=10,
    pady=5,
    sticky="w"
)


email_entry = tk.Entry(
    input_card,
    font=("Arial", 12),
    width=25
)

email_entry.grid(
    row=1,
    column=2,
    padx=10,
    pady=5
)


# ================= BUTTONS =================

button_frame = tk.Frame(
    root,
    bg="#101827"
)

button_frame.pack(pady=15)


add_button = tk.Button(
    button_frame,
    text="ADD CONTACT",
    command=add_contact,
    font=("Arial", 11, "bold"),
    bg="#6366F1",
    fg="white",
    relief="flat",
    cursor="hand2"
)

add_button.grid(
    row=0,
    column=0,
    padx=8,
    ipadx=15,
    ipady=8
)


update_button = tk.Button(
    button_frame,
    text="UPDATE",
    command=update_contact,
    font=("Arial", 11, "bold"),
    bg="#10B981",
    fg="white",
    relief="flat",
    cursor="hand2"
)

update_button.grid(
    row=0,
    column=1,
    padx=8,
    ipadx=20,
    ipady=8
)


delete_button = tk.Button(
    button_frame,
    text="DELETE",
    command=delete_contact,
    font=("Arial", 11, "bold"),
    bg="#EF4444",
    fg="white",
    relief="flat",
    cursor="hand2"
)

delete_button.grid(
    row=0,
    column=2,
    padx=8,
    ipadx=20,
    ipady=8
)


clear_button = tk.Button(
    button_frame,
    text="CLEAR",
    command=clear_fields,
    font=("Arial", 11, "bold"),
    bg="#374151",
    fg="white",
    relief="flat",
    cursor="hand2"
)

clear_button.grid(
    row=0,
    column=3,
    padx=8,
    ipadx=20,
    ipady=8
)


# ================= CONTACT TABLE =================

table_frame = tk.Frame(
    root,
    bg="#1F2937"
)

table_frame.pack(
    padx=30,
    pady=10,
    fill="both",
    expand=True
)


columns = (
    "Name",
    "Phone Number",
    "Email Address"
)


contact_list = ttk.Treeview(
    table_frame,
    columns=columns,
    show="headings",
    height=12
)


contact_list.heading(
    "Name",
    text="Name"
)

contact_list.heading(
    "Phone Number",
    text="Phone Number"
)

contact_list.heading(
    "Email Address",
    text="Email Address"
)


contact_list.column(
    "Name",
    width=200
)

contact_list.column(
    "Phone Number",
    width=200
)

contact_list.column(
    "Email Address",
    width=300
)


contact_list.pack(
    fill="both",
    expand=True,
    padx=10,
    pady=10
)


# Select contact when clicked

contact_list.bind(
    "<<TreeviewSelect>>",
    select_contact
)


# Load existing contacts

refresh_contacts()


# Run application

root.mainloop()