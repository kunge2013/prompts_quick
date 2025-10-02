import tkinter as tk
from tkinter import ttk
import threading

class ShortcutManager:
    def __init__(self):
        self.registered_shortcuts = {}
        self.running = False
        self.lock = threading.Lock()
        self.prompt_service = None
        self.window = None

    def setup_shortcuts(self):
        """初始化快捷键"""
        print("正在设置提示词模板...")
        self.running = True

    def create_input_dialog(self, template):
        """为模板创建输入对话框"""
        dialog = tk.Toplevel(self.window)
        dialog.title(f"输入 - {template['name']}")
        dialog.geometry("400x300")

        # 创建输入框
        entries = {}
        for i, var in enumerate(template["variables"]):
            frame = ttk.Frame(dialog)
            frame.pack(fill="x", padx=5, pady=5)
            
            label = ttk.Label(frame, text=f"{var}:")
            label.pack(side="left", padx=5)
            
            entry = ttk.Entry(frame)
            entry.pack(side="right", expand=True, fill="x", padx=5)
            entries[var] = entry

        def submit():
            # 收集所有输入
            values = {var: entry.get() for var, entry in entries.items()}
            with self.lock:
                prompt = self.prompt_service.generate_prompt(template["name"], **values)
                self.prompt_service.call_service(prompt)
            dialog.destroy()

        # 提交按钮
        submit_btn = ttk.Button(dialog, text="生成提示词", command=submit)
        submit_btn.pack(pady=10)

    def create_template_button(self, frame, template):
        """为模板创建按钮"""
        def on_click():
            self.create_input_dialog(template)

        btn = ttk.Button(
            frame, 
            text=f"{template['name']} ({template['shortcut']})",
            command=on_click
        )
        btn.pack(fill="x", padx=5, pady=2)

    def listen_for_shortcuts(self, prompt_service):
        """启动GUI界面"""
        try:
            self.prompt_service = prompt_service
            
            # 创建主窗口
            self.window = tk.Tk()
            self.window.title("提示词模板选择器")
            self.window.geometry("300x400")

            # 创建一个框架来容纳按钮
            frame = ttk.Frame(self.window)
            frame.pack(fill="both", expand=True, padx=10, pady=10)

            # 创建标题标签
            title = ttk.Label(frame, text="请选择提示词模板:", font=("Arial", 12))
            title.pack(pady=10)

            # 为每个模板创建一个按钮
            for template in prompt_service.templates:
                self.create_template_button(frame, template)

            # 运行主循环
            self.window.mainloop()
            
        except Exception as e:
            print(f"错误: {str(e)}")
            self.running = False