animali = [
    "cane",
    "gatto",
    "elefante",
    "leone",
    "tigre",
    "orso"
]

choice = input("Inserisci il nome di un animale: ").lower().strip()

if choice in animali:
    print(f"L'animale '{choice}' è presente nella lista.")
else:
    print(f"L'animale '{choice}' non è presente nella lista.")