
import json
import os

class PromptService:
    def __init__(self, template_path=None):
        if template_path is None:
            template_path = os.path.join(os.path.dirname(__file__), '../templates/prompt_templates.json')
        self.template_path = os.path.abspath(template_path)
        self.templates = self.load_templates()

    def load_templates(self):
        if not os.path.exists(self.template_path):
            return []
        with open(self.template_path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def save_templates(self):
        with open(self.template_path, 'w', encoding='utf-8') as f:
            json.dump(self.templates, f, ensure_ascii=False, indent=2)

    def add_template(self, name, shortcut, template, variables):
        new_template = {
            "name": name,
            "shortcut": shortcut,
            "template": template,
            "variables": variables
        }
        self.templates.append(new_template)
        self.save_templates()

    def get_template_by_shortcut(self, shortcut):
        for tpl in self.templates:
            if tpl["shortcut"] == shortcut:
                return tpl
        return None

    def get_template_by_name(self, name):
        for tpl in self.templates:
            if tpl["name"] == name:
                return tpl
        return None

    def generate_prompt(self, template_name, **kwargs):
        tpl = self.get_template_by_name(template_name)
        if not tpl:
            raise ValueError(f"Template '{template_name}' not found.")
        prompt = tpl["template"]
        for var in tpl["variables"]:
            value = kwargs.get(var, f"{{{var}}}")
            prompt = prompt.replace(f"{{{var}}}", str(value))
        return prompt

    def call_service(self, prompt):
        # Placeholder for service call logic
        print(f"调用服务，提示词: {prompt}")
        # 实际服务调用逻辑可在此实现

    def handle_prompt_request(self, template_name, **kwargs):
        prompt = self.generate_prompt(template_name, **kwargs)
        self.call_service(prompt)