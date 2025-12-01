animali = [
    "cane",
    "gatto",
    "elefante",
    "leone",
    "tigre",
    "orso"
]

persone = []

while True:
    choice = input("Inserisci il nome di un animale o di una persona (q per terminare): ").lower().strip()
    if choice == "q":
        print("Uscita dal programma.")
        break

    if choice in animali:
        print(f"L'animale '{choice}' è presente nella lista.")
    elif choice in persone:
        print(f"La persona '{choice}' è presente nella lista.")
    else:
        print(f"il soggetto '{choice}' non è presente nelle due liste.")
        add_choice = input("Vuoi aggiungerlo a una lista? (y/n): ").lower().strip()
        if add_choice == "y":
            list_choice = input("A quale lista vuoi aggiungerlo? (animali/persone): ").lower().strip()
            if list_choice == "animali":
                animali.append(choice)
                print(f"L'animale '{choice}' è stato aggiunto alla lista.")
                print("Lista aggiornata:", animali)
            elif list_choice == "persone":
                persone.append(choice)
                print(f"La persona '{choice}' è stata aggiunta alla lista.")
                print("Lista aggiornata:", persone)
            else:
                print("Scelta non valida. Nessuna modifica apportata alla lista.")
        else:
            print("Nessuna modifica apportata alla lista.")