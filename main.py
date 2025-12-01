animali = [
    "cane",
    "gatto",
    "elefante",
    "leone",
    "tigre",
    "orso"
]

while True:
    choice = input("Inserisci il nome di un animale (q per terminare): ").lower().strip()
    if choice == "q":
        print("Uscita dal programma.")
        break

    if choice in animali:
        print(f"L'animale '{choice}' è presente nella lista.")
    else:
        print(f"L'animale '{choice}' non è presente nella lista.")
        add_choice = input("Vuoi aggiungerlo alla lista? (y/n): ").lower().strip()
        if add_choice == "y":
            animali.append(choice)
            print(f"L'animale '{choice}' è stato aggiunto alla lista.")
            print("Lista aggiornata:", animali)
        else:
            print("Nessuna modifica apportata alla lista.")