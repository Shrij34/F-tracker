
# # ###################################
# # # import tkinter as tk
# # # from tkinter import ttk, messagebox, filedialog
# # # import csv, os, logging
# # # from datetime import datetime
# # # import matplotlib.pyplot as plt
# # # from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# # # from PIL import Image, ImageTk

# # # # Directories
# # # BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# # # DATA_FILE = os.path.join(BASE_DIR, "data", "finances.csv")
# # # FIXED_FILE = os.path.join(BASE_DIR, "config", "fixed_expenses.csv")
# # # INVESTMENT_FILE = os.path.join(BASE_DIR, "config", "investments.csv")
# # # BACKGROUND_FILE = os.path.join(BASE_DIR, "assets", "background.png")
# # # os.makedirs(os.path.join(BASE_DIR, "data"), exist_ok=True)
# # # os.makedirs(os.path.join(BASE_DIR, "config"), exist_ok=True)
# # # os.makedirs(os.path.join(BASE_DIR, "logs"), exist_ok=True)
# # # os.makedirs(os.path.join(BASE_DIR, "assets"), exist_ok=True)

# # # # Global variables
# # # fixed_expense_window = None
# # # investment_window = None

# # # # Logging
# # # logging.basicConfig(
# # #     filename=os.path.join(BASE_DIR, "logs", "app.log"),
# # #     level=logging.INFO,
# # #     format='%(asctime)s - %(levelname)s - %(message)s'
# # # )

# # # # 🎨 Color scheme
# # # COLORS = {
# # #     'primary': '#2E3440',
# # #     'secondary': '#3B4252',
# # #     'accent': '#5E81AC',
# # #     'success': '#A3BE8C',
# # #     'warning': '#EBCB8B',
# # #     'error': '#BF616A',
# # #     'background': '#ECEFF4',
# # #     'surface': '#E5E9F0',
# # #     'text': '#2E3440',
# # #     'text_light': '#4C566A'
# # # }

# # # # 🔁 Load/Save Functions
# # # def load_fixed_expenses():
# # #     fixed = {}
# # #     if os.path.exists(FIXED_FILE):
# # #         try:
# # #             with open(FIXED_FILE, newline='') as f:
# # #                 reader = csv.reader(f)
# # #                 next(reader, None)
# # #                 for row in reader:
# # #                     if len(row) == 2:
# # #                         fixed[row[0]] = float(row[1])
# # #         except Exception as e:
# # #             logging.error(f"Failed to load fixed expenses: {e}")
# # #     return fixed

# # # def save_fixed_expenses(fixed_dict):
# # #     try:
# # #         with open(FIXED_FILE, 'w', newline='') as f:
# # #             writer = csv.writer(f)
# # #             writer.writerow(["Description", "Amount"])
# # #             for k, v in fixed_dict.items():
# # #                 writer.writerow([k, v])
# # #         logging.info("Fixed expenses saved.")
# # #     except Exception as e:
# # #         logging.error(f"Failed to save fixed expenses: {e}")

# # # def load_investments():
# # #     investments = {}
# # #     if os.path.exists(INVESTMENT_FILE):
# # #         try:
# # #             with open(INVESTMENT_FILE, newline='') as f:
# # #                 reader = csv.reader(f)
# # #                 next(reader, None)
# # #                 for row in reader:
# # #                     if len(row) == 2:
# # #                         investments[row[0]] = float(row[1])
# # #         except Exception as e:
# # #             logging.error(f"Failed to load investments: {e}")
# # #     return investments

# # # def save_investments(investment_dict):
# # #     try:
# # #         with open(INVESTMENT_FILE, 'w', newline='') as f:
# # #             writer = csv.writer(f)
# # #             writer.writerow(["Investment Type", "Amount"])
# # #             for k, v in investment_dict.items():
# # #                 writer.writerow([k, v])
# # #         logging.info("Investments saved.")
# # #     except Exception as e:
# # #         logging.error(f"Failed to save investments: {e}")

# # # # 🧮 Data Saving
# # # def save_data(salary, rent, expenses, investments, net_savings):
# # #     try:
# # #         file_exists = os.path.isfile(DATA_FILE)
# # #         with open(DATA_FILE, mode='a', newline='') as file:
# # #             writer = csv.writer(file)
# # #             if not file_exists:
# # #                 writer.writerow(["Date", "Salary", "Rent", "Total Income", "Total Expenses", "Total Investments", "Net Savings"])
# # #             today = datetime.now().strftime("%Y-%m-%d")
# # #             total_expenses = sum(expenses.values())
# # #             total_investments = sum(investments.values())
# # #             writer.writerow([today, salary, rent, salary + rent, total_expenses, total_investments, net_savings])
# # #         logging.info("Data saved successfully")
# # #     except Exception as e:
# # #         logging.error(f"Error saving data: {e}")

# # # # 📊 Enhanced Pie Chart
# # # def show_expense_chart(expenses, investments):
# # #     for widget in chart_frame.winfo_children():
# # #         widget.destroy()
    
# # #     if not expenses and not investments:
# # #         no_data_label = tk.Label(chart_frame, text="No data to display", 
# # #                                bg=COLORS['background'], fg=COLORS['text_light'],
# # #                                font=("Segoe UI", 12))
# # #         no_data_label.pack(pady=20)
# # #         return
    
# # #     # Combine expenses and investments for the chart
# # #     all_categories = {}
# # #     all_categories.update(expenses)
    
# # #     # Add investments with different styling
# # #     for inv_name, inv_amount in investments.items():
# # #         all_categories[f"💰 {inv_name}"] = inv_amount
    
# # #     if all_categories:
# # #         categories = list(all_categories.keys())
# # #         amounts = list(all_categories.values())
        
# # #         # Create a more colorful pie chart
# # #         fig, ax = plt.subplots(figsize=(5, 5))
# # #         colors = plt.cm.Set3(range(len(categories)))
        
# # #         wedges, texts, autotexts = ax.pie(amounts, labels=categories, autopct='%1.1f%%', 
# # #                                          startangle=90, colors=colors, 
# # #                                          explode=[0.05] * len(categories))
        
# # #         ax.set_title("Financial Breakdown", fontsize=14, fontweight='bold', pad=20)
        
# # #         # Style the text
# # #         for autotext in autotexts:
# # #             autotext.set_color('white')
# # #             autotext.set_fontweight('bold')
        
# # #         plt.tight_layout()
# # #         canvas = FigureCanvasTkAgg(fig, master=chart_frame)
# # #         canvas.draw()
# # #         canvas.get_tk_widget().pack()

# # # # 🧠 Enhanced Calculate Logic
# # # def calculate():
# # #     try:
# # #         salary = float(entry_salary.get()) if entry_salary.get() else 0
# # #         rent = float(entry_rent.get()) if entry_rent.get() else 0
# # #         total_income = salary + rent

# # #         # Get regular expenses
# # #         expenses = {}
# # #         for desc, amt in expense_entries:
# # #             if desc.get() and amt.get():
# # #                 expenses[desc.get()] = float(amt.get())

# # #         # Add fixed expenses
# # #         fixed_expenses = load_fixed_expenses()
# # #         expenses.update(fixed_expenses)

# # #         # Get investments (not deducted from savings)
# # #         investments = load_investments()

# # #         total_expense = sum(expenses.values())
# # #         total_investments = sum(investments.values())
# # #         net_savings = total_income - total_expense  # Investments don't reduce savings

# # #         # Update result with colorful formatting
# # #         result_text = f"💰 Total Income: ₹{total_income:,.2f}\n"
# # #         result_text += f"💸 Total Expenses: ₹{total_expense:,.2f}\n"
# # #         result_text += f"📈 Total Investments: ₹{total_investments:,.2f}\n"
# # #         result_text += f"✅ Net Savings: ₹{net_savings:,.2f}"
        
# # #         result.set(result_text)
        
# # #         # Color code the savings based on amount
# # #         if net_savings > 0:
# # #             result_label.config(fg=COLORS['success'])
# # #         elif net_savings == 0:
# # #             result_label.config(fg=COLORS['warning'])
# # #         else:
# # #             result_label.config(fg=COLORS['error'])

# # #         save_data(salary, rent, expenses, investments, net_savings)
# # #         show_expense_chart(expenses, investments)
# # #         logging.info("Calculation complete.")

# # #     except ValueError:
# # #         logging.warning("Invalid numeric input detected.")
# # #         messagebox.showerror("Input Error", "Please enter valid numbers.")
# # #     except Exception as e:
# # #         logging.error(f"Unexpected error: {e}")
# # #         messagebox.showerror("Error", str(e))

# # # # ⚙️ Fixed Expense Editor
# # # def open_fixed_expense_editor():
# # #     global fixed_expense_window
    
# # #     if fixed_expense_window and tk.Toplevel.winfo_exists(fixed_expense_window):
# # #         fixed_expense_window.lift()
# # #         fixed_expense_window.focus()
# # #         return
    
# # #     fixed_expense_window = tk.Toplevel(app)
# # #     fixed_expense_window.title("🏠 Fixed Expenses Setup")
# # #     fixed_expense_window.configure(bg=COLORS['background'])
# # #     fixed_expense_window.geometry("500x450")
# # #     fixed_expense_window.resizable(True, True)
    
# # #     # Header
# # #     header_frame = tk.Frame(fixed_expense_window, bg=COLORS['primary'], height=50)
# # #     header_frame.pack(fill="x")
# # #     header_frame.pack_propagate(False)
    
# # #     title_label = tk.Label(header_frame, text="🏠 Fixed Expenses Manager", 
# # #                           font=("Segoe UI", 14, "bold"), 
# # #                           bg=COLORS['primary'], fg='white')
# # #     title_label.pack(expand=True)
    
# # #     subtitle_label = tk.Label(fixed_expense_window, text="Manage recurring expenses like EMI, SIPs, Rent, etc.", 
# # #                              font=("Segoe UI", 10), 
# # #                              bg=COLORS['background'], fg=COLORS['text_light'])
# # #     subtitle_label.pack(pady=10)
    
# # #     # Main content frame
# # #     content_frame = tk.Frame(fixed_expense_window, bg=COLORS['background'])
# # #     content_frame.pack(fill="both", expand=True, padx=20, pady=10)
    
# # #     # Headers for the input fields
# # #     header_row = tk.Frame(content_frame, bg=COLORS['background'])
# # #     header_row.pack(fill="x", pady=(0, 5))
    
# # #     tk.Label(header_row, text="Description", font=("Segoe UI", 10, "bold"), 
# # #              bg=COLORS['background'], fg=COLORS['primary']).pack(side="left", padx=(10, 0))
# # #     tk.Label(header_row, text="Amount (₹)", font=("Segoe UI", 10, "bold"), 
# # #              bg=COLORS['background'], fg=COLORS['primary']).pack(side="right", padx=(0, 50))
    
# # #     # Scrollable frame for entries
# # #     canvas = tk.Canvas(content_frame, bg=COLORS['background'], highlightthickness=0)
# # #     scrollbar = ttk.Scrollbar(content_frame, orient="vertical", command=canvas.yview)
# # #     scrollable_frame = tk.Frame(canvas, bg=COLORS['background'])
    
# # #     scrollable_frame.bind(
# # #         "<Configure>",
# # #         lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
# # #     )
    
# # #     canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
# # #     canvas.configure(yscrollcommand=scrollbar.set)
    
# # #     canvas.pack(side="left", fill="both", expand=True)
# # #     scrollbar.pack(side="right", fill="y")
    
# # #     entries = []
# # #     existing = load_fixed_expenses()
    
# # #     def add_expense_field(desc="", amount=""):
# # #         entry_frame = tk.Frame(scrollable_frame, bg=COLORS['surface'], relief="raised", bd=1)
# # #         entry_frame.pack(pady=3, fill="x", padx=5)
        
