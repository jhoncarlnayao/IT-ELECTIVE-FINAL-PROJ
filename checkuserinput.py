import shutil

def print_centered(text):
    terminal_width, _ = shutil.get_terminal_size()
    centered_text = text.center(terminal_width)
    print(centered_text)

# Example usage:
print_centered("Hello, World!")
print_centered("adadadadada")
