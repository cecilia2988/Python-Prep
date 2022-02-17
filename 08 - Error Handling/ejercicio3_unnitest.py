'''
3) Importar el modulo "unittest" y crear los siguientes casos de pruebas sobre la clase utilizada en el punto 2<br>
Creacion del objeto incorrecta<br>
Creacion correcta del objeto<br>
Metodo valor_modal()<br>
'''

from logging import exception
import unittest
import misherramientas as h

class   ProbandoMetodos (unittest.TestCase):
    def test_crear_objeto_incorrecto(self):
        param="Hola"
        self.assertRaises(ValueError,h.Herramientas,param)


    def test_crear_objeto_correcto(self):
         lista =[1,2,3,4,5]
         h1= h.Herramientas(lista)
         self.assertEquals(h1.lista,lista)  


    def test_numero_primo (self):
        numero="a"
        with self.assertRaises(Exception): h.Herramientas.__verifica_primo(numero)


    # def test_valor_modal(self):
    #     lis = [1,2,1,3]
    #     h1 = h.Herramientas(lis)
    #     moda, veces = h1.valor_modal(False)
    #     moda = [moda]
    #     moda.append(veces)
    #     resultado = [1, 2]
    #     self.assertEqual(moda, resultado)
        
        


unittest.main(argv=[''], verbosity=2, exit=False)