# # #         d = tk.StringVar(value=desc)
# # #         a = tk.StringVar(value=str(amount) if amount else "")
        
# # #         desc_entry = tk.Entry(entry_frame, textvariable=d, width=30, font=("Segoe UI", 10))
# # #         desc_entry.pack(side="left", padx=8, pady=8)
        
# # #         amt_entry = tk.Entry(entry_frame, textvariable=a, width=15, font=("Segoe UI", 10))
# # #         amt_entry.pack(side="right", padx=8, pady=8)
        
# # #         # Delete button for each row
# # #         del_btn = tk.Button(entry_frame, text="🗑️", command=lambda: delete_expense_field(entry_frame, d, a),
# # #                            bg=COLORS['error'], fg='white', font=("Segoe UI", 8),
# # #                            width=3, relief="flat")
# # #         del_btn.pack(side="right", padx=2)
        
# # #         entries.append((d, a, entry_frame))
# # #         canvas.configure(scrollregion=canvas.bbox("all"))
    
# # #     def delete_expense_field(frame, desc_var, amt_var):
# # #         # Remove from entries list
# # #         for i, (d, a, f) in enumerate(entries):
# # #             if f == frame:
# # #                 entries.pop(i)
# # #                 break
# # #         frame.destroy()
# # #         canvas.configure(scrollregion=canvas.bbox("all"))
    
# # #     # Load existing expenses
# # #     for desc, val in existing.items():
# # #         add_expense_field(desc, val)
    
# # #     # Add 3 empty fields
# # #     for _ in range(3):
# # #         add_expense_field()
    
# # #     # Button frame
# # #     button_frame = tk.Frame(fixed_expense_window, bg=COLORS['background'])
# # #     button_frame.pack(fill="x", padx=20, pady=10)
    
# # #     # Add new expense button
# # #     add_btn = tk.Button(button_frame, text="➕ Add New Expense", 
# # #                        command=lambda: add_expense_field(),
# # #                        bg=COLORS['accent'], fg='white', font=("Segoe UI", 10),
# # #                        padx=15, pady=5, relief="flat")
# # #     add_btn.pack(side="left", padx=5)
    
# # #     def save_expenses():
# # #         new_fixed = {}
# # #         for d, a, f in entries:
# # #             if d.get().strip() and a.get().strip():
# # #                 try:
# # #                     amount = float(a.get())
# # #                     if amount > 0:
# # #                         new_fixed[d.get().strip()] = amount
# # #                 except ValueError:
# # #                     messagebox.showerror("Invalid Input", f"Please enter a valid number for '{d.get()}'")
# # #                     return False
        
# # #         save_fixed_expenses(new_fixed)
# # #         messagebox.showinfo("✅ Saved", f"Fixed expenses saved successfully!\n{len(new_fixed)} expenses saved.")
# # #         return True
    
# # #     def save_and_close():
# # #         if save_expenses():
# # #             fixed_expense_window.destroy()
    
# # #     def save_only():
# # #         save_expenses()
    
# # #     # Save buttons
# # #     save_btn = tk.Button(button_frame, text="💾 Save", command=save_only,
# # #                         bg=COLORS['warning'], fg=COLORS['text'], font=("Segoe UI", 10, "bold"),
# # #                         padx=15, pady=5, relief="flat")
# # #     save_btn.pack(side="right", padx=5)
    
# # #     save_close_btn = tk.Button(button_frame, text="💾 Save & Close", command=save_and_close,
# # #                               bg=COLORS['success'], fg='white', font=("Segoe UI", 10, "bold"),
# # #                               padx=15, pady=5, relief="flat")
# # #     save_close_btn.pack(side="right", padx=5)

# # # # 📈 Investment Manager
# # # def open_investment_manager():
# # #     global investment_window
    
# # #     if investment_window and tk.Toplevel.winfo_exists(investment_window):
# # #         investment_window.lift()
# # #         investment_window.focus()
# # #         return
    
# # #     investment_window = tk.Toplevel(app)
# # #     investment_window.title("📈 Investment Manager")
# # #     investment_window.configure(bg=COLORS['background'])
# # #     investment_window.geometry("500x450")
# # #     investment_window.resizable(True, True)
    
# # #     # Header
# # #     header_frame = tk.Frame(investment_window, bg=COLORS['accent'], height=50)
# # #     header_frame.pack(fill="x")
# # #     header_frame.pack_propagate(False)
    
# # #     title_label = tk.Label(header_frame, text="📈 Investment Portfolio Manager", 
# # #                           font=("Segoe UI", 14, "bold"), 
# # #                           bg=COLORS['accent'], fg='white')
# # #     title_label.pack(expand=True)
    
# # #     subtitle_label = tk.Label(investment_window, text="Manage your investments (Bank FD, Mutual Funds, Stocks, etc.)", 
# # #                              font=("Segoe UI", 10), 
# # #                              bg=COLORS['background'], fg=COLORS['text_light'])
# # #     subtitle_label.pack(pady=10)
    
# # #     # Main content frame
# # #     content_frame = tk.Frame(investment_window, bg=COLORS['background'])
# # #     content_frame.pack(fill="both", expand=True, padx=20, pady=10)
    
# # #     # Headers for the input fields
# # #     header_row = tk.Frame(content_frame, bg=COLORS['background'])
# # #     header_row.pack(fill="x", pady=(0, 5))
    
# # #     tk.Label(header_row, text="Investment Type", font=("Segoe UI", 10, "bold"), 
# # #              bg=COLORS['background'], fg=COLORS['primary']).pack(side="left", padx=(10, 0))
# # #     tk.Label(header_row, text="Amount (₹)", font=("Segoe UI", 10, "bold"), 
# # #              bg=COLORS['background'], fg=COLORS['primary']).pack(side="right", padx=(0, 50))
    
# # #     # Scrollable frame for entries
# # #     canvas = tk.Canvas(content_frame, bg=COLORS['background'], highlightthickness=0)
# # #     scrollbar = ttk.Scrollbar(content_frame, orient="vertical", command=canvas.yview)
# # #     scrollable_frame = tk.Frame(canvas, bg=COLORS['background'])
    
# # #     scrollable_frame.bind(
# # #         "<Configure>",
# # #         lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
# # #     )
    
# # #     canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
# # #     canvas.configure(yscrollcommand=scrollbar.set)
    
# # #     canvas.pack(side="left", fill="both", expand=True)
# # #     scrollbar.pack(side="right", fill="y")
    
# # #     entries = []
# # #     existing = load_investments()
    
# # #     # Add Bank FD as default if not present
# # #     if "Bank FD" not in existing:
# # #         existing["Bank FD"] = 0
    
# # #     def add_investment_field(desc="", amount=""):
# # #         entry_frame = tk.Frame(scrollable_frame, bg=COLORS['surface'], relief="raised", bd=1)
# # #         entry_frame.pack(pady=3, fill="x", padx=5)
        
# # #         d = tk.StringVar(value=desc)
# # #         a = tk.StringVar(value=str(amount) if amount else "")
        
# # #         desc_entry = tk.Entry(entry_frame, textvariable=d, width=30, font=("Segoe UI", 10))
# # #         desc_entry.pack(side="left", padx=8, pady=8)
        
# # #         amt_entry = tk.Entry(entry_frame, textvariable=a, width=15, font=("Segoe UI", 10))
# # #         amt_entry.pack(side="right", padx=8, pady=8)
        
# # #         # Delete button for each row (except Bank FD)
# # #         if desc != "Bank FD":
# # #             del_btn = tk.Button(entry_frame, text="🗑️", command=lambda: delete_investment_field(entry_frame, d, a),
# # #                                bg=COLORS['error'], fg='white', font=("Segoe UI", 8),
# # #                                width=3, relief="flat")
# # #             del_btn.pack(side="right", padx=2)
        
# # #         entries.append((d, a, entry_frame))
# # #         canvas.configure(scrollregion=canvas.bbox("all"))
    
# # #     def delete_investment_field(frame, desc_var, amt_var):
# # #         # Don't allow deletion of Bank FD
# # #         if desc_var.get() == "Bank FD":
# # #             return
            
# # #         # Remove from entries list
# # #         for i, (d, a, f) in enumerate(entries):
# # #             if f == frame:
# # #                 entries.pop(i)
# # #                 break
# # #         frame.destroy()
# # #         canvas.configure(scrollregion=canvas.bbox("all"))
    
# # #     # Load existing investments
# # #     for desc, val in existing.items():
# # #         add_investment_field(desc, val if val != 0 else "")
    
# # #     # Add 3 empty fields
# # #     for _ in range(3):
# # #         add_investment_field()
    
# # #     # Button frame
# # #     button_frame = tk.Frame(investment_window, bg=COLORS['background'])
# # #     button_frame.pack(fill="x", padx=20, pady=10)
    
# # #     # Add new investment button
# # #     add_btn = tk.Button(button_frame, text="➕ Add New Investment", 
# # #                        command=lambda: add_investment_field(),
# # #                        bg=COLORS['accent'], fg='white', font=("Segoe UI", 10),
# # #                        padx=15, pady=5, relief="flat")
# # #     add_btn.pack(side="left", padx=5)
    
# # #     def save_investments_data():
# # #         new_investments = {}
# # #         for d, a, f in entries:
# # #             if d.get().strip() and a.get().strip():
# # #                 try:
# # #                     amount = float(a.get())
# # #                     if amount >= 0:  # Allow 0 for investments
# # #                         new_investments[d.get().strip()] = amount
# # #                 except ValueError:
# # #                     messagebox.showerror("Invalid Input", f"Please enter a valid number for '{d.get()}'")
# # #                     return False
        
# # #         save_investments(new_investments)
# # #         messagebox.showinfo("✅ Saved", f"Investments saved successfully!\n{len(new_investments)} investments saved.")
# # #         return True
    
# # #     def save_and_close():
# # #         if save_investments_data():
# # #             investment_window.destroy()
    
# # #     def save_only():
# # #         save_investments_data()
    
# # #     # Save buttons
# # #     save_btn = tk.Button(button_frame, text="💾 Save", command=save_only,
# # #                         bg=COLORS['warning'], fg=COLORS['text'], font=("Segoe UI", 10, "bold"),
# # #                         padx=15, pady=5, relief="flat")
# # #     save_btn.pack(side="right", padx=5)
    
# # #     save_close_btn = tk.Button(button_frame, text="💾 Save & Close", command=save_and_close,
# # #                               bg=COLORS['success'], fg='white', font=("Segoe UI", 10, "bold"),
# # #                               padx=15, pady=5, relief="flat")
# # #     save_close_btn.pack(side="right", padx=5)

# # # # 🖼️ Background Image Functions
# # # def load_background_image():
# # #     """Load background image if it exists"""
# # #     if os.path.exists(BACKGROUND_FILE):
# # #         try:
# # #             image = Image.open(BACKGROUND_FILE)
# # #             image = image.resize((800, 600), Image.Resampling.LANCZOS)
# # #             return ImageTk.PhotoImage(image)
# # #         except Exception as e:
# # #             logging.error(f"Failed to load background image: {e}")
# # #     return None

# # # def change_background():
# # #     """Allow user to select and set background image"""
# # #     file_path = filedialog.askopenfilename(
# # #         title="Select Background Image",
# # #         filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif *.bmp")]
# # #     )
# # #     if file_path:
# # #         try:
# # #             # Copy the selected image to assets folder
# # #             image = Image.open(file_path)
# # #             image.save(BACKGROUND_FILE)
# # #             messagebox.showinfo("Success", f"Background changed! Restart the app to see changes.\n\nImage saved to: {BACKGROUND_FILE}")
# # #         except Exception as e:
# # #             messagebox.showerror("Error", f"Failed to set background: {e}")

# # # # 🌈 Enhanced UI Setup
# # # app = tk.Tk()
# # # app.title("💰 Personal Finance Tracker Pro")
# # # app.configure(bg=COLORS['background'])
# # # app.geometry("900x700")

