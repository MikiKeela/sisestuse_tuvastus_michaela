import tkinter as tk
from app.gui import AppGUI


def main():
    root = tk.Tk()
    AppGUI(root)
    root.minsize(520, 420)
    root.mainloop()

if __name__ == "__main__":
    main()
