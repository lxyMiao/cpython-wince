import unittest

class LongExpText(unittest.TestCase):
    def test_longexp(self):
        REPS = 65580
        import os
        if os.name == "ce":
            REPS = 20000 # Avoid MemoryError on Windows CE
        l = eval("[" + "2," * REPS + "]")
        self.assertEqual(len(l), REPS)

if __name__ == "__main__":
    unittest.main()