# # # # Try to load background image
# # # bg_image = load_background_image()
# # # if bg_image:
# # #     bg_label = tk.Label(app, image=bg_image, bg=COLORS['background'])
# # #     bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# # # # Main container with semi-transparent background
# # # main_container = tk.Frame(app, bg=COLORS['background'], relief="raised", bd=2)
# # # main_container.pack(fill="both", expand=True, padx=20, pady=20)

# # # # Header
# # # header_frame = tk.Frame(main_container, bg=COLORS['primary'], height=60)
# # # header_frame.pack(fill="x", pady=(0, 20))
# # # header_frame.pack_propagate(False)

# # # title_label = tk.Label(header_frame, text="💰 Personal Finance Tracker Pro", 
# # #                       font=("Segoe UI", 18, "bold"), 
# # #                       bg=COLORS['primary'], fg='white')
# # # title_label.pack(expand=True)

# # # # Create notebook for tabs
# # # notebook = ttk.Notebook(main_container)
# # # notebook.pack(fill="both", expand=True)

# # # # Main tab
# # # main_tab = tk.Frame(notebook, bg=COLORS['background'])
# # # notebook.add(main_tab, text="💼 Main Calculator")

# # # # Left panel for inputs
# # # left_panel = tk.Frame(main_tab, bg=COLORS['surface'], relief="raised", bd=2)
# # # left_panel.pack(side="left", fill="both", expand=True, padx=(0, 10), pady=10)

# # # # Income section
# # # income_frame = tk.LabelFrame(left_panel, text="💰 Income Sources", 
# # #                            font=("Segoe UI", 12, "bold"),
# # #                            bg=COLORS['surface'], fg=COLORS['primary'])
# # # income_frame.pack(fill="x", padx=15, pady=10)

# # # tk.Label(income_frame, text="Monthly Salary (₹):", 
# # #          font=("Segoe UI", 10), bg=COLORS['surface']).pack(anchor="w", pady=2)
# # # entry_salary = tk.Entry(income_frame, font=("Segoe UI", 11), width=20)
# # # entry_salary.pack(fill="x", padx=5, pady=2)

# # # tk.Label(income_frame, text="Rental Income (₹):", 
# # #          font=("Segoe UI", 10), bg=COLORS['surface']).pack(anchor="w", pady=2)
# # # entry_rent = tk.Entry(income_frame, font=("Segoe UI", 11), width=20)
# # # entry_rent.pack(fill="x", padx=5, pady=2)

# # # # Expenses section
# # # expense_main_frame = tk.LabelFrame(left_panel, text="💸 Monthly Expenses", 
# # #                                  font=("Segoe UI", 12, "bold"),
# # #                                  bg=COLORS['surface'], fg=COLORS['primary'])
# # # expense_main_frame.pack(fill="both", expand=True, padx=15, pady=10)

# # # expense_frame = tk.Frame(expense_main_frame, bg=COLORS['surface'])
# # # expense_frame.pack(fill="both", expand=True, padx=10, pady=5)
# # # expense_entries = []

# # # def add_expense_field():
# # #     desc = tk.StringVar()
# # #     amt = tk.StringVar()
# # #     frame = tk.Frame(expense_frame, bg=COLORS['background'], relief="flat", bd=1)
# # #     frame.pack(pady=2, fill='x')
    
# # #     desc_entry = tk.Entry(frame, textvariable=desc, width=20, font=("Segoe UI", 10))
# # #     desc_entry.pack(side="left", padx=5, pady=2)
    
# # #     amt_entry = tk.Entry(frame, textvariable=amt, width=12, font=("Segoe UI", 10))
# # #     amt_entry.pack(side="right", padx=5, pady=2)
    
# # #     expense_entries.append((desc, amt))

# # # # Add initial expense fields
# # # for _ in range(4):
# # #     add_expense_field()

# # # add_expense_btn = tk.Button(expense_main_frame, text="➕ Add More Expenses", 
# # #                           command=add_expense_field,
# # #                           bg=COLORS['accent'], fg='white', 
# # #                           font=("Segoe UI", 10), relief="flat")
# # # add_expense_btn.pack(pady=10)

# # # # Button section
# # # button_frame = tk.Frame(left_panel, bg=COLORS['surface'])
# # # button_frame.pack(fill="x", padx=15, pady=10)

# # # calc_btn = tk.Button(button_frame, text="🧮 Calculate & Save", command=calculate,
# # #                     bg=COLORS['success'], fg='white', 
# # #                     font=("Segoe UI", 12, "bold"), 
# # #                     relief="flat", padx=20, pady=8)
# # # calc_btn.pack(fill="x", pady=5)

# # # fixed_btn = tk.Button(button_frame, text="🏠 Fixed Expenses Setup", 
# # #                      command=open_fixed_expense_editor,
# # #                      bg=COLORS['warning'], fg=COLORS['text'], 
# # #                      font=("Segoe UI", 10), relief="flat", padx=20, pady=5)
# # # fixed_btn.pack(fill="x", pady=2)

# # # invest_btn = tk.Button(button_frame, text="📈 Investment Manager", 
# # #                       command=open_investment_manager,
# # #                       bg=COLORS['accent'], fg='white', 
# # #                       font=("Segoe UI", 10), relief="flat", padx=20, pady=5)
# # # invest_btn.pack(fill="x", pady=2)

# # # bg_btn = tk.Button(button_frame, text="🖼️ Change Background", 
# # #                   command=change_background,
# # #                   bg=COLORS['secondary'], fg='white', 
# # #                   font=("Segoe UI", 9), relief="flat", padx=20, pady=3)
# # # bg_btn.pack(fill="x", pady=2)

# # # # Right panel for results
# # # right_panel = tk.Frame(main_tab, bg=COLORS['surface'], relief="raised", bd=2)
# # # right_panel.pack(side="right", fill="both", expand=True, padx=(10, 0), pady=10)

# # # # Results section
# # # result_frame = tk.LabelFrame(right_panel, text="📊 Financial Summary", 
# # #                            font=("Segoe UI", 12, "bold"),
# # #                            bg=COLORS['surface'], fg=COLORS['primary'])
# # # result_frame.pack(fill="x", padx=15, pady=10)

# # # result = tk.StringVar()
# # # result_label = tk.Label(result_frame, textvariable=result, 
# # #                        font=("Segoe UI", 11, "bold"), 
# # #                        bg=COLORS['surface'], fg=COLORS['success'],
# # #                        justify="left")
# # # result_label.pack(pady=10)

# # # # Chart section
# # # chart_label_frame = tk.LabelFrame(right_panel, text="📈 Visual Breakdown", 
# # #                                 font=("Segoe UI", 12, "bold"),
# # #                                 bg=COLORS['surface'], fg=COLORS['primary'])
# # # chart_label_frame.pack(fill="both", expand=True, padx=15, pady=10)

# # # chart_frame = tk.Frame(chart_label_frame, bg=COLORS['surface'])
# # # chart_frame.pack(fill="both", expand=True, padx=10, pady=10)

# # # # Add help text at bottom
# # # help_text = ("💡 Tips: Use Fixed Expenses for recurring payments like EMI, SIP. "
# # #             "Use Investment Manager to track your investments separately. "
# # #             "Investments don't reduce your savings calculation!")
# # # help_label = tk.Label(main_container, text=help_text, 
# # #                      font=("Segoe UI", 9), 
# # #                      bg=COLORS['background'], fg=COLORS['text_light'],
# # #                      wraplength=850, justify="center")
# # # help_label.pack(pady=10)

# # # # Instructions for background image
# # # instructions = f"""
# # # 🖼️ Background Image Instructions:
# # # 1. Click 'Change Background' button to select an image
# # # 2. Or manually place your image at: {BACKGROUND_FILE}
# # # 3. Restart the app to see the background
# # # 4. Supported formats: PNG, JPG, JPEG, GIF, BMP
# # # """
# # # print(instructions)

# # # app.mainloop()








# # # # import tkinter as tk
# # # # from tkinter import ttk, messagebox, filedialog
# # # # import csv, os, logging
# # # # from datetime import datetime
# # # # import matplotlib.pyplot as plt
# # # # from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# # # # from PIL import Image, ImageTk

# # # # # Directories
# # # # BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# # # # DATA_FILE = os.path.join(BASE_DIR, "data", "finances.csv")
# # # # FIXED_FILE = os.path.join(BASE_DIR, "config", "fixed_expenses.csv")
# # # # INVESTMENT_FILE = os.path.join(BASE_DIR, "config", "investments.csv")
# # # # BACKGROUND_FILE = os.path.join(BASE_DIR, "assets", "background.png")
# # # # os.makedirs(os.path.join(BASE_DIR, "data"), exist_ok=True)
# # # # os.makedirs(os.path.join(BASE_DIR, "config"), exist_ok=True)
# # # # os.makedirs(os.path.join(BASE_DIR, "logs"), exist_ok=True)
# # # # os.makedirs(os.path.join(BASE_DIR, "assets"), exist_ok=True)

# # # # # Global variables
# # # # fixed_expense_window = None
# # # # investment_window = None

# # # # # Logging
# # # # logging.basicConfig(
# # # #     filename=os.path.join(BASE_DIR, "logs", "app.log"),
# # # #     level=logging.INFO,
# # # #     format='%(asctime)s - %(levelname)s - %(message)s'
# # # # )

# # # # # 🎨 Color scheme
# # # # COLORS = {
# # # #     'primary': '#2E3440',
# # # #     'secondary': '#3B4252',
# # # #     'accent': '#5E81AC',
# # # #     'success': '#A3BE8C',
# # # #     'warning': '#EBCB8B',
# # # #     'error': '#BF616A',
# # # #     'background': '#ECEFF4',
# # # #     'surface': '#E5E9F0',
# # # #     'text': '#2E3440',
# # # #     'text_light': '#4C566A'
# # # # }

# # # # # 🔁 Load/Save Functions
# # # # def load_fixed_expenses():
# # # #     fixed = {}
# # # #     if os.path.exists(FIXED_FILE):
# # # #         try:
# # # #             with open(FIXED_FILE, newline='') as f:
# # # #                 reader = csv.reader(f)
# # # #                 next(reader, None)
# # # #                 for row in reader:
# # # #                     if len(row) == 2:
# # # #                         fixed[row[0]] = float(row[1])
# # # #         except Exception as e:
# # # #             logging.error(f"Failed to load fixed expenses: {e}")
# # # #     return fixed

# # # # def save_fixed_expenses(fixed_dict):
# # # #     try:
# # # #         with open(FIXED_FILE, 'w', newline='') as f:
# # # #             writer = csv.writer(f)
# # # #             writer.writerow(["Description", "Amount"])
# # # #             for k, v in fixed_dict.items():
# # # #                 writer.writerow([k, v])
# # # #         logging.info("Fixed expenses saved.")
# # # #     except Exception as e:
# # # #         logging.error(f"Failed to save fixed expenses: {e}")

# # # # def load_investments():
# # # #     investments = {}
# # # #     if os.path.exists(INVESTMENT_FILE):
# # # #         try:
# # # #             with open(INVESTMENT_FILE, newline='') as f:
# # # #                 reader = csv.reader(f)
# # # #                 next(reader, None)
# # # #                 for row in reader:
# # # #                     if len(row) == 2:
# # # #                         investments[row[0]] = float(row[1])
# # # #         except Exception as e:
# # # #             logging.error(f"Failed to load investments: {e}")
# # # #     return investments

# # # # def save_investments(investment_dict):
# # # #     try:
# # # #         with open(INVESTMENT_FILE, 'w', newline='') as f:
# # # #             writer = csv.writer(f)
# # # #             writer.writerow(["Investment Type", "Amount"])
# # # #             for k, v in investment_dict.items():
# # # #                 writer.writerow([k, v])
# # # #         logging.info("Investments saved.")
# # # #     except Exception as e:
# # # #         logging.error(f"Failed to save investments: {e}")

