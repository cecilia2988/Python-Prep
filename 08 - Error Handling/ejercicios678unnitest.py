'''6) Agregar casos de pruebas para el método verifica_primos() realizando el cambio en la clase, para que devuelva una lista de True o False en función de que el elemento en la posisicón sea o no primo

7) Agregar casos de pruebas para el método conversion_grados()

8) Agregar casos de pruebas para el método factorial()'''

import unittest


import misherramientas as h

class ProbandoMetodos (unittest.TestCase):
    def test_verificar_primo(self):
        lista=[6]
        h1=h.Herramientas(lista)
        listaprimos= h1.verifica_primo()
        esperado=[False]
        self.assertEqual(listaprimos,esperado)

    def test_conversion_grados(self):
        pass

    def test_factorial_concero(self):
        lista=[0]
        h1=h.Herramientas(lista)
        listafactorial=h1.factorial()
        esperado=[0]
        self.assertEqual(listafactorial,esperado)    
    
    def test_factorial_erroneo(self):
        num="a"
        with self.assertRaises(Exception): h.Herramientas.__factorial(num)

unittest.main(argv=[''], verbosity=2, exit=False)