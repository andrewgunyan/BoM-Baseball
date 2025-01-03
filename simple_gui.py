import tkinter as tk
import main


def display_verse():
    global book, chapter
    random_url, book, chapter = main.generate_random_verse()
    main.scrape(random_url)
    verse = main.parse()
    label.config(text=verse)
    answer.config(text="Reference")

def display_reference():
    name = convert_reference(book)
    answer.config(text=f"{name} {chapter}")

def convert_reference(book):
    names = { 
        "1-ne": "1 Nephi",
        "2-ne": "2 Nephi",
        "jacob": "Jacob",
        "enos": "Enos",
        "jarom": "Jarom",
        "omni": "Omni",
        "w-of-m": "Words of Mormon",
        "mosiah": "Mosiah",
        "alma": "Alma",
        "hel": "Helaman",
        "3-ne": "3 Nephi",
        "4-ne": "4 Nephi",
        "morm": "Mormon",
    }

    return names[book]


book = ""
chapter = 0

window = tk.Tk()
window.title("Scripture Verse Generator")

label = tk.Label(window, text="Enter your name:", font=("Arial", 14), wraplength=500)
label.pack(padx=20, pady=20)

answer = tk.Label(window, font=("Arial", 12))
answer.pack(padx=20, pady=10)

# Create a frame to hold both buttons
button_frame = tk.Frame(window)
button_frame.pack(pady=10)

# First button (Greet)
button_generate = tk.Button(button_frame, text="Generate Scripture", command=display_verse, font=("Arial", 12))
button_generate.pack(side="left", padx=10)

# Second button (New Button)
button_answer = tk.Button(button_frame, text="Show Reference", command=display_reference, font=("Arial", 12))
button_answer.pack(side="left", padx=10)

window.mainloop()

