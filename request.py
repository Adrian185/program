def main_menu():
    print("Fenntarthatósági Adatok Elemzése")
    print("1. Adatok lekérdezése")
    print("2. Grafikon rajzolása")
    print("3. Mutató lekérdezése")
    print("0. Kilépés")

def adatok_lekerdezese():
    # Implementálj adatlekérdezés funkciót
    pass

def grafikon_rajzolasa():
    # Implementálj grafikonrajzolás funkciót
    pass

def mutato_lekerdezese():
    # Implementálj mutatólekérdezés funkciót
    pass

def main():
    while True:
        main_menu()
        choice = input("Válassz egy menüpontot: ")
        if choice == "1":
            adatok_lekerdezese()
        elif choice == "2":
            grafikon_rajzolasa()
        elif choice == "3":
            mutato_lekerdezese()
        elif choice == "0":
            print("Kilépés...")
            break
        else:
            print("Érvénytelen választás! Kérlek, válassz újra.")

if __name__ == "__main__":
    main()
