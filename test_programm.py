import unittest
import programm

class TestProgramm(unittest.TestCase):

    def test_plusmal(self):
        self.assertEqual(programm.plusmal(2, 3), 10)

    def test_unterschreiben(self):
        self.assertEqual(programm.unterschreiben("test"), "test_unterschrieben")

    def test_kubieren(self):
        self.assertEqual(programm.kubieren(2), 8)
        self.assertEqual(programm.kubieren(3), 27)

if __name__ == '__main__':
    unittest.main()
