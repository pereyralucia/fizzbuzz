#/fizzbuzz/fizzbuzz.py
#/fizzbuzz/test_fizzbuzz.py
#HU 001:(es un requerimiento, se dividen en tareas) Como usuario de la aplicación quiero que se clasifique cualquier número entero según sea múltiplo de 3, de 5, 
#de ambos o de ninguno para que el juego muestre la respuesta correcta.
#fizzbuzz, devuelve verdadero o falso, fizz verdadero, buzz falso, dos condiciones si son verdaderas es fizzbuzz
#cuando todos los if son falsos llega a return
#funcion=def
#condicion
#bug=error en produccion=cuando ya entregas el codigo produccion= cuando estas escribiendo el codigo.
#
def fizzbuzz(num):
    if num%3==0 and num%5==0:
      return "fizzbuzz"
    if num%3==0:
     return "fizz"
    if num%5==0:
       return"buzz"
    if num == 0:
       return "fizzbuzz"
    return (num)
#print(fizzbuzz(3))->"fizz"
#print(fizzbuzz(18))->"fizz"
#print(fizzbuzz(20))->"buzz"
#print(fizzbuzz(15))
#print(fizzbuzz(9))
#test_fizzbuzz.py
import unittest
from fizzbuzz import fizzbuzz

class Testfizzbuzz(unittest.TestCase):
    def test_multiplo_3(self):
        self.assertEqual(fizzbuzz(9),"fizz")
    def test_multiplo_5(self):
        self.assertEqual(fizzbuzz(20),"buzz")
    def test_multiplo_3_and_multiplo_5(self):
        self.assertEqual(fizzbuzz(15),"fizzbuzz")
    def test_no_multiplo(self):
        self.assertEqual(fizzbuzz(98),98)
    def test_0(self):
        self.assertEqual(fizzbuzz(0),"fizzbuzz")
    def test_multiplo_negativo(self):
        self.assertEqual(fizzbuzz(-15),"fizzbuzz")
    def test_multiplo_decimales(self):
        self.assertEqual(fizzbuzz(5.0),"buzz")


if __name__ == '__main__':
    unittest.main()



