import tkinter as tk
import random
import time


class SortingVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Bubble Sort Visualizer")

        self.canvas = tk.Canvas(self.root, width=850, height=450, bg="white")
        self.canvas.pack()

        self.num_elements = 30
        self.bar_width = 800 // self.num_elements
        self.bars = []
        self.data = []

        self.create_ui()
        self.generate_data()

    def create_ui(self):
        frame = tk.Frame(self.root)
        frame.pack()

        tk.Button(frame, text="Start Bubble Sort", command=self.start_bubble_sort).pack(side=tk.LEFT, padx=10)
        tk.Button(frame, text="Generate New Data", command=self.generate_data).pack(side=tk.LEFT, padx=10)

        self.speed_var = tk.DoubleVar(value=0.1)
        tk.Scale(frame, from_=0.01, to=1.0, resolution=0.01, orient=tk.HORIZONTAL, label="Speed",
                 variable=self.speed_var).pack(side=tk.LEFT, padx=10)

    def generate_data(self):
        self.canvas.delete("all")
        self.data = [random.randint(10, 390) for _ in range(self.num_elements)]
        self.bars = [
            self.canvas.create_rectangle(i * self.bar_width, 400 - h, (i + 1) * self.bar_width, 400, fill="blue")
            for i, h in enumerate(self.data)
        ]

    def start_bubble_sort(self):
        self.bubble_sort()

    def bubble_sort(self):
        n = len(self.data)
        for i in range(n):
            for j in range(0, n - i - 1):
                self.update_visuals(j, j + 1, comparing=True)
                if self.data[j] > self.data[j + 1]:
                    self.data[j], self.data[j + 1] = self.data[j + 1], self.data[j]
                    self.update_visuals(j, j + 1, swapping=True)
                time.sleep(self.speed_var.get())

        self.update_visuals(final=True)

    def update_visuals(self, idx1=None, idx2=None, comparing=False, swapping=False, final=False):
        for i, bar in enumerate(self.bars):
            color = "green" if final else "orange"
            if comparing and (i == idx1 or i == idx2):
                color = "yellow"
            if swapping and (i == idx1 or i == idx2):
                color = "red"
            self.canvas.itemconfig(bar, fill=color)
            self.canvas.coords(bar, i * self.bar_width, 400 - self.data[i], (i + 1) * self.bar_width, 400)

        self.root.update_idletasks()


if __name__ == "__main__":
    root = tk.Tk()
    app = SortingVisualizer(root)
    root.mainloop()