# # # # # 🧮 Data Saving
# # # # def save_data(salary, rent, expenses, investments, net_savings):
# # # #     try:
# # # #         file_exists = os.path.isfile(DATA_FILE)
# # # #         with open(DATA_FILE, mode='a', newline='') as file:
# # # #             writer = csv.writer(file)
# # # #             if not file_exists:
# # # #                 writer.writerow(["Date", "Salary", "Rent", "Total Income", "Total Expenses", "Total Investments", "Net Savings"])
# # # #             today = datetime.now().strftime("%Y-%m-%d")
# # # #             total_expenses = sum(expenses.values())
# # # #             total_investments = sum(investments.values())
# # # #             writer.writerow([today, salary, rent, salary + rent, total_expenses, total_investments, net_savings])
# # # #         logging.info("Data saved successfully")
# # # #     except Exception as e:
# # # #         logging.error(f"Error saving data: {e}")

# # # # # 📊 Enhanced Pie Chart
# # # # def show_expense_chart(expenses, investments):
# # # #     for widget in chart_frame.winfo_children():
# # # #         widget.destroy()
    
# # # #     if not expenses and not investments:
# # # #         no_data_label = tk.Label(chart_frame, text="No data to display", 
# # # #                                bg=COLORS['background'], fg=COLORS['text_light'],
# # # #                                font=("Segoe UI", 12))
# # # #         no_data_label.pack(pady=20)
# # # #         return
    
# # # #     # Combine expenses and investments for the chart
# # # #     all_categories = {}
# # # #     all_categories.update(expenses)
    
# # # #     # Add investments with different styling
# # # #     for inv_name, inv_amount in investments.items():
# # # #         all_categories[f"💰 {inv_name}"] = inv_amount
    
# # # #     if all_categories:
# # # #         categories = list(all_categories.keys())
# # # #         amounts = list(all_categories.values())
        
# # # #         # Create a more colorful pie chart
# # # #         fig, ax = plt.subplots(figsize=(5, 5))
# # # #         colors = plt.cm.Set3(range(len(categories)))
        
# # # #         wedges, texts, autotexts = ax.pie(amounts, labels=categories, autopct='%1.1f%%', 
# # # #                                          startangle=90, colors=colors, 
# # # #                                          explode=[0.05] * len(categories))
        
# # # #         ax.set_title("Financial Breakdown", fontsize=14, fontweight='bold', pad=20)
        
# # # #         # Style the text
# # # #         for autotext in autotexts:
# # # #             autotext.set_color('white')
# # # #             autotext.set_fontweight('bold')
        
# # # #         plt.tight_layout()
# # # #         canvas = FigureCanvasTkAgg(fig, master=chart_frame)
# # # #         canvas.draw()
# # # #         canvas.get_tk_widget().pack()

# # # # # 🧠 Enhanced Calculate Logic
# # # # def calculate():
# # # #     try:
# # # #         salary = float(entry_salary.get()) if entry_salary.get() else 0
# # # #         rent = float(entry_rent.get()) if entry_rent.get() else 0
# # # #         total_income = salary + rent

# # # #         # Get regular expenses
# # # #         expenses = {}
# # # #         for desc, amt in expense_entries:
# # # #             if desc.get() and amt.get():
# # # #                 expenses[desc.get()] = float(amt.get())

# # # #         # Add fixed expenses
# # # #         fixed_expenses = load_fixed_expenses()
# # # #         expenses.update(fixed_expenses)

# # # #         # Get investments (not deducted from savings)
# # # #         investments = load_investments()

# # # #         total_expense = sum(expenses.values())
# # # #         total_investments = sum(investments.values())
# # # #         net_savings = total_income - total_expense  # Investments don't reduce savings

# # # #         # Update result with colorful formatting
# # # #         result_text = f"💰 Total Income: ₹{total_income:,.2f}\n"
# # # #         result_text += f"💸 Total Expenses: ₹{total_expense:,.2f}\n"
# # # #         result_text += f"📈 Total Investments: ₹{total_investments:,.2f}\n"
# # # #         result_text += f"✅ Net Savings: ₹{net_savings:,.2f}"
        
# # # #         result.set(result_text)
        
# # # #         # Color code the savings based on amount
# # # #         if net_savings > 0:
# # # #             result_label.config(fg=COLORS['success'])
# # # #         elif net_savings == 0:
# # # #             result_label.config(fg=COLORS['warning'])
# # # #         else:
# # # #             result_label.config(fg=COLORS['error'])

# # # #         save_data(salary, rent, expenses, investments, net_savings)
# # # #         show_expense_chart(expenses, investments)
# # # #         logging.info("Calculation complete.")

# # # #     except ValueError:
# # # #         logging.warning("Invalid numeric input detected.")
# # # #         messagebox.showerror("Input Error", "Please enter valid numbers.")
# # # #     except Exception as e:
# # # #         logging.error(f"Unexpected error: {e}")
# # # #         messagebox.showerror("Error", str(e))

# # # # # ⚙️ Fixed Expense Editor
# # # # def open_fixed_expense_editor():
# # # #     global fixed_expense_window
    
# # # #     if fixed_expense_window and tk.Toplevel.winfo_exists(fixed_expense_window):
# # # #         fixed_expense_window.lift()
# # # #         fixed_expense_window.focus()
# # # #         return
    
# # # #     fixed_expense_window = tk.Toplevel(app)
# # # #     fixed_expense_window.title("🏠 Fixed Expenses Setup")
# # # #     fixed_expense_window.configure(bg=COLORS['background'])
# # # #     fixed_expense_window.geometry("500x450")
# # # #     fixed_expense_window.resizable(True, True)
    
# # # #     # Header
# # # #     header_frame = tk.Frame(fixed_expense_window, bg=COLORS['primary'], height=50)
# # # #     header_frame.pack(fill="x")
# # # #     header_frame.pack_propagate(False)
    
# # # #     title_label = tk.Label(header_frame, text="🏠 Fixed Expenses Manager", 
# # # #                           font=("Segoe UI", 14, "bold"), 
# # # #                           bg=COLORS['primary'], fg='white')
# # # #     title_label.pack(expand=True)
    
# # # #     subtitle_label = tk.Label(fixed_expense_window, text="Manage recurring expenses like EMI, SIPs, Rent, etc.", 
# # # #                              font=("Segoe UI", 10), 
# # # #                              bg=COLORS['background'], fg=COLORS['text_light'])
# # # #     subtitle_label.pack(pady=10)
    
# # # #     # Main content frame
# # # #     content_frame = tk.Frame(fixed_expense_window, bg=COLORS['background'])
# # # #     content_frame.pack(fill="both", expand=True, padx=20, pady=10)
    
# # # #     # Headers for the input fields
# # # #     header_row = tk.Frame(content_frame, bg=COLORS['background'])
# # # #     header_row.pack(fill="x", pady=(0, 5))
    
# # # #     tk.Label(header_row, text="Description", font=("Segoe UI", 10, "bold"), 
# # # #              bg=COLORS['background'], fg=COLORS['primary']).pack(side="left", padx=(10, 0))
# # # #     tk.Label(header_row, text="Amount (₹)", font=("Segoe UI", 10, "bold"), 
# # # #              bg=COLORS['background'], fg=COLORS['primary']).pack(side="right", padx=(0, 50))
    
# # # #     # Scrollable frame for entries
# # # #     canvas = tk.Canvas(content_frame, bg=COLORS['background'], highlightthickness=0)
# # # #     scrollbar = ttk.Scrollbar(content_frame, orient="vertical", command=canvas.yview)
# # # #     scrollable_frame = tk.Frame(canvas, bg=COLORS['background'])
    
# # # #     scrollable_frame.bind(
# # # #         "<Configure>",
# # # #         lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
# # # #     )
    
# # # #     canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
# # # #     canvas.configure(yscrollcommand=scrollbar.set)
    
# # # #     canvas.pack(side="left", fill="both", expand=True)
# # # #     scrollbar.pack(side="right", fill="y")
    
# # # #     entries = []
# # # #     existing = load_fixed_expenses()
    
# # # #     def add_expense_field(desc="", amount=""):
# # # #         entry_frame = tk.Frame(scrollable_frame, bg=COLORS['surface'], relief="raised", bd=1)
# # # #         entry_frame.pack(pady=3, fill="x", padx=5)
        
# # # #         d = tk.StringVar(value=desc)
# # # #         a = tk.StringVar(value=str(amount) if amount else "")
        
# # # #         desc_entry = tk.Entry(entry_frame, textvariable=d, width=30, font=("Segoe UI", 10))
# # # #         desc_entry.pack(side="left", padx=8, pady=8)
        
# # # #         amt_entry = tk.Entry(entry_frame, textvariable=a, width=15, font=("Segoe UI", 10))
# # # #         amt_entry.pack(side="right", padx=8, pady=8)
        
# # # #         # Delete button for each row
# # # #         del_btn = tk.Button(entry_frame, text="🗑️", command=lambda: delete_expense_field(entry_frame, d, a),
# # # #                            bg=COLORS['error'], fg='white', font=("Segoe UI", 8),
# # # #                            width=3, relief="flat")
# # # #         del_btn.pack(side="right", padx=2)
        
# # # #         entries.append((d, a, entry_frame))
# # # #         canvas.configure(scrollregion=canvas.bbox("all"))
    
# # # #     def delete_expense_field(frame, desc_var, amt_var):
# # # #         # Remove from entries list
# # # #         for i, (d, a, f) in enumerate(entries):
# # # #             if f == frame:
# # # #                 entries.pop(i)
# # # #                 break
# # # #         frame.destroy()
# # # #         canvas.configure(scrollregion=canvas.bbox("all"))
    
# # # #     # Load existing expenses
# # # #     for desc, val in existing.items():
# # # #         add_expense_field(desc, val)
    
# # # #     # Add 3 empty fields
# # # #     for _ in range(3):
# # # #         add_expense_field()
    
# # # #     # Button frame
# # # #     button_frame = tk.Frame(fixed_expense_window, bg=COLORS['background'])
# # # #     button_frame.pack(fill="x", padx=20, pady=10)
    
# # # #     # Add new expense button
# # # #     add_btn = tk.Button(button_frame, text="➕ Add New Expense", 
# # # #                        command=lambda: add_expense_field(),
# # # #                        bg=COLORS['accent'], fg='white', font=("Segoe UI", 10),
# # # #                        padx=15, pady=5, relief="flat")
# # # #     add_btn.pack(side="left", padx=5)
    
# # # #     def save_expenses():
# # # #         new_fixed = {}
# # # #         for d, a, f in entries:
# # # #             if d.get().strip() and a.get().strip():
# # # #                 try:
# # # #                     amount = float(a.get())
# # # #                     if amount > 0:
# # # #                         new_fixed[d.get().strip()] = amount
# # # #                 except ValueError:
# # # #                     messagebox.showerror("Invalid Input", f"Please enter a valid number for '{d.get()}'")
# # # #                     return False
        
# # # #         save_fixed_expenses(new_fixed)
# # # #         messagebox.showinfo("✅ Saved", f"Fixed expenses saved successfully!\n{len(new_fixed)} expenses saved.")
# # # #         return True
    
# # # #     def save_and_close():
# # # #         if save_expenses():
# # # #             fixed_expense_window.destroy()
    
# # # #     def save_only():
# # # #         save_expenses()
    
# # # #     # Save buttons
# # # #     save_btn = tk.Button(button_frame, text="💾 Save", command=save_only,
# # # #                         bg=COLORS['warning'], fg=COLORS['text'], font=("Segoe UI", 10, "bold"),
# # # #                         padx=15, pady=5, relief="flat")
# # # #     save_btn.pack(side="right", padx=5)
    
