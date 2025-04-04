import random
import time

def generate_ascii_art(width=40, height=10, charset='@#*+=-:. '):
    """Gera e exibe uma arte ASCII aleatória no terminal."""
    for _ in range(height):
        line = ''.join(random.choice(charset) for _ in range(width))
        print(line)
        time.sleep(0.1)  # Pequeno atraso para efeito visual

if __name__ == "__main__":
    while True:
        generate_ascii_art()
        time.sleep(1)
        print("\033c", end="")  # Limpa a tela para animação contínua