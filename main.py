animali = [
    "cane",
    "gatto",
    "elefante",
    "leone",
    "tigre",
    "orso"
]

persone = ["giacomo", "mario", "luigi", "anna", "maria", "francesca"]

while True:
    choice = input("\n1 - Visualizza le liste \n"
    "2 - Aggiungi un elemento a una lista \n"
    "q - Esci\n"
    "Scegli un'opzione: ").lower().strip()

    if choice == "q":
        print("Uscita dal programma.")
        break
    elif choice == "1":
        print("Lista degli animali:")
        for animale in animali:
            print(f"- {animale}")
        print("\nLista delle persone:")
        for persona in persone:
            print(f"- {persona}")
    elif choice == "2":
        while True:
            list_choice = input("A quale lista vuoi aggiungere un elemento? (1 - Animali, 2 - Persone, e - Indietro): ").strip()
            if list_choice == "1":
                new_animal = input("Inserisci il nome dell'animale da aggiungere: ").strip()
                if new_animal in animali:
                    print(f"{new_animal} è già presente nella lista degli animali.")
                else:
                    animali.append(new_animal)
                    print(f"{new_animal} è stato aggiunto alla lista degli animali.")
                break
            elif list_choice == "2":
                new_person = input("Inserisci il nome della persona da aggiungere: ").strip()
                if new_person in persone:
                    print(f"{new_person} è già presente nella lista delle persone.")
                else:
                    persone.append(new_person)
                    print(f"{new_person} è stato aggiunto alla lista delle persone.")
                break
            elif list_choice.lower() == "e":
                break
            else:
                print("Scelta non valida. Riprova.")
    else:
        print("Scelta non valida. Riprova.")