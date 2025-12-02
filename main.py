animali = [
    "cane",
    "gatto",
    "elefante",
    "leone",
    "tigre",
    "orso"
]

persone = ["giacomo", "mario", "luigi", "anna", "maria", "francesca"]

liste = {
    "animali": ["cane", "gatto", "elefante", "leone", "tigre", "orso"],
    "persone": ["giacomo", "mario", "luigi", "anna", "maria", "francesca"]
}

avaiable_options = list(liste.keys()) + ["e"]

choice = input("\n1 - Visualizza le liste \n"
    "2 - Aggiungi un elemento a una lista \n"
    "3 - Cerca un elemento in una lista \n"
    "q - Esci\n"
    "Scegli un'opzione: ").lower().strip()

while choice != "q":
    if choice == "1":
        for key, value in liste.items():
            print(f"\nLista di {key}:")
            for item in value:
                print(f"- {item}")
    elif choice == "2":
        list_choice = input(f"A quale lista vuoi aggiungere un elemento? ({', '.join(avaiable_options)} - indietro ): ").strip().lower()
        while list_choice not in avaiable_options:
            list_choice = input(f"A quale lista vuoi aggiungere un elemento? ({', '.join(avaiable_options)} - Indietro): ").strip().lower()
            
        if list_choice == "animali":
            new_animal = input("Inserisci il nome dell'animale da aggiungere: ").strip().lower()
            if new_animal in animali:
                print(f"{new_animal} è già presente nella lista degli animali.")
            else:
                animali.append(new_animal)
                print(f"{new_animal} è stato aggiunto alla lista degli animali.")
        elif list_choice == "persone":
            new_person = input("Inserisci il nome della persona da aggiungere: ").strip().lower()
            if new_person in persone:
                print(f"{new_person} è già presente nella lista delle persone.")
            else:
                persone.append(new_person)
                print(f"{new_person} è stato aggiunto alla lista delle persone.")
        elif list_choice.lower() == "e":
            print("Tornando al menu principale.")
        else:
            print("Scelta non valida. Riprova. ")
    elif choice == "3":
        search_el = input("Inserisci il nome dell'elemento da cercare: ").strip().lower()
        if search_el in animali:
            print(f"{search_el} è presente nella lista degli animali.")
        elif search_el in persone:
            print(f"{search_el} è presente nella lista delle persone.")
        else:
            print(f"{search_el} non è presente in nessuna delle liste.")

    choice = input("\n1 - Visualizza le liste \n"
    "2 - Aggiungi un elemento a una lista \n"
    "3 - Cerca un elemento in una lista \n"
    "q - Esci\n"
    "Scegli un'opzione: ").lower().strip()

print("Programma terminato.")