# # # #     save_close_btn = tk.Button(button_frame, text="💾 Save & Close", command=save_and_close,
# # # #                               bg=COLORS['success'], fg='white', font=("Segoe UI", 10, "bold"),
# # # #                               padx=15, pady=5, relief="flat")
# # # #     save_close_btn.pack(side="right", padx=5)

# # # # # 📈 Investment Manager
# # # # def open_investment_manager():
# # # #     global investment_window
    
# # # #     if investment_window and tk.Toplevel.winfo_exists(investment_window):
# # # #         investment_window.lift()
# # # #         investment_window.focus()
# # # #         return
    
# # # #     investment_window = tk.Toplevel(app)
# # # #     investment_window.title("📈 Investment Manager")
# # # #     investment_window.configure(bg=COLORS['background'])
# # # #     investment_window.geometry("500x450")
# # # #     investment_window.resizable(True, True)
    
# # # #     # Header
# # # #     header_frame = tk.Frame(investment_window, bg=COLORS['accent'], height=50)
# # # #     header_frame.pack(fill="x")
# # # #     header_frame.pack_propagate(False)
    
# # # #     title_label = tk.Label(header_frame, text="📈 Investment Portfolio Manager", 
# # # #                           font=("Segoe UI", 14, "bold"), 
# # # #                           bg=COLORS['accent'], fg='white')
# # # #     title_label.pack(expand=True)
    
# # # #     subtitle_label = tk.Label(investment_window, text="Manage your investments (Bank FD, Mutual Funds, Stocks, etc.)", 
# # # #                              font=("Segoe UI", 10), 
# # # #                              bg=COLORS['background'], fg=COLORS['text_light'])
# # # #     subtitle_label.pack(pady=10)
    
# # # #     # Main content frame
# # # #     content_frame = tk.Frame(investment_window, bg=COLORS['background'])
# # # #     content_frame.pack(fill="both", expand=True, padx=20, pady=10)
    
# # # #     # Headers for the input fields
# # # #     header_row = tk.Frame(content_frame, bg=COLORS['background'])
# # # #     header_row.pack(fill="x", pady=(0, 5))
    
# # # #     tk.Label(header_row, text="Investment Type", font=("Segoe UI", 10, "bold"), 
# # # #              bg=COLORS['background'], fg=COLORS['primary']).pack(side="left", padx=(10, 0))
# # # #     tk.Label(header_row, text="Amount (₹)", font=("Segoe UI", 10, "bold"), 
# # # #              bg=COLORS['background'], fg=COLORS['primary']).pack(side="right", padx=(0, 50))
    
# # # #     # Scrollable frame for entries
# # # #     canvas = tk.Canvas(content_frame, bg=COLORS['background'], highlightthickness=0)
# # # #     scrollbar = ttk.Scrollbar(content_frame, orient="vertical", command=canvas.yview)
# # # #     scrollable_frame = tk.Frame(canvas, bg=COLORS['background'])
    
# # # #     scrollable_frame.bind(
# # # #         "<Configure>",
# # # #         lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
# # # #     )
    
# # # #     canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
# # # #     canvas.configure(yscrollcommand=scrollbar.set)
    
# # # #     canvas.pack(side="left", fill="both", expand=True)
# # # #     scrollbar.pack(side="right", fill="y")
    
# # # #     entries = []
# # # #     existing = load_investments()
    
# # # #     # Add Bank FD as default if not present
# # # #     if "Bank FD" not in existing:
# # # #         existing["Bank FD"] = 0
    
# # # #     def add_investment_field(desc="", amount=""):
# # # #         entry_frame = tk.Frame(scrollable_frame, bg=COLORS['surface'], relief="raised", bd=1)
# # # #         entry_frame.pack(pady=3, fill="x", padx=5)
        
# # # #         d = tk.StringVar(value=desc)
# # # #         a = tk.StringVar(value=str(amount) if amount else "")
        
# # # #         desc_entry = tk.Entry(entry_frame, textvariable=d, width=30, font=("Segoe UI", 10))
# # # #         desc_entry.pack(side="left", padx=8, pady=8)
        
# # # #         amt_entry = tk.Entry(entry_frame, textvariable=a, width=15, font=("Segoe UI", 10))
# # # #         amt_entry.pack(side="right", padx=8, pady=8)
        
# # # #         # Delete button for each row (except Bank FD)
# # # #         if desc != "Bank FD":
# # # #             del_btn = tk.Button(entry_frame, text="🗑️", command=lambda: delete_investment_field(entry_frame, d, a),
# # # #                                bg=COLORS['error'], fg='white', font=("Segoe UI", 8),
# # # #                                width=3, relief="flat")
# # # #             del_btn.pack(side="right", padx=2)
        
# # # #         entries.append((d, a, entry_frame))
# # # #         canvas.configure(scrollregion=canvas.bbox("all"))
    
# # # #     def delete_investment_field(frame, desc_var, amt_var):
# # # #         # Don't allow deletion of Bank FD
# # # #         if desc_var.get() == "Bank FD":
# # # #             return
            
# # # #         # Remove from entries list
# # # #         for i, (d, a, f) in enumerate(entries):
# # # #             if f == frame:
# # # #                 entries.pop(i)
# # # #                 break
# # # #         frame.destroy()
# # # #         canvas.configure(scrollregion=canvas.bbox("all"))
    
# # # #     # Load existing investments
# # # #     for desc, val in existing.items():
# # # #         add_investment_field(desc, val if val != 0 else "")
    
# # # #     # Add 3 empty fields
# # # #     for _ in range(3):
# # # #         add_investment_field()
    
# # # #     # Button frame
# # # #     button_frame = tk.Frame(investment_window, bg=COLORS['background'])
# # # #     button_frame.pack(fill="x", padx=20, pady=10)
    
# # # #     # Add new investment button
# # # #     add_btn = tk.Button(button_frame, text="➕ Add New Investment", 
# # # #                        command=lambda: add_investment_field(),
# # # #                        bg=COLORS['accent'], fg='white', font=("Segoe UI", 10),
# # # #                        padx=15, pady=5, relief="flat")
# # # #     add_btn.pack(side="left", padx=5)
    
# # # #     def save_investments_data():
# # # #         new_investments = {}
# # # #         for d, a, f in entries:
# # # #             if d.get().strip() and a.get().strip():
# # # #                 try:
# # # #                     amount = float(a.get())
# # # #                     if amount >= 0:  # Allow 0 for investments
# # # #                         new_investments[d.get().strip()] = amount
# # # #                 except ValueError:
# # # #                     messagebox.showerror("Invalid Input", f"Please enter a valid number for '{d.get()}'")
# # # #                     return False
        
# # # #         save_investments(new_investments)
# # # #         messagebox.showinfo("✅ Saved", f"Investments saved successfully!\n{len(new_investments)} investments saved.")
# # # #         return True
    
# # # #     def save_and_close():
# # # #         if save_investments_data():
# # # #             investment_window.destroy()
    
# # # #     def save_only():
# # # #         save_investments_data()
    
# # # #     # Save buttons
# # # #     save_btn = tk.Button(button_frame, text="💾 Save", command=save_only,
# # # #                         bg=COLORS['warning'], fg=COLORS['text'], font=("Segoe UI", 10, "bold"),
# # # #                         padx=15, pady=5, relief="flat")
# # # #     save_btn.pack(side="right", padx=5)
    
# # # #     save_close_btn = tk.Button(button_frame, text="💾 Save & Close", command=save_and_close,
# # # #                               bg=COLORS['success'], fg='white', font=("Segoe UI", 10, "bold"),
# # # #                               padx=15, pady=5, relief="flat")
# # # #     save_close_btn.pack(side="right", padx=5)

# # # # # 🖼️ Background Image Functions
# # # # def load_background_image():
# # # #     """Load background image if it exists"""
# # # #     if os.path.exists(BACKGROUND_FILE):
# # # #         try:
# # # #             image = Image.open(BACKGROUND_FILE)
# # # #             image = image.resize((800, 600), Image.Resampling.LANCZOS)
# # # #             return ImageTk.PhotoImage(image)
# # # #         except Exception as e:
# # # #             logging.error(f"Failed to load background image: {e}")
# # # #     return None

# # # # def change_background():
# # # #     """Allow user to select and set background image"""
# # # #     file_path = filedialog.askopenfilename(
# # # #         title="Select Background Image",
# # # #         filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif *.bmp")]
# # # #     )
# # # #     if file_path:
# # # #         try:
# # # #             # Copy the selected image to assets folder
# # # #             image = Image.open(file_path)
# # # #             image.save(BACKGROUND_FILE)
# # # #             messagebox.showinfo("Success", f"Background changed! Restart the app to see changes.\n\nImage saved to: {BACKGROUND_FILE}")
# # # #         except Exception as e:
# # # #             messagebox.showerror("Error", f"Failed to set background: {e}")

# # # # # 🌈 Enhanced UI Setup
# # # # app = tk.Tk()
# # # # app.title("💰 Personal Finance Tracker Pro")
# # # # app.configure(bg=COLORS['background'])
# # # # app.geometry("900x700")

# # # # # Try to load background image
# # # # bg_image = load_background_image()
# # # # if bg_image:
# # # #     bg_label = tk.Label(app, image=bg_image, bg=COLORS['background'])
# # # #     bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# # # # # Main container with semi-transparent background
# # # # main_container = tk.Frame(app, bg=COLORS['background'], relief="raised", bd=2)
# # # # main_container.pack(fill="both", expand=True, padx=20, pady=20)

# # # # # Header
# # # # header_frame = tk.Frame(main_container, bg=COLORS['primary'], height=60)
# # # # header_frame.pack(fill="x", pady=(0, 20))
# # # # header_frame.pack_propagate(False)

# # # # title_label = tk.Label(header_frame, text="💰 Personal Finance Tracker Pro", 
# # # #                       font=("Segoe UI", 18, "bold"), 
# # # #                       bg=COLORS['primary'], fg='white')
# # # # title_label.pack(expand=True)

# # # # # Create notebook for tabs
# # # # notebook = ttk.Notebook(main_container)
# # # # notebook.pack(fill="both", expand=True)

# # # # # Main tab
# # # # main_tab = tk.Frame(notebook, bg=COLORS['background'])
# # # # notebook.add(main_tab, text="💼 Main Calculator")

# # # # # Left panel for inputs
# # # # left_panel = tk.Frame(main_tab, bg=COLORS['surface'], relief="raised", bd=2)
# # # # left_panel.pack(side="left", fill="both", expand=True, padx=(0, 10), pady=10)

# # # # # Income section
# # # # income_frame = tk.LabelFrame(left_panel, text="💰 Income Sources", 
# # # #                            font=("Segoe UI", 12, "bold"),
# # # #                            bg=COLORS['surface'], fg=COLORS['primary'])
# # # # income_frame.pack(fill="x", padx=15, pady=10)

# # # # tk.Label(income_frame, text="Monthly Salary (₹):", 
# # # #          font=("Segoe UI", 10), bg=COLORS['surface']).pack(anchor="w", pady=2)
# # # # entry_salary = tk.Entry(income_frame, font=("Segoe UI", 11), width=20)
# # # # entry_salary.pack(fill="x", padx=5, pady=2)

# # # # tk.Label(income_frame, text="Rental Income (₹):", 
# # # #          font=("Segoe UI", 10), bg=COLORS['surface']).pack(anchor="w", pady=2)
# # # # entry_rent = tk.Entry(income_frame, font=("Segoe UI", 11), width=20)
# # # # entry_rent.pack(fill="x", padx=5, pady=2)

# # # # # Expenses section
# # # # expense_main_frame = tk.LabelFrame(left_panel, text="💸 Monthly Expenses", 
# # # #                                  font=("Segoe UI", 12, "bold"),
# # # #                                  bg=COLORS['surface'], fg=COLORS['primary'])
# # # # expense_main_frame.pack(fill="both", expand=True, padx=15, pady=10)

