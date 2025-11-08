import tkinter as tk
from tkinter import ttk, messagebox
import json
import os
import threading
import pyperclip
try:
    import keyboard  # 需安装 keyboard 库
except ImportError:
    keyboard = None

# 模板文件路径
TEMPLATE_PATH = os.path.join(os.path.dirname(__file__), 'templates', 'prompt_templates.json')

class PromptToolApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Prompt Tool')
        self.geometry('400x200')
        self.templates = self.load_templates()
        self.create_widgets()

    def load_templates(self):
        if not os.path.exists(TEMPLATE_PATH):
            return {}
        with open(TEMPLATE_PATH, 'r', encoding='utf-8') as f:
            return json.load(f)

    def create_widgets(self):
        tk.Label(self, text='选择模板:').pack(pady=10)
        self.template_var = tk.StringVar()
        self.combo = ttk.Combobox(self, textvariable=self.template_var, state='readonly')
        self.combo['values'] = list(self.templates.keys())
        self.combo.pack(pady=5)
        self.combo.bind('<<ComboboxSelected>>', self.on_select)

        self.prompt_text = tk.Text(self, height=5)
        self.prompt_text.pack(pady=5)

        tk.Button(self, text='复制到剪贴板', command=self.copy_to_clipboard).pack(pady=5)

    def on_select(self, event=None):
        key = self.template_var.get()
        prompt = self.templates.get(key, '')
        self.prompt_text.delete('1.0', tk.END)
        self.prompt_text.insert(tk.END, prompt)

    def copy_to_clipboard(self):
        text = self.prompt_text.get('1.0', tk.END).strip()
        pyperclip.copy(text)
        messagebox.showinfo('提示', '已复制到剪贴板!')

def run_app():
    app = PromptToolApp()
    app.mainloop()

def listen_hotkey():
    if keyboard is None:
        print('请先安装 keyboard 库: pip install keyboard')
        return
    # 监听 Ctrl+Alt+P
    keyboard.add_hotkey('ctrl+alt+p', run_app)
    print('按 Ctrl+Alt+P 弹出模板选择窗口...')
    keyboard.wait()

if __name__ == '__main__':
    # 用线程防止阻塞
    t = threading.Thread(target=listen_hotkey)
    t.daemon = True
    t.start()
    while True:
        pass