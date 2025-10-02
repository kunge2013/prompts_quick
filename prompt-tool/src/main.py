from services.prompt_service import PromptService
from utils.shortcut_manager import ShortcutManager

def main():
    shortcut_manager = ShortcutManager()
    prompt_service = PromptService()

    # Initialize shortcuts
    shortcut_manager.setup_shortcuts()

    print("Prompt Tool is running...")
    print("Press your configured shortcuts to generate prompts.")

    # Main loop to listen for shortcuts
    while True:
        shortcut_manager.listen_for_shortcuts(prompt_service)

if __name__ == "__main__":
    main()