# # # # expense_frame = tk.Frame(expense_main_frame, bg=COLORS['surface'])
# # # # expense_frame.pack(fill="both", expand=True, padx=10, pady=5)
# # # # expense_entries = []

# # # # def add_expense_field():
# # # #     desc = tk.StringVar()
# # # #     amt = tk.StringVar()
# # # #     frame = tk.Frame(expense_frame, bg=COLORS['background'], relief="flat", bd=1)
# # # #     frame.pack(pady=2, fill='x')
    
# # # #     desc_entry = tk.Entry(frame, textvariable=desc, width=20, font=("Segoe UI", 10))
# # # #     desc_entry.pack(side="left", padx=5, pady=2)
    
# # # #     amt_entry = tk.Entry(frame, textvariable=amt, width=12, font=("Segoe UI", 10))
# # # #     amt_entry.pack(side="right", padx=5, pady=2)
    
# # # #     expense_entries.append((desc, amt))

# # # # # Add initial expense fields
# # # # for _ in range(4):
# # # #     add_expense_field()

# # # # add_expense_btn = tk.Button(expense_main_frame, text="➕ Add More Expenses", 
# # # #                           command=add_expense_field,
# # # #                           bg=COLORS['accent'], fg='white', 
# # # #                           font=("Segoe UI", 10), relief="flat")
# # # # add_expense_btn.pack(pady=10)

# # # # # Button section
# # # # button_frame = tk.Frame(left_panel, bg=COLORS['surface'])
# # # # button_frame.pack(fill="x", padx=15, pady=10)

# # # # calc_btn = tk.Button(button_frame, text="🧮 Calculate & Save", command=calculate,
# # # #                     bg=COLORS['success'], fg='white', 
# # # #                     font=("Segoe UI", 12, "bold"), 
# # # #                     relief="flat", padx=20, pady=8)
# # # # calc_btn.pack(fill="x", pady=5)

# # # # fixed_btn = tk.Button(button_frame, text="🏠 Fixed Expenses Setup", 
# # # #                      command=open_fixed_expense_editor,
# # # #                      bg=COLORS['warning'], fg=COLORS['text'], 
# # # #                      font=("Segoe UI", 10), relief="flat", padx=20, pady=5)
# # # # fixed_btn.pack(fill="x", pady=2)

# # # # invest_btn = tk.Button(button_frame, text="📈 Investment Manager", 
# # # #                       command=open_investment_manager,
# # # #                       bg=COLORS['accent'], fg='white', 
# # # #                       font=("Segoe UI", 10), relief="flat", padx=20, pady=5)
# # # # invest_btn.pack(fill="x", pady=2)

# # # # bg_btn = tk.Button(button_frame, text="🖼️ Change Background", 
# # # #                   command=change_background,
# # # #                   bg=COLORS['secondary'], fg='white', 
# # # #                   font=("Segoe UI", 9), relief="flat", padx=20, pady=3)
# # # # bg_btn.pack(fill="x", pady=2)

# # # # # Right panel for results
# # # # right_panel = tk.Frame(main_tab, bg=COLORS['surface'], relief="raised", bd=2)
# # # # right_panel.pack(side="right", fill="both", expand=True, padx=(10, 0), pady=10)

# # # # # Results section
# # # # result_frame = tk.LabelFrame(right_panel, text="📊 Financial Summary", 
# # # #                            font=("Segoe UI", 12, "bold"),
# # # #                            bg=COLORS['surface'], fg=COLORS['primary'])
# # # # result_frame.pack(fill="x", padx=15, pady=10)

# # # # result = tk.StringVar()
# # # # result_label = tk.Label(result_frame, textvariable=result, 
# # # #                        font=("Segoe UI", 11, "bold"), 
# # # #                        bg=COLORS['surface'], fg=COLORS['success'],
# # # #                        justify="left")
# # # # result_label.pack(pady=10)

# # # # # Chart section
# # # # chart_label_frame = tk.LabelFrame(right_panel, text="📈 Visual Breakdown", 
# # # #                                 font=("Segoe UI", 12, "bold"),
# # # #                                 bg=COLORS['surface'], fg=COLORS['primary'])
# # # # chart_label_frame.pack(fill="both", expand=True, padx=15, pady=10)

# # # # chart_frame = tk.Frame(chart_label_frame, bg=COLORS['surface'])
# # # # chart_frame.pack(fill="both", expand=True, padx=10, pady=10)

# # # # # Add help text at bottom
# # # # help_text = ("💡 Tips: Use Fixed Expenses for recurring payments like EMI, SIP. "
# # # #             "Use Investment Manager to track your investments separately. "
# # # #             "Investments don't reduce your savings calculation!")
# # # # help_label = tk.Label(main_container, text=help_text, 
# # # #                      font=("Segoe UI", 9), 
# # # #                      bg=COLORS['background'], fg=COLORS['text_light'],
# # # #                      wraplength=850, justify="center")
# # # # help_label.pack(pady=10)

# # # # # Instructions for background image
# # # # instructions = f"""
# # # # 🖼️ Background Image Instructions:
# # # # 1. Click 'Change Background' button to select an image
# # # # 2. Or manually place your image at: {BACKGROUND_FILE}
# # # # 3. Restart the app to see the background
# # # # 4. Supported formats: PNG, JPG, JPEG, GIF, BMP
# # # # """
# # # # print(instructions)

# # # # app.mainloop()





# # # # # import tkinter as tk
# # # # # from tkinter import ttk, messagebox, filedialog
# # # # # import csv, os, logging
# # # # # from datetime import datetime
# # # # # import matplotlib.pyplot as plt
# # # # # from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# # # # # from PIL import Image, ImageTk

# # # # # # Directories
# # # # # BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# # # # # DATA_FILE = os.path.join(BASE_DIR, "data", "finances.csv")
# # # # # FIXED_FILE = os.path.join(BASE_DIR, "config", "fixed_expenses.csv")
# # # # # INVESTMENT_FILE = os.path.join(BASE_DIR, "config", "investments.csv")
# # # # # BACKGROUND_FILE = os.path.join(BASE_DIR, "assets", "background.png")
# # # # # os.makedirs(os.path.join(BASE_DIR, "data"), exist_ok=True)
# # # # # os.makedirs(os.path.join(BASE_DIR, "config"), exist_ok=True)
# # # # # os.makedirs(os.path.join(BASE_DIR, "logs"), exist_ok=True)
# # # # # os.makedirs(os.path.join(BASE_DIR, "assets"), exist_ok=True)

# # # # # # Global variables
# # # # # fixed_expense_window = None
# # # # # investment_window = None

# # # # # # Logging
# # # # # logging.basicConfig(
# # # # #     filename=os.path.join(BASE_DIR, "logs", "app.log"),
# # # # #     level=logging.INFO,
# # # # #     format='%(asctime)s - %(levelname)s - %(message)s'
# # # # # )

# # # # # # 🎨 Color scheme
# # # # # COLORS = {
# # # # #     'primary': '#2E3440',
# # # # #     'secondary': '#3B4252',
# # # # #     'accent': '#5E81AC',
# # # # #     'success': '#A3BE8C',
# # # # #     'warning': '#EBCB8B',
# # # # #     'error': '#BF616A',
# # # # #     'background': '#ECEFF4',
# # # # #     'surface': '#E5E9F0',
# # # # #     'text': '#2E3440',
# # # # #     'text_light': '#4C566A'
# # # # # }

# # # # # # 🔁 Load/Save Functions
# # # # # def load_fixed_expenses():
# # # # #     fixed = {}
# # # # #     if os.path.exists(FIXED_FILE):
# # # # #         try:
# # # # #             with open(FIXED_FILE, newline='') as f:
# # # # #                 reader = csv.reader(f)
# # # # #                 next(reader, None)
# # # # #                 for row in reader:
# # # # #                     if len(row) == 2:
# # # # #                         fixed[row[0]] = float(row[1])
# # # # #         except Exception as e:
# # # # #             logging.error(f"Failed to load fixed expenses: {e}")
# # # # #     return fixed

# # # # # def save_fixed_expenses(fixed_dict):
# # # # #     try:
# # # # #         with open(FIXED_FILE, 'w', newline='') as f:
# # # # #             writer = csv.writer(f)
# # # # #             writer.writerow(["Description", "Amount"])
# # # # #             for k, v in fixed_dict.items():
# # # # #                 writer.writerow([k, v])
# # # # #         logging.info("Fixed expenses saved.")
# # # # #     except Exception as e:
# # # # #         logging.error(f"Failed to save fixed expenses: {e}")

# # # # # def load_investments():
# # # # #     investments = {}
# # # # #     if os.path.exists(INVESTMENT_FILE):
# # # # #         try:
# # # # #             with open(INVESTMENT_FILE, newline='') as f:
# # # # #                 reader = csv.reader(f)
# # # # #                 next(reader, None)
# # # # #                 for row in reader:
# # # # #                     if len(row) == 2:
# # # # #                         investments[row[0]] = float(row[1])
# # # # #         except Exception as e:
# # # # #             logging.error(f"Failed to load investments: {e}")
# # # # #     return investments

# # # # # def save_investments(investment_dict):
# # # # #     try:
# # # # #         with open(INVESTMENT_FILE, 'w', newline='') as f:
# # # # #             writer = csv.writer(f)
# # # # #             writer.writerow(["Investment Type", "Amount"])
# # # # #             for k, v in investment_dict.items():
# # # # #                 writer.writerow([k, v])
# # # # #         logging.info("Investments saved.")
# # # # #     except Exception as e:
# # # # #         logging.error(f"Failed to save investments: {e}")

# # # # # # 🧮 Data Saving
# # # # # def save_data(salary, rent, expenses, investments, net_savings):
# # # # #     try:
# # # # #         file_exists = os.path.isfile(DATA_FILE)
# # # # #         with open(DATA_FILE, mode='a', newline='') as file:
# # # # #             writer = csv.writer(file)
# # # # #             if not file_exists:
# # # # #                 writer.writerow(["Date", "Salary", "Rent", "Total Income", "Total Expenses", "Total Investments", "Net Savings"])
# # # # #             today = datetime.now().strftime("%Y-%m-%d")
# # # # #             total_expenses = sum(expenses.values())
# # # # #             total_investments = sum(investments.values())
# # # # #             writer.writerow([today, salary, rent, salary + rent, total_expenses, total_investments, net_savings])
# # # # #         logging.info("Data saved successfully")
# # # # #     except Exception as e:
# # # # #         logging.error(f"Error saving data: {e}")

# # # # # # 📊 Enhanced Pie Chart
# # # # # def show_expense_chart(expenses, investments):
# # # # #     for widget in chart_frame.winfo_children():
# # # # #         widget.destroy()
    
# # # # #     if not expenses and not investments:
# # # # #         no_data_label = tk.Label(chart_frame, text="No data to display", 
# # # # #                                bg=COLORS['background'], fg=COLORS['text_light'],
# # # # #                                font=("Segoe UI", 12))
# # # # #         no_data_label.pack(pady=20)
# # # # #         return
    
# # # # #     # Combine expenses and investments for the chart
# # # # #     all_categories = {}
# # # # #     all_categories.update(expenses)
    
# # # # #     # Add investments with different styling
# # # # #     for inv_name, inv_amount in investments.items():
# # # # #         all_categories[f"💰 {inv_name}"] = inv_amount
    
# # # # #     if all_categories:
# # # # #         categories = list(all_categories.keys())
# # # # #         amounts = list(all_categories.values())
        
# # # # #         # Create a more colorful pie chart
# # # # #         fig, ax = plt.subplots(figsize=(5, 5))
# # # # #         colors = plt.cm.Set3(range(len(categories)))
        
# # # # #         wedges, texts, autotexts = ax.pie(amounts, labels=categories, autopct='%1.1f%%', 
# # # # #                                          startangle=90, colors=colors, 
# # # # #                                          explode=[0.05] * len(categories))
        
# # # # #         ax.set_title("Financial Breakdown", fontsize=14, fontweight='bold', pad=20)
        
# # # # #         # Style the text
# # # # #         for autotext in autotexts:
# # # # #             autotext.set_color('white')
# # # # #             autotext.set_fontweight('bold')
        
# # # # #         plt.tight_layout()
# # # # #         canvas = FigureCanvasTkAgg(fig, master=chart_frame)
# # # # #         canvas.draw()
# # # # #         canvas.get_tk_widget().pack()

# # # # # # 🧠 Enhanced Calculate Logic
# # # # # def calculate():
# # # # #     try:
# # # # #         salary = float(entry_salary.get()) if entry_salary.get() else 0
# # # # #         rent = float(entry_rent.get()) if entry_rent.get() else 0
# # # # #         total_income = salary + rent

# # # # #         # Get regular expenses
# # # # #         expenses = {}
# # # # #         for desc, amt in expense_entries:
# # # # #             if desc.get() and amt.get():
# # # # #                 expenses[desc.get()] = float(amt.get())

# # # # #         # Add fixed expenses
# # # # #         fixed_expenses = load_fixed_expenses()
# # # # #         expenses.update(fixed_expenses)

# # # # #         # Get investments (not deducted from savings)
# # # # #         investments = load_investments()

# # # # #         total_expense = sum(expenses.values())
# # # # #         total_investments = sum(investments.values())
# # # # #         net_savings = total_income - total_expense  # Investments don't reduce savings

# # # # #         # Update result with colorful formatting
# # # # #         result_text = f"💰 Total Income: ₹{total_income:,.2f}\n"
# # # # #         result_text += f"💸 Total Expenses: ₹{total_expense:,.2f}\n"
# # # # #         result_text += f"📈 Total Investments: ₹{total_investments:,.2f}\n"
# # # # #         result_text += f"✅ Net Savings: ₹{net_savings:,.2f}"
        
# # # # #         result.set(result_text)
        
# # # # #         # Color code the savings based on amount
# # # # #         if net_savings > 0:
# # # # #             result_label.config(fg=COLORS['success'])
# # # # #         elif net_savings == 0:
# # # # #             result_label.config(fg=COLORS['warning'])
# # # # #         else:
# # # # #             result_label.config(fg=COLORS['error'])

# # # # #         save_data(salary, rent, expenses, investments, net_savings)
# # # # #         show_expense_chart(expenses, investments)
# # # # #         logging.info("Calculation complete.")

# # # # #     except ValueError:
# # # # #         logging.warning("Invalid numeric input detected.")
# # # # #         messagebox.showerror("Input Error", "Please enter valid numbers.")
# # # # #     except Exception as e:
# # # # #         logging.error(f"Unexpected error: {e}")
# # # # #         messagebox.showerror("Error", str(e))

# # # # # # ⚙️ Fixed Expense Editor
# # # # # def open_fixed_expense_editor():
# # # # #     global fixed_expense_window
    
# # # # #     if fixed_expense_window and tk.Toplevel.winfo_exists(fixed_expense_window):
# # # # #         fixed_expense_window.lift()
# # # # #         fixed_expense_window.focus()
# # # # #         return
    
# # # # #     fixed_expense_window = tk.Toplevel(app)
# # # # #     fixed_expense_window.title("🏠 Fixed Expenses Setup")
# # # # #     fixed_expense_window.configure(bg=COLORS['background'])
# # # # #     fixed_expense_window.geometry("400x300")
    
# # # # #     title_label = tk.Label(fixed_expense_window, text="Fixed Expenses Setup", 
# # # # #                           font=("Segoe UI", 14, "bold"), 
# # # # #                           bg=COLORS['background'], fg=COLORS['primary'])
# # # # #     title_label.pack(pady=10)
    
# # # # #     subtitle_label = tk.Label(fixed_expense_window, text="Enter recurring expenses like EMI, SIPs, etc.", 
# # # # #                              font=("Segoe UI", 10), 
# # # # #                              bg=COLORS['background'], fg=COLORS['text_light'])
# # # # #     subtitle_label.pack(pady=5)
    
# # # # #     entries = []
# # # # #     existing = load_fixed_expenses()
# # # # #     items = list(existing.items()) + [("", "")] * (5 - len(existing))

# # # # #     scroll_frame = tk.Frame(fixed_expense_window, bg=COLORS['background'])
# # # # #     scroll_frame.pack(fill="both", expand=True, padx=20, pady=10)

# # # # #     for i, (desc, val) in enumerate(items):
# # # # #         frame = tk.Frame(scroll_frame, bg=COLORS['surface'], relief="raised", bd=1)
# # # # #         frame.pack(pady=3, fill="x", padx=5)
        
# # # # #         d = tk.StringVar(value=desc)
# # # # #         a = tk.StringVar(value=str(val) if val != "" else "")
        
# # # # #         desc_entry = tk.Entry(frame, textvariable=d, width=25, font=("Segoe UI", 10))
# # # # #         desc_entry.pack(side="left", padx=8, pady=5)
        
# # # # #         amt_entry = tk.Entry(frame, textvariable=a, width=12, font=("Segoe UI", 10))
# # # # #         amt_entry.pack(side="right", padx=8, pady=5)
        
# # # # #         entries.append((d, a))

# # # # #     def save_and_close():
# # # # #         new_fixed = {}
# # # # #         for d, a in entries:
# # # # #             if d.get() and a.get():
# # # # #                 try:
# # # # #                     new_fixed[d.get()] = float(a.get())
# # # # #                 except ValueError:
# # # # #                     messagebox.showerror("Invalid Input", "Please enter numbers only.")
# # # # #                     return
# # # # #         save_fixed_expenses(new_fixed)
# # # # #         messagebox.showinfo("✅ Saved", "Fixed expenses saved successfully!")
# # # # #         fixed_expense_window.destroy()

# # # # #     button_frame = tk.Frame(fixed_expense_window, bg=COLORS['background'])
# # # # #     button_frame.pack(pady=10)
    
# # # # #     save_btn = tk.Button(button_frame, text="💾 Save & Close", command=save_and_close,
# # # # #                         bg=COLORS['success'], fg='white', font=("Segoe UI", 10, "bold"),
# # # # #                         padx=20, pady=5, relief="flat")
# # # # #     save_btn.pack()

# # # # # # 📈 Investment Manager
# # # # # def open_investment_manager():
# # # # #     global investment_window
    
# # # # #     if investment_window and tk.Toplevel.winfo_exists(investment_window):
# # # # #         investment_window.lift()
# # # # #         investment_window.focus()
# # # # #         return
    
# # # # #     investment_window = tk.Toplevel(app)
# # # # #     investment_window.title("📈 Investment Manager")
# # # # #     investment_window.configure(bg=COLORS['background'])
# # # # #     investment_window.geometry("450x350")
    
# # # # #     title_label = tk.Label(investment_window, text="Investment Manager", 
# # # # #                           font=("Segoe UI", 14, "bold"), 
# # # # #                           bg=COLORS['background'], fg=COLORS['primary'])
# # # # #     title_label.pack(pady=10)
    
# # # # #     subtitle_label = tk.Label(investment_window, text="Manage your investments (Bank FD, Mutual Funds, etc.)", 
# # # # #                              font=("Segoe UI", 10), 
# # # # #                              bg=COLORS['background'], fg=COLORS['text_light'])
# # # # #     subtitle_label.pack(pady=5)
    
# # # # #     entries = []
# # # # #     existing = load_investments()
    
# # # # #     # Add Bank FD as default if not present
# # # # #     if "Bank FD" not in existing:
# # # # #         existing["Bank FD"] = 0
    
# # # # #     items = list(existing.items()) + [("", "")] * (6 - len(existing))

# # # # #     scroll_frame = tk.Frame(investment_window, bg=COLORS['background'])
# # # # #     scroll_frame.pack(fill="both", expand=True, padx=20, pady=10)

# # # # #     for i, (desc, val) in enumerate(items):
# # # # #         frame = tk.Frame(scroll_frame, bg=COLORS['surface'], relief="raised", bd=1)
# # # # #         frame.pack(pady=3, fill="x", padx=5)
        
# # # # #         d = tk.StringVar(value=desc)
# # # # #         a = tk.StringVar(value=str(val) if val != "" and val != 0 else "")
        
# # # # #         desc_entry = tk.Entry(frame, textvariable=d, width=25, font=("Segoe UI", 10))
# # # # #         desc_entry.pack(side="left", padx=8, pady=5)
        
# # # # #         amt_entry = tk.Entry(frame, textvariable=a, width=12, font=("Segoe UI", 10))
# # # # #         amt_entry.pack(side="right", padx=8, pady=5)
        
# # # # #         entries.append((d, a))

# # # # #     def save_and_close():
# # # # #         new_investments = {}
# # # # #         for d, a in entries:
# # # # #             if d.get() and a.get():
# # # # #                 try:
# # # # #                     new_investments[d.get()] = float(a.get())
# # # # #                 except ValueError:
# # # # #                     messagebox.showerror("Invalid Input", "Please enter numbers only.")
# # # # #                     return
# # # # #         save_investments(new_investments)
# # # # #         messagebox.showinfo("✅ Saved", "Investments saved successfully!")
# # # # #         investment_window.destroy()

# # # # #     button_frame = tk.Frame(investment_window, bg=COLORS['background'])
# # # # #     button_frame.pack(pady=10)
    
# # # # #     save_btn = tk.Button(button_frame, text="💾 Save & Close", command=save_and_close,
# # # # #                         bg=COLORS['accent'], fg='white', font=("Segoe UI", 10, "bold"),
# # # # #                         padx=20, pady=5, relief="flat")
# # # # #     save_btn.pack()

# # # # # # 🖼️ Background Image Functions
# # # # # def load_background_image():
# # # # #     """Load background image if it exists"""
# # # # #     if os.path.exists(BACKGROUND_FILE):
# # # # #         try:
# # # # #             image = Image.open(BACKGROUND_FILE)
# # # # #             image = image.resize((800, 600), Image.Resampling.LANCZOS)
# # # # #             return ImageTk.PhotoImage(image)
# # # # #         except Exception as e:
# # # # #             logging.error(f"Failed to load background image: {e}")
# # # # #     return None

# # # # # def change_background():
# # # # #     """Allow user to select and set background image"""
# # # # #     file_path = filedialog.askopenfilename(
# # # # #         title="Select Background Image",
# # # # #         filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif *.bmp")]
# # # # #     )
# # # # #     if file_path:
# # # # #         try:
# # # # #             # Copy the selected image to assets folder
# # # # #             image = Image.open(file_path)
# # # # #             image.save(BACKGROUND_FILE)
# # # # #             messagebox.showinfo("Success", f"Background changed! Restart the app to see changes.\n\nImage saved to: {BACKGROUND_FILE}")
# # # # #         except Exception as e:
# # # # #             messagebox.showerror("Error", f"Failed to set background: {e}")

# # # # # # 🌈 Enhanced UI Setup
# # # # # app = tk.Tk()
# # # # # app.title("💰 Personal Finance Tracker Pro")
# # # # # app.configure(bg=COLORS['background'])
# # # # # app.geometry("900x700")

# # # # # # Try to load background image
# # # # # bg_image = load_background_image()
# # # # # if bg_image:
# # # # #     bg_label = tk.Label(app, image=bg_image, bg=COLORS['background'])
# # # # #     bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# # # # # # Main container with semi-transparent background
# # # # # main_container = tk.Frame(app, bg=COLORS['background'], relief="raised", bd=2)
# # # # # main_container.pack(fill="both", expand=True, padx=20, pady=20)

# # # # # # Header
# # # # # header_frame = tk.Frame(main_container, bg=COLORS['primary'], height=60)
# # # # # header_frame.pack(fill="x", pady=(0, 20))
# # # # # header_frame.pack_propagate(False)

