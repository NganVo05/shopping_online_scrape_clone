import tkinter as tk
from main import shopping_online_run

def print_input_value():
    location = e1.get()
    keyword = e2.get()
    keyword1 = e3.get()
    keyword2 = e4.get()
    keyword3 = e5.get()
    page = e6.get()
    root.destroy()
    shopping_online_run(location, keyword, keyword1, keyword2, keyword3, page)

# Create the main tkinter window
root = tk.Tk()
root.title("Shopping Online Info")
root.geometry("600x300")

tk.Label(root, text='Location: ', padx=100,pady=10).grid(row=0)
tk.Label(root, text='Keyword: ', padx=100, pady=10).grid(row=1)
tk.Label(root, text='Keyword1: ', padx=100, pady=10).grid(row=2)
tk.Label(root, text='Keyword2: ', padx=100, pady=10).grid(row=3)
tk.Label(root, text='Keyword3: ', padx=100, pady=10).grid(row=4)
tk.Label(root, text='Page: ', padx=100, pady=10).grid(row=5)

e1 = tk.Entry(root)
e2 = tk.Entry(root)
e3 = tk.Entry(root)
e4 = tk.Entry(root)
e5 = tk.Entry(root)
e6 = tk.Entry(root)

# Set default values for entries
e1.insert(0, "fahasa")
e2.insert(0, "sach-trong-nuoc")
e3.insert(0, "thieu-nhi")
e4.insert(0, "truyen-thieu-nhi")
e5.insert(0, "truyen-tranh-thieu-nhi")
e6.insert(0, "1")

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)
e5.grid(row=4, column=1)
e6.grid(row=5, column=1)

# Create a button to trigger printing the input value
print_button = tk.Button(root, text="Print Input Value", command=print_input_value)
print_button.grid(row=6, column=1)

# Start the tkinter main loop
root.mainloop()