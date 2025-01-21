def main_menu():
    print("=" * 30)
    print("     🌟 SPRÁVCE ÚKOLŮ 🌟     ")
    print("=" * 30)
    print("1. Přidat nový úkol")
    print("2. Zobrazit všechny úkoly")
    print("3. Odstranit úkol")
    print("4. Konec programu")
    print("=" * 30)
    while True:
        try:
            choice = int(input("👉 Vyberte možnost (1-4): "))
            if choice in [1, 2, 3, 4]:
                return choice
            else:
                print("❌ Neplatná volba. Zkuste to znovu.")
        except ValueError:
            print("❌ Zadejte prosím číslo od 1 do 4.")

tasks = []  # Globální seznam úkolů

def pridej_ukol():
    print("\n📋 Přidání nového úkolu")
    print("=" * 30)
    task = input("✍️ Zadejte popis úkolu: ").strip()
    if task:
        tasks.append(task)
        print(f"✅ Úkol '{task}' byl úspěšně přidán!")
    else:
        print("❌ Popis úkolu nemůže být prázdný.")
        
def zobraz_vsechny_ukoly():
    print("\n📋 Seznam všech úkolů")
    print("=" * 30)
    if tasks:
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    else:
        print("❌ Žádné úkoly nejsou k dispozici.")
        
def odstran_ukol():
    print("\n🗑️ Odstranění úkolu")
    print("=" * 30)
    if tasks:
        zobraz_vsechny_ukoly()
        try:
            choice = int(input("👉 Zadejte číslo úkolu, který chcete odstranit: "))
            if 1 <= choice <= len(tasks):
                removed_task = tasks.pop(choice - 1)
                print(f"✅ Úkol '{removed_task}' byl úspěšně odstraněn.")
            else:
                print("❌ Neplatné číslo úkolu. Zkuste to znovu.")
        except ValueError:
            print("❌ Zadejte platné číslo.")
    else:
        print("❌ Žádné úkoly nejsou k dispozici k odstranění.")


            
if __name__ == "__main__":
    while True:
        volba = main_menu()
        if volba == 1:
            pridej_ukol()
        elif volba == 2:
            zobraz_vsechny_ukoly()
        elif volba == 3:
            odstran_ukol()
        elif volba == 4:
            print("👋 Konec programu.")
            break



