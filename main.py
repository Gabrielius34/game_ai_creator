from utils.parser import analizuoti_aprasyma
from engines.pygame_gen import generuoti_pygame
from engines.ursina_gen import generuoti_ursina

def pagrindinis():
    aprasymas = input("🎮 Įveskite žaidimo aprašymą: ")
    parametrai = analizuoti_aprasyma(aprasymas)

    if parametrai["engine"] == "pygame":
        generuoti_pygame(aprasymas, parametrai)
    elif parametrai["engine"] == "ursina":
        generuoti_ursina(aprasymas, parametrai)
    else:
        print("⚠️ Šiam aprašymui dar nėra palaikymo.")

if __name__ == "__main__":
    pagrindinis()