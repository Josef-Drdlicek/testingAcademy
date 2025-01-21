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

## 🧬 Struktura projektu
```
task_manager_project/
├── task_manager.py        # Hlavní soubor s aplikací
├── test_task_manager.py   # Soubory s automatickými testy
├── pycache/               # Složka s kompilovanými Python soubory
└── README.md              # Popis projektu
```

---

## 🚀 Jak spustit projekt

1. Klonujte repozitář:
   ```bash
   git clone git@github.com:Josef-Drdlicek/testingAcademy.git
   cd testingAcademy
   ```

2. Spusťte aplikaci:
   ```bash
   python task_manager.py
   ```

3. Spusťte testy:
   ```bash
   python -m unittest test_task_manager.py
   ```

---

## 🔍 Testovací případy

### Testovací případy pro `main_menu()`

**Název:** Test volby v hlavním menu  
**Popis:** Ověření, že volba čísla 1 v hlavním menu správně spustí funkci `pridej_ukol`.  
**Vstupní podmínky:** Program zobrazuje hlavní menu.  
**Kroky testu:**
1. Spusťte program.
2. Ověřte, že se zobrazuje hlavní menu s nabídkou voleb ("1. Přidat nový úkol", "2. Zobrazit všechny úkoly" atd.).
3. Zadejte číslo 1 a potvrďte stisknutím klávesy Enter.  
**Očekávaný výsledek:** Program spustí funkci `pridej_ukol()`.  
**Skutečný výsledek:** Funkce `pridej_ukol()` byla spuštěna a program zobrazil výzvu k zadání nového úkolu.  
**Stav:** Pass  
**Poznámky:** Tento případ ověřuje funkčnost navigace z hlavního menu a správné spuštění klíčové funkce programu.

---

### Testovací případy pro `pridej_ukol()`

**Název:** Přidání platného úkolu  
**Popis:** Ověření, že funkce správně přidá platný úkol do seznamu.  
**Vstupní podmínky:** Seznam úkolů je prázdný.  
**Kroky testu:**
1. Spusťte program a zvolte možnost "1. Přidat nový úkol".
2. Zadejte popis úkolu: "Nakoupit potraviny".
3. Potvrďte zadání klávesou Enter.  
**Očekávaný výsledek:** Úkol "Nakoupit potraviny" je uložen do seznamu.  
**Skutečný výsledek:** Úkol byl uložen do seznamu a zobrazila se potvrzovací zpráva.  
**Stav:** Pass  
**Poznámky:** Test ověřuje, že funkce správně ukládá úkoly a poskytuje uživatelskou odezvu.

---

### Testovací případy pro `zobraz_vsechny_ukoly()`

**Název:** Zobrazení prázdného seznamu  
**Popis:** Ověření, že funkce správně informuje uživatele, pokud je seznam úkolů prázdný.  
**Vstupní podmínky:** Seznam úkolů je prázdný.  
**Kroky testu:**
1. Spusťte program a zvolte možnost "2. Zobrazit všechny úkoly".  
**Očekávaný výsledek:** Program zobrazí zprávu "Žádné úkoly nejsou k dispozici".  
**Skutečný výsledek:** Zpráva byla zobrazena.  
**Stav:** Pass  
**Poznámky:** Tento test je důležitý pro ověření správné komunikace s uživatelem v případě prázdného seznamu.

---

### Testovací případy pro `odstran_ukol()`

**Název:** Odstranění platného úkolu  
**Popis:** Ověření, že funkce správně odstraní vybraný úkol podle jeho čísla.  
**Vstupní podmínky:** Seznam úkolů obsahuje tři úkoly.  
**Kroky testu:**
1. Spusťte program a zvolte možnost "3. Odstranit úkol".
2. Zadejte číslo 2 a potvrďte.  
**Očekávaný výsledek:** Druhý úkol je odstraněn a zbývající úkoly jsou posunuty.  
**Skutečný výsledek:** Úkol byl odstraněn a seznam byl aktualizován.  
**Stav:** Pass  
**Poznámky:** Tento test ověřuje klíčovou funkcionalitu programu a správné chování při změně seznamu.

---

## 🔧 Další kroky
- [ ] Implementace uložení seznamu úkolů do souboru.
- [ ] Rozšíření aplikace o grafické rozhraní (GUI).

---

## 🔧 Autor
Josef Drdlíček  
[GitHub Profil](https://github.com/Josef-Drdlicek)
