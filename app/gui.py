import tkinter as tk
from tkinter import ttk

from classes.input_analyser import InputAnalyzer


class AppGUI:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Sisestuse tuvastus")

        self.analyzer = InputAnalyzer()

        self._build_ui()

    def _build_ui(self):
        main = ttk.Frame(self.root, padding=12)
        main.grid(row=0, column=0, sticky="nsew")

        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        main.columnconfigure(0, weight=1)
        main.rowconfigure(3, weight=1)

        self.label = ttk.Label(main, text="Sisesta väärtus:")
        self.label.grid(row=0, column=0, sticky="w")

        self.entry = ttk.Entry(main)
        self.entry.grid(row=1, column=0, sticky="ew", pady=(6, 10))
        self.entry.focus_set()

        btn_frame = ttk.Frame(main)
        btn_frame.grid(row=2, column=0, sticky="w", pady=(0, 10))

        self.btn_show = ttk.Button(btn_frame, text="Näita", command=self.on_show)
        self.btn_show.grid(row=0, column=0, padx=(0, 8))

        self.btn_clear = ttk.Button(btn_frame, text="Puhasta", command=self.on_clear)
        self.btn_clear.grid(row=0, column=1)

        self.text = tk.Text(main, height=18, wrap="word")
        self.text.grid(row=3, column=0, sticky="nsew")

        self._set_text_readonly(True)

        self.root.bind("<Return>", lambda event: self.on_show())

    def _set_text_readonly(self, readonly: bool):
        self.text.configure(state="disabled" if readonly else "normal")

    def _write_text(self, content: str):
        self._set_text_readonly(False)
        self.text.delete("1.0", tk.END)
        self.text.insert(tk.END, content)
        self._set_text_readonly(True)

    def on_show(self):
        user_input = self.entry.get()

        result = self.analyzer.analyze(user_input)
        self._write_text(result)

        self.entry.delete(0, tk.END)
        self.entry.focus_set()

    def on_clear(self):
        self.entry.delete(0, tk.END)
        self._write_text("")
        self.entry.focus_set()
