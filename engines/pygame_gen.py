import os

def generuoti_pygame(aprasymas, parametrai):
    turinys = f"""import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("2D Nuotykis")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    pygame.display.flip()

pygame.quit()
"""
    pavadinimas = "projekti/pygame_zaidimas.py"
    os.makedirs("projekti", exist_ok=True)
    with open(pavadinimas, "w", encoding="utf-8") as f:
        f.write(turinys)
    print(f"✅ Sukurtas žaidimas: {pavadinimas}")