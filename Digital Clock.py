import tkinter as tk
from time import strftime
import time

# ---------------- WINDOW ---------------- #

root = tk.Tk()
root.title("Premium Glass Clock & Stopwatch")
root.geometry("900x600")
root.configure(bg="#0b1120")
root.resizable(False, False)

# ---------------- CLOCK ---------------- #

def update_clock():
    current_time = strftime("%H:%M:%S %p")
    current_date = strftime("%A, %d %B %Y")

    clock_label.config(text=current_time)
    date_label.config(text=current_date)

    clock_label.after(1000, update_clock)

# ---------------- MAIN GLASS FRAME ---------------- #

main_frame = tk.Frame(
    root,
    bg="#111827",
    padx=30,
    pady=30,
    bd=0
)

main_frame.place(relx=0.5, rely=0.5, anchor="center")

# ---------------- DIGITAL CLOCK ---------------- #

title = tk.Label(
    main_frame,
    text="DIGITAL CLOCK",
    font=("Segoe UI", 18, "bold"),
    bg="#111827",
    fg="#94a3b8"
)
title.pack(pady=(0, 10))

clock_label = tk.Label(
    main_frame,
    font=("Segoe UI", 42, "bold"),
    bg="#111827",
    fg="#38bdf8"
)
clock_label.pack()

date_label = tk.Label(
    main_frame,
    font=("Segoe UI", 16),
    bg="#111827",
    fg="#cbd5e1"
)
date_label.pack(pady=(5, 30))

# ---------------- STOPWATCH ---------------- #

stopwatch_title = tk.Label(
    main_frame,
    text="STOPWATCH",
    font=("Segoe UI", 18, "bold"),
    bg="#111827",
    fg="#94a3b8"
)
stopwatch_title.pack(pady=(10, 10))

stopwatch_label = tk.Label(
    main_frame,
    text="00:00:00:000",
    font=("Consolas", 40, "bold"),
    bg="#111827",
    fg="#22c55e"
)
stopwatch_label.pack(pady=15)

running = False
start_time = 0
elapsed_time = 0

# ---------------- STOPWATCH FUNCTIONS ---------------- #

def update_stopwatch():
    global elapsed_time

    if running:
        elapsed_time = time.time() - start_time

        hours = int(elapsed_time // 3600)
        minutes = int((elapsed_time % 3600) // 60)
        seconds = int(elapsed_time % 60)
        milliseconds = int((elapsed_time * 1000) % 1000)

        time_text = f"{hours:02}:{minutes:02}:{seconds:02}:{milliseconds:03}"

        stopwatch_label.config(text=time_text)

    root.after(10, update_stopwatch)

def start():
    global running, start_time

    if not running:
        start_time = time.time() - elapsed_time
        running = True

def stop():
    global running
    running = False

def reset():
    global running, start_time, elapsed_time

    running = False
    start_time = 0
    elapsed_time = 0

    stopwatch_label.config(text="00:00:00:000")

# ---------------- BUTTONS ---------------- #

button_frame = tk.Frame(main_frame, bg="#111827")
button_frame.pack(pady=20)

button_style = {
    "font": ("Segoe UI", 12, "bold"),
    "width": 12,
    "height": 1,
    "bd": 0,
    "cursor": "hand2",
    "pady": 10
}

start_btn = tk.Button(
    button_frame,
    text="▶ START",
    command=start,
    bg="#22c55e",
    fg="white",
    activebackground="#16a34a",
    **button_style
)

start_btn.grid(row=0, column=0, padx=12)

stop_btn = tk.Button(
    button_frame,
    text="⏸ STOP",
    command=stop,
    bg="#ef4444",
    fg="white",
    activebackground="#dc2626",
    **button_style
)

stop_btn.grid(row=0, column=1, padx=12)

reset_btn = tk.Button(
    button_frame,
    text="↺ RESET",
    command=reset,
    bg="#3b82f6",
    fg="white",
    activebackground="#2563eb",
    **button_style
)

reset_btn.grid(row=0, column=2, padx=12)

# ---------------- START FUNCTIONS ---------------- #

update_clock()
update_stopwatch()

root.mainloop()