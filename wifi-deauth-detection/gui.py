import tkinter as tk
from queue import Queue

# global queue (detector → GUI)
gui_queue = Queue()

def update_gui(root, status_label, text_box):
    while not gui_queue.empty():
        data = gui_queue.get()

        status_label.config(text="🚨 DEAUTH ATTACK DETECTED 🚨")

        text_box.config(state="normal")
        text_box.delete("1.0", tk.END)
        text_box.insert(tk.END, data)
        text_box.config(state="disabled")

    root.after(500, update_gui, root, status_label, text_box)

def start_gui():
    root = tk.Tk()
    root.title("WiFi Deauth Detection System")
    root.geometry("650x450")

    status_label = tk.Label(
        root,
        text="🟢 Monitoring WiFi Network...",
        font=("Arial", 14, "bold"),
        fg="green"
    )
    status_label.pack(pady=10)

    text_box = tk.Text(
        root,
        height=20,
        width=80,
        state="disabled",
        wrap="word"
    )
    text_box.pack(padx=10, pady=10)

    update_gui(root, status_label, text_box)
    root.mainloop()
