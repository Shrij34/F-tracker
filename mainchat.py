# Multi-User Personal Finance Tracker with Full Logic
# Includes: Background change, multi-user management, persistent data, income/expense tracking, pie chart

import tkinter as tk
from tkinter import ttk, messagebox, filedialog, simpledialog
import csv, os
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import Image, ImageTk

# ====== Directories Setup ======
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
USERS_DIR = os.path.join(BASE_DIR, "users")
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
os.makedirs(USERS_DIR, exist_ok=True)
os.makedirs(ASSETS_DIR, exist_ok=True)

USER_DATA_FILE = os.path.join(BASE_DIR, "users.csv")
BACKGROUND_FILE = os.path.join(ASSETS_DIR, "background.png")

# ====== Global Variables ======
current_user = None
user_data_path = lambda u: os.path.join(USERS_DIR, u, "finances.csv")

COLORS = {
    'primary': '#2E3440', 'secondary': '#3B4252', 'accent': '#5E81AC',
    'success': '#A3BE8C', 'warning': '#EBCB8B', 'error': '#BF616A',
    'background': '#ECEFF4', 'surface': '#E5E9F0', 'text': '#2E3440', 'text_light': '#4C566A'
}

# ====== User Management ======
def load_users():
    if not os.path.exists(USER_DATA_FILE): return []
    with open(USER_DATA_FILE, newline='') as f:
        return [row[0] for row in csv.reader(f) if row]

def save_user(username):
    users = load_users()
    if username not in users:
        with open(USER_DATA_FILE, 'a', newline='') as f:
            csv.writer(f).writerow([username])
        user_dir = os.path.join(USERS_DIR, username)
        os.makedirs(user_dir, exist_ok=True)
        with open(user_data_path(username), 'w', newline='') as f:
            csv.writer(f).writerow(["Date", "Salary", "Rent", "Fixed Expenses", "Investments", "Expenses", "Net Savings"])

# ====== Background Functions ======
def load_background():
    if os.path.exists(BACKGROUND_FILE):
        try:
            image = Image.open(BACKGROUND_FILE)
            return ImageTk.PhotoImage(image.resize((900, 700), Image.Resampling.LANCZOS))
        except:
            return None

def change_background():
    file_path = filedialog.askopenfilename(title="Choose Background", filetypes=[("Image files", "*.png *.jpg *.jpeg *.bmp")])
    if file_path:
        try:
            img = Image.open(file_path)
            img.save(BACKGROUND_FILE)
            apply_background()
        except Exception as e:
            messagebox.showerror("Error", str(e))

def apply_background():
    bg_img = load_background()
    if bg_img:
        bg_label.config(image=bg_img)
        bg_label.image = bg_img

# ====== Launch User Window ======
def launch_user_window():
    window = tk.Tk()
    window.title("Select User")
    window.geometry("300x250")
    window.configure(bg=COLORS['background'])

    tk.Label(window, text="Select or Add User", bg=COLORS['background'], font=("Segoe UI", 12, "bold"), fg=COLORS['text']).pack(pady=10)

    users = load_users()
    listbox = tk.Listbox(window, font=("Segoe UI", 10))
    listbox.pack(pady=10, fill='both', expand=True)
    for user in users:
        listbox.insert(tk.END, user)

    def select_user():
        selection = listbox.curselection()
        if selection:
            global current_user
            current_user = listbox.get(selection[0])
            window.destroy()
            launch_main_app()

    def add_user():
        name = simpledialog.askstring("Add User", "Enter new user name:")
        if name:
            save_user(name)
            listbox.insert(tk.END, name)

    tk.Button(window, text="Use Selected", command=select_user, bg=COLORS['success'], fg='white').pack(pady=5)
    tk.Button(window, text="Add User", command=add_user, bg=COLORS['accent'], fg='white').pack(pady=5)

    window.mainloop()

# ====== Main App ======
def launch_main_app():
    global app, bg_label
    app = tk.Tk()
    app.title(f"Personal Finance Tracker - {current_user}")
    app.geometry("900x700")
    app.configure(bg=COLORS['background'])

    bg_label = tk.Label(app, bg=COLORS['background'])
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    apply_background()

    # Input Fields
    entries = {}
    for idx, label in enumerate(["Salary", "Rent", "Fixed Expenses", "Investments", "Expenses"]):
        tk.Label(app, text=label, bg=COLORS['background'], font=("Segoe UI", 10)).place(x=50, y=50 + idx * 40)
        entry = tk.Entry(app)
        entry.place(x=200, y=50 + idx * 40)
        entries[label] = entry

    # Save Button
    def save_data():
        try:
            values = {k: float(v.get()) if v.get() else 0.0 for k, v in entries.items()}
            net = values['Salary'] + values['Rent'] - values['Fixed Expenses'] - values['Investments'] - values['Expenses']
            row = [datetime.now().strftime('%Y-%m-%d')] + [values[k] for k in ["Salary", "Rent", "Fixed Expenses", "Investments", "Expenses"]] + [net]
            with open(user_data_path(current_user), 'a', newline='') as f:
                csv.writer(f).writerow(row)
            messagebox.showinfo("Saved", f"Data saved. Net Savings: ₹{net:.2f}")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers")

    tk.Button(app, text="💾 Save", command=save_data, bg=COLORS['success'], fg='white').place(x=200, y=300)
    tk.Button(app, text="🖼️ Background", command=change_background, bg=COLORS['accent'], fg='white').place(x=280, y=300)
    tk.Button(app, text="📊 Show Chart", command=lambda: draw_chart(app), bg=COLORS['warning'], fg='black').place(x=400, y=300)

    app.mainloop()

# ====== Draw Pie Chart ======
def draw_chart(parent):
    try:
        with open(user_data_path(current_user), newline='') as f:
            rows = list(csv.reader(f))
        if len(rows) <= 1:
            messagebox.showinfo("No Data", "No data to show chart.")
            return
        latest = rows[-1]
        labels = ["Fixed", "Investments", "Expenses", "Net Savings"]
        values = [float(latest[i]) for i in range(3, 7)]

        fig, ax = plt.subplots(figsize=(4, 4))
        ax.pie(values, labels=labels, autopct='%1.1f%%')
        ax.set_title(f"{current_user}'s Finance Overview")

        top = tk.Toplevel(parent)
        top.title("Chart")
        canvas = FigureCanvasTkAgg(fig, master=top)
        canvas.draw()
        canvas.get_tk_widget().pack()
    except Exception as e:
        messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    launch_user_window()
