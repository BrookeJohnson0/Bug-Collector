import tkinter as tk
from tkinter import messagebox

class BugCollectorTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Bug Collector")
        self.root.geometry("350x400")
        self.root.configure(bg="#87ceeb")  # Light pink background

        self.entries = {}

        # Title
        tk.Label(self.root, text="Enter Bugs Collected Each Day", bg="#87ceeb", font=("Arial", 14, "bold")).pack(pady=10)

        # Input fields for counting
        for i in range(1, 6):
            frame = tk.Frame(self.root, bg="#87ceeb")
            frame.pack(pady=5)
            tk.Label(frame, text=f"Day {i}:", bg="#87ceeb", font=("Arial", 11)).pack(side="left")
            entry = tk.Entry(frame, width=10)
            entry.pack(side="left")
            self.entries[f"day{i}"] = entry

        # Button to calculate total
        tk.Button(self.root, text="Calculate Total", command=self.calculate_total, bg="#ff99cc", fg="white").pack(pady=20)

        # Result label
        self.result_label = tk.Label(self.root, text="", bg="#87ceeb", font=("Arial", 12, "bold"))
        self.result_label.pack(pady=10)

    def calculate_total(self):
        try:
            total = 0
            for i in range(1, 6):
                val = int(self.entries[f"day{i}"].get())
                if val < 0:
                    raise ValueError
                total += val
            self.result_label.config(text=f"Total bugs collected: {total}")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter non-negative integers for all days.")

if __name__ == "__main__":
    root = tk.Tk()
    app = BugCollectorTracker(root)
    root.mainloop()
