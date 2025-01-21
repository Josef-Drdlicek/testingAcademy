import unittest
from unittest.mock import patch
import io
from contextlib import redirect_stdout
from task_manager import pridej_ukol, zobraz_vsechny_ukoly, odstran_ukol, tasks

class TestTaskManager(unittest.TestCase):
    def setUp(self):
        # Nastaví prázdný seznam úkolů před každým testem
        tasks.clear()

    @patch('builtins.input', return_value="Zadaný testovací úkol")
    def test_pridej_ukol(self, mock_input):
        # Test přidání úkolu
        pridej_ukol()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0], "Zadaný testovací úkol")

    def test_zobraz_vsechny_ukoly(self):
        # Přidáme několik úkolů do seznamu
        tasks.extend(["První úkol", "Druhý úkol", "Třetí úkol"])
        
        # Zachytíme výstup funkce
        captured_output = io.StringIO()
        with redirect_stdout(captured_output):
            zobraz_vsechny_ukoly()
        
        # Ověříme, že výstup obsahuje očekávané řádky
        output = captured_output.getvalue()
        self.assertIn("1. První úkol", output)
        self.assertIn("2. Druhý úkol", output)
        self.assertIn("3. Třetí úkol", output)

    def test_odstran_ukol(self):
        # Přidáme testovací úkoly do seznamu
        tasks.extend(["Úkol 1", "Úkol 2", "Úkol 3"])
        
        # Odstraníme druhý úkol
        with patch('builtins.input', return_value="2"):
            odstran_ukol()
        
        # Ověříme, že seznam je aktualizovaný
        self.assertEqual(len(tasks), 2)
        self.assertNotIn("Úkol 2", tasks)
        self.assertEqual(tasks, ["Úkol 1", "Úkol 3"])

if __name__ == '__main__':
    unittest.main()
