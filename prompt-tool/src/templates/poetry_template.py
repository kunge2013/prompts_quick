class PoetryTemplate:
    def __init__(self, title: str, author: str, content: str):
        self.title = title
        self.author = author
        self.content = content

    def generate_prompt(self) -> str:
        return f"Title: {self.title}\nAuthor: {self.author}\nContent:\n{self.content}"

    @staticmethod
    def from_variables(title: str, author: str, lines: list) -> 'PoetryTemplate':
        content = "\n".join(lines)
        return PoetryTemplate(title, author, content)