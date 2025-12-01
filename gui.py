import requests
import threading
import time
from datetime import datetime, timedelta
from tkinter import *
from tkinter.scrolledtext import ScrolledText

# ======================
# CONFIG
# ======================

# Replace with PC #1 LAN IP
# Example: "http://192.168.1.50:5000/fetch"
SERVER_FETCH_URL = "http://192.168.4.48:5000/fetch"

FETCH_DELAY = 3  # seconds between server polls

# ======================
# GUI
# ======================

root = Tk()
root.title("Screen Live Receiver + Time Search + Highlight")
root.geometry("950x700")

top_frame = Frame(root)
top_frame.pack(pady=5)

Label(top_frame, text="Search:", font=("Segoe UI", 11)).grid(row=0, column=0, padx=5)
search_entry = Entry(top_frame, font=("Segoe UI", 11), width=30)
search_entry.grid(row=0, column=1, padx=5)

Label(top_frame, text="Time Range:", font=("Segoe UI", 11)).grid(row=0, column=2, padx=5)

time_range_var = StringVar(value="All")
time_range_options = ["All", "Today", "Yesterday", "Last 1 Hour", "Last 24 Hours"]
time_range_menu = OptionMenu(top_frame, time_range_var, *time_range_options)
time_range_menu.grid(row=0, column=3, padx=5)

search_button = Button(top_frame, text="Search", font=("Segoe UI", 10, "bold"),
                       bg="#2b90d9", fg="white")
search_button.grid(row=0, column=4, padx=5)

clear_button = Button(top_frame, text="Clear", font=("Segoe UI", 10),
                      bg="#555", fg="white")
clear_button.grid(row=0, column=5, padx=5)

text_box = ScrolledText(root, font=("Segoe UI", 11), wrap=WORD)
text_box.pack(expand=True, fill=BOTH, padx=10, pady=10)

text_box.tag_configure("highlight", background="yellow", foreground="black")

all_messages = []  # list of {"time": ..., "msg": ...}
last_count = 0
lock = threading.Lock()

# ======================
# HELPERS
# ======================

def parse_time(ts: str):
    try:
        return datetime.fromisoformat(ts)
    except Exception:
        return None


def filter_by_time(messages, range_name: str):
    if range_name == "All":
        return messages

    now = datetime.now()
    filtered = []

    for item in messages:
        dt = parse_time(item["time"])
        if not dt:
            continue

        if range_name == "Today":
            if dt.date() == now.date():
                filtered.append(item)

        elif range_name == "Yesterday":
            if dt.date() == (now.date() - timedelta(days=1)):
                filtered.append(item)

        elif range_name == "Last 1 Hour":
            if dt >= now - timedelta(hours=1):
                filtered.append(item)

        elif range_name == "Last 24 Hours":
            if dt >= now - timedelta(hours=24):
                filtered.append(item)

    return filtered


def render_messages(msgs, keyword=None):
    text_box.delete("1.0", END)

    keyword = (keyword or "").strip()
    keyword_lower = keyword.lower()

    for item in msgs:
        line = f"[{item['time']}] {item['msg']}\n"
        text_box.insert(END, line)

    # Highlight keyword if present
    if keyword:
        start = "1.0"
        while True:
            pos = text_box.search(keyword_lower, start, stopindex=END, nocase=1)
            if not pos:
                break
            end = f"{pos}+{len(keyword)}c"
            text_box.tag_add("highlight", pos, end)
            start = end


# ======================
# FETCH LOOP
# ======================

def fetch_loop():
    global all_messages, last_count
    while True:
        try:
            r = requests.get(SERVER_FETCH_URL, timeout=3)
            data = r.json()

            if isinstance(data, list):
                with lock:
                    all_messages = data
                    last_count = len(all_messages)
        except Exception as e:
            # print("[RECEIVER ERROR]", e)
            pass

        time.sleep(FETCH_DELAY)


def refresh_display_if_no_search():
    """
    Periodically refresh display when not in search mode.
    """
    # If search box is empty and time filter is 'All', show everything live
    if not search_entry.get().strip():
        with lock:
            msgs = filter_by_time(all_messages, time_range_var.get())
        render_messages(msgs)

    root.after(2000, refresh_display_if_no_search)


# ======================
# BUTTON ACTIONS
# ======================

def on_search():
    keyword = search_entry.get().strip()
    range_name = time_range_var.get()

    with lock:
        msgs = filter_by_time(all_messages, range_name)

    if keyword:
        msgs = [m for m in msgs if keyword.lower() in m["msg"].lower()]

    render_messages(msgs, keyword=keyword)


def on_clear():
    search_entry.delete(0, END)
    time_range_var.set("All")
    with lock:
        msgs = all_messages[:]
    render_messages(msgs)


search_button.config(command=on_search)
clear_button.config(command=on_clear)

# ======================
# START THREADS
# ======================

threading.Thread(target=fetch_loop, daemon=True).start()
root.after(1000, refresh_display_if_no_search)

root.mainloop()
