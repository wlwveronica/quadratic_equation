# Kvadratická rovnice – řešitel v Pythonu

Tento projekt obsahuje jednoduchý skript v Pythonu pro řešení kvadratické rovnice ve tvaru:

ax² + bx + c = 0

yaml
Zkopírovat kód

Na základě hodnot `a`, `b`, `c` se vypočítá diskriminant a následně reálné kořeny.

---

## 🔧 Spuštění

```bash
python3 rovnice.py <a> <b> <c>
✅ Příklad:
bash
Zkopírovat kód
python3 rovnice.py 1 -3 2
📤 Výstup:

makefile
Zkopírovat kód
Řešení: [2.0, 1.0]
Kategorie: Dva reálné kořeny
🧠 Funkce
Výpočet diskriminantu: D = b² - 4ac

Výpočet reálných řešení (pokud existují)

Kategorizace rovnice podle počtu reálných řešení

Ošetření neplatného vstupu (např. a = 0 nebo špatný počet argumentů)

📁 Struktura
bash
Zkopírovat kód
rovnice.py    # Hlavní skript
README.md     # Dokumentace
.gitignore    # Ignorace zbytečných souborů
💡 Možnosti rozšíření
Podpora pro komplexní řešení (D < 0)

Interaktivní režim bez argumentů

Jednotkové testy (unittest, pytest)