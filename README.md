# Task Manager Project

## 📋 Popis projektu
Task Manager je jednoduchá aplikace vytvořená v Pythonu, která umožňuje spravovat úkoly prostřednictvím konzolového rozhraní. Tento projekt je navržen jako tréninkový projekt pro zlepšení dovedností v programování a testování v Pythonu.

---

## ✨ Funkce
1. **Přidávání úkolů:**
   - Uživatel může přidat nový úkol prostřednictvím jednoduchého vstupu.

2. **Zobrazení úkolů:**
   - Aplikace vypíše všechny aktuálně uložené úkoly.
   - Pokud nejsou žádné úkoly, zobrazí zprávu, že seznam je prázdný.

3. **Odstranění úkolů:**
   - Uživatel může odstranit úkol podle jeho pořadového čísla.

4. **Testování:**
   - Projekt obsahuje automatické testy pomocí modulu `unittest`, které pokrývají všechny hlavní funkce aplikace.

---

## 🛠️ Použité technologie
- **Programovací jazyk:** Python 3.10+
- **Moduly:**
  - `unittest`: Pro testování.
  - `io` a `contextlib`: Pro zachycení výstupu během testů.

---

## 🧩 Struktura projektu
task_manager_project/ │ ├── task_manager.py # Hlavní soubor s aplikací ├── test_task_manager.py # Soubory s automatickými testy ├── pycache/ # Složka s kompilovanými Python soubory └── README.md # Popis projektu

yaml
Zkopírovat
Upravit

---

## 🚀 Jak spustit projekt
1. Klonujte repozitář:
   ```bash
   git clone git@github.com:Josef-Drdlicek/testingAcademy.git
   cd testingAcademy
Spusťte aplikaci:

bash
Zkopírovat
Upravit
python task_manager.py
Spusťte testy:

bash
Zkopírovat
Upravit
python -m unittest test_task_manager.py
🧪 Testování
Aplikace obsahuje automatické testy, které pokrývají:

Přidání úkolu
Zobrazení všech úkolů
Odstranění úkolu
Chcete-li spustit všechny testy:

bash
Zkopírovat
Upravit
python -m unittest discover
📌 Poznámky k vývoji
Tento projekt byl vytvořen jako součást vzdělávacího kurzu na téma programování a testování v Pythonu. Cílem bylo procvičit:

Použití funkcí v Pythonu.
Základy testování pomocí unittest.
Správu verzí s Git a GitHub.
📝 Autor
Josef Drdlíček