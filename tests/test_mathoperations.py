
import unittest
import mathoperations

class TestMathOperation(unittest.TestCase):

    def test_add(self):
        #assert bedeutet=> Stelle fest.
        #Wir verknuepfen daher assert mit einen vergleich.
        #Bspw. assertEqual => Stelle fest das der resultat gleich irgendetwas ist.
        self.assertEqual(mathoperations.add(3,7),10)
        self.assertEqual(mathoperations.add(-1,1),0)
        self.assertNotEqual(mathoperations.add(2,2),5)

    def test_divide(self):
        self.assertEqual(mathoperations.divide(10,2),5)
        self.assertAlmostEqual(mathoperations.divide(5,2),2.5)
        self.assertAlmostEqual(mathoperations.divide(10,3),3.33,places=2)

        with self.assertRaises(ZeroDivisionError):
            mathoperations.divide(5,0)

if __name__ == '__main__':
    unittest.main()