# # # # # title_label = tk.Label(header_frame, text="💰 Personal Finance Tracker Pro", 
# # # # #                       font=("Segoe UI", 18, "bold"), 
# # # # #                       bg=COLORS['primary'], fg='white')
# # # # # title_label.pack(expand=True)

# # # # # # Create notebook for tabs
# # # # # notebook = ttk.Notebook(main_container)
# # # # # notebook.pack(fill="both", expand=True)

# # # # # # Main tab
# # # # # main_tab = tk.Frame(notebook, bg=COLORS['background'])
# # # # # notebook.add(main_tab, text="💼 Main Calculator")

# # # # # # Left panel for inputs
# # # # # left_panel = tk.Frame(main_tab, bg=COLORS['surface'], relief="raised", bd=2)
# # # # # left_panel.pack(side="left", fill="both", expand=True, padx=(0, 10), pady=10)

# # # # # # Income section
# # # # # income_frame = tk.LabelFrame(left_panel, text="💰 Income Sources", 
# # # # #                            font=("Segoe UI", 12, "bold"),
# # # # #                            bg=COLORS['surface'], fg=COLORS['primary'])
# # # # # income_frame.pack(fill="x", padx=15, pady=10)

# # # # # tk.Label(income_frame, text="Monthly Salary (₹):", 
# # # # #          font=("Segoe UI", 10), bg=COLORS['surface']).pack(anchor="w", pady=2)
# # # # # entry_salary = tk.Entry(income_frame, font=("Segoe UI", 11), width=20)
# # # # # entry_salary.pack(fill="x", padx=5, pady=2)

# # # # # tk.Label(income_frame, text="Rental Income (₹):", 
# # # # #          font=("Segoe UI", 10), bg=COLORS['surface']).pack(anchor="w", pady=2)
# # # # # entry_rent = tk.Entry(income_frame, font=("Segoe UI", 11), width=20)
# # # # # entry_rent.pack(fill="x", padx=5, pady=2)

# # # # # # Expenses section
# # # # # expense_main_frame = tk.LabelFrame(left_panel, text="💸 Monthly Expenses", 
# # # # #                                  font=("Segoe UI", 12, "bold"),
# # # # #                                  bg=COLORS['surface'], fg=COLORS['primary'])
# # # # # expense_main_frame.pack(fill="both", expand=True, padx=15, pady=10)

# # # # # expense_frame = tk.Frame(expense_main_frame, bg=COLORS['surface'])
# # # # # expense_frame.pack(fill="both", expand=True, padx=10, pady=5)
# # # # # expense_entries = []

# # # # # def add_expense_field():
# # # # #     desc = tk.StringVar()
# # # # #     amt = tk.StringVar()
# # # # #     frame = tk.Frame(expense_frame, bg=COLORS['background'], relief="flat", bd=1)
# # # # #     frame.pack(pady=2, fill='x')
    
# # # # #     desc_entry = tk.Entry(frame, textvariable=desc, width=20, font=("Segoe UI", 10))
# # # # #     desc_entry.pack(side="left", padx=5, pady=2)
    
# # # # #     amt_entry = tk.Entry(frame, textvariable=amt, width=12, font=("Segoe UI", 10))
# # # # #     amt_entry.pack(side="right", padx=5, pady=2)
    
# # # # #     expense_entries.append((desc, amt))

# # # # # # Add initial expense fields
# # # # # for _ in range(4):
# # # # #     add_expense_field()

# # # # # add_expense_btn = tk.Button(expense_main_frame, text="➕ Add More Expenses", 
# # # # #                           command=add_expense_field,
# # # # #                           bg=COLORS['accent'], fg='white', 
# # # # #                           font=("Segoe UI", 10), relief="flat")
# # # # # add_expense_btn.pack(pady=10)

# # # # # # Button section
# # # # # button_frame = tk.Frame(left_panel, bg=COLORS['surface'])
# # # # # button_frame.pack(fill="x", padx=15, pady=10)

# # # # # calc_btn = tk.Button(button_frame, text="🧮 Calculate & Save", command=calculate,
# # # # #                     bg=COLORS['success'], fg='white', 
# # # # #                     font=("Segoe UI", 12, "bold"), 
# # # # #                     relief="flat", padx=20, pady=8)
# # # # # calc_btn.pack(fill="x", pady=5)

# # # # # fixed_btn = tk.Button(button_frame, text="🏠 Fixed Expenses Setup", 
# # # # #                      command=open_fixed_expense_editor,
# # # # #                      bg=COLORS['warning'], fg=COLORS['text'], 
# # # # #                      font=("Segoe UI", 10), relief="flat", padx=20, pady=5)
# # # # # fixed_btn.pack(fill="x", pady=2)

# # # # # invest_btn = tk.Button(button_frame, text="📈 Investment Manager", 
# # # # #                       command=open_investment_manager,
# # # # #                       bg=COLORS['accent'], fg='white', 
# # # # #                       font=("Segoe UI", 10), relief="flat", padx=20, pady=5)
# # # # # invest_btn.pack(fill="x", pady=2)

# # # # # bg_btn = tk.Button(button_frame, text="🖼️ Change Background", 
# # # # #                   command=change_background,
# # # # #                   bg=COLORS['secondary'], fg='white', 
# # # # #                   font=("Segoe UI", 9), relief="flat", padx=20, pady=3)
# # # # # bg_btn.pack(fill="x", pady=2)

# # # # # # Right panel for results
# # # # # right_panel = tk.Frame(main_tab, bg=COLORS['surface'], relief="raised", bd=2)
# # # # # right_panel.pack(side="right", fill="both", expand=True, padx=(10, 0), pady=10)

# # # # # # Results section
# # # # # result_frame = tk.LabelFrame(right_panel, text="📊 Financial Summary", 
# # # # #                            font=("Segoe UI", 12, "bold"),
# # # # #                            bg=COLORS['surface'], fg=COLORS['primary'])
# # # # # result_frame.pack(fill="x", padx=15, pady=10)

# # # # # result = tk.StringVar()
# # # # # result_label = tk.Label(result_frame, textvariable=result, 
# # # # #                        font=("Segoe UI", 11, "bold"), 
# # # # #                        bg=COLORS['surface'], fg=COLORS['success'],
# # # # #                        justify="left")
# # # # # result_label.pack(pady=10)

# # # # # # Chart section
# # # # # chart_label_frame = tk.LabelFrame(right_panel, text="📈 Visual Breakdown", 
# # # # #                                 font=("Segoe UI", 12, "bold"),
# # # # #                                 bg=COLORS['surface'], fg=COLORS['primary'])
# # # # # chart_label_frame.pack(fill="both", expand=True, padx=15, pady=10)

# # # # # chart_frame = tk.Frame(chart_label_frame, bg=COLORS['surface'])
# # # # # chart_frame.pack(fill="both", expand=True, padx=10, pady=10)

# # # # # # Add help text at bottom
# # # # # help_text = ("💡 Tips: Use Fixed Expenses for recurring payments like EMI, SIP. "
# # # # #             "Use Investment Manager to track your investments separately. "
# # # # #             "Investments don't reduce your savings calculation!")
# # # # # help_label = tk.Label(main_container, text=help_text, 
# # # # #                      font=("Segoe UI", 9), 
# # # # #                      bg=COLORS['background'], fg=COLORS['text_light'],
# # # # #                      wraplength=850, justify="center")
# # # # # help_label.pack(pady=10)

# # # # # # Instructions for background image
# # # # # instructions = f"""
# # # # # 🖼️ Background Image Instructions:
# # # # # 1. Click 'Change Background' button to select an image
# # # # # 2. Or manually place your image at: {BACKGROUND_FILE}
# # # # # 3. Restart the app to see the background
# # # # # 4. Supported formats: PNG, JPG, JPEG, GIF, BMP
# # # # # """
# # # # # print(instructions)

# # # # # app.mainloop()


import tkinter as tk
from tkinter import ttk, messagebox, filedialog, simpledialog
import os

# Import all your functions and variables from your existing code here
# For this example, I'm assuming everything you shared above is in the same script file

# ⬇️ Setup main app window
app = tk.Tk()
app.title("💰 Personal Finance Tracker")
app.geometry("1000x700")
app.configure(bg=COLORS['background'])

# 🧱 Main Container
main_container = tk.Frame(app, bg=COLORS['background'])
main_container.pack(fill="both", expand=True, padx=20, pady=20)

# 👤 User Info
user_label = tk.Label(main_container, text="👤 No User Selected", font=("Segoe UI", 11, "bold"),
                      bg=COLORS['background'], fg=COLORS['primary'])
user_label.pack(anchor="ne")

# 📝 Entry Form
form_frame = tk.Frame(main_container, bg=COLORS['background'])
form_frame.pack(fill="x", pady=10)

# Salary Input
salary_label = tk.Label(form_frame, text="Salary (₹):", font=("Segoe UI", 10),
                        bg=COLORS['background'])
salary_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
entry_salary = tk.Entry(form_frame, width=20)
entry_salary.grid(row=0, column=1, padx=5, pady=5)

# Rent Input
rent_label = tk.Label(form_frame, text="Rent Income (₹):", font=("Segoe UI", 10),
                      bg=COLORS['background'])
rent_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
entry_rent = tk.Entry(form_frame, width=20)
entry_rent.grid(row=1, column=1, padx=5, pady=5)

# 📋 Expense Inputs
expense_label = tk.Label(form_frame, text="Monthly Expenses:", font=("Segoe UI", 10, "bold"),
                         bg=COLORS['background'])
expense_label.grid(row=2, column=0, columnspan=2, pady=(15, 5), sticky="w")

expense_entries = []
for i in range(5):
    desc = tk.StringVar()
    amt = tk.StringVar()
    desc_entry = tk.Entry(form_frame, textvariable=desc, width=30)
    amt_entry = tk.Entry(form_frame, textvariable=amt, width=15)
    desc_entry.grid(row=3+i, column=0, padx=5, pady=2)
    amt_entry.grid(row=3+i, column=1, padx=5, pady=2)
    expense_entries.append((desc, amt))

# 🧮 Result Label
result = tk.StringVar()
result_label = tk.Label(main_container, textvariable=result, font=("Segoe UI", 11, "bold"),
                        bg=COLORS['background'], justify="left")
result_label.pack(pady=15)

# 📈 Chart Frame
chart_frame = tk.Frame(main_container, bg=COLORS['background'])
chart_frame.pack(fill="both", expand=True)

# 🔘 Buttons
button_frame = tk.Frame(main_container, bg=COLORS['background'])
button_frame.pack(pady=10)

btn_calc = tk.Button(button_frame, text="🧮 Calculate", command=calculate,
                     bg=COLORS['success'], fg='white', padx=15, pady=5)
btn_calc.grid(row=0, column=0, padx=5)

btn_fixed = tk.Button(button_frame, text="🏠 Fixed Expenses", command=open_fixed_expense_editor,
                      bg=COLORS['warning'], fg='black', padx=15, pady=5)
btn_fixed.grid(row=0, column=1, padx=5)

btn_inv = tk.Button(button_frame, text="📈 Investments", command=open_investment_manager,
                    bg=COLORS['accent'], fg='white', padx=15, pady=5)
btn_inv.grid(row=0, column=2, padx=5)

btn_bg = tk.Button(button_frame, text="🖼️ Change Background", command=change_background,
                   bg=COLORS['primary'], fg='white', padx=15, pady=5)
btn_bg.grid(row=0, column=3, padx=5)

btn_user = tk.Button(button_frame, text="👤 Select User", command=show_user_selection,
                     bg=COLORS['secondary'], fg='white', padx=15, pady=5)
btn_user.grid(row=0, column=4, padx=5)

# 🚀 Start
apply_background()
show_user_selection()
app.mainloop()
