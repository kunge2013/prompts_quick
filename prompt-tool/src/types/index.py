from typing import Protocol, Dict, Any

class PromptTemplate(Protocol):
    def generate_prompt(self, **kwargs: Any) -> str:
        ...

class Shortcut(Protocol):
    def register_shortcut(self, key_combination: str, action: str) -> None:
        ...

class PromptService(Protocol):
    def create_prompt(self, template: PromptTemplate, **variables: Any) -> str:
        ...

    def call_service(self, prompt: str) -> None:
        ...