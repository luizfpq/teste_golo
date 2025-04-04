import random
import time
import sys

# Definição de constantes para facilitar manutenção e reutilização
WIDTH = 40
HEIGHT = 10
CHARSET = "@#*+=-:. "
FRAME_DELAY = 0.1
LOOP_DELAY = 1

def generate_ascii_art(width=WIDTH, height=HEIGHT, charset=CHARSET):
    """Gera arte ASCII como uma string única para melhor desempenho."""
    return "\n".join(
        "".join(random.choice(charset) for _ in range(width))
        for _ in range(height)
    )

def display_ascii_animation():
    """Exibe a animação ASCII em loop contínuo."""
    try:
        while True:
            sys.stdout.write("\033c")  # Limpa a tela
            sys.stdout.write(generate_ascii_art() + "\n")
            sys.stdout.flush()
            time.sleep(LOOP_DELAY)
    except KeyboardInterrupt:
        print("\nAnimação encerrada.")

if __name__ == "__main__":
    display_ascii_animation()
