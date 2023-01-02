import unittest
from robo import *

class TesteBSI(unittest.TestCase):

    def setUp(self):
        #inicialização do robo
        self.robo = iniciar()

    def testar_sobre_o_curso(self):
        mensagens = ["o que é o curso?", "como é o curso?", "o que faz o curso?", "o que o curso faz?"]

        for mensagem in mensagens:
            resposta = self.robo.get_response(mensagem)

            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "O curso serve para formar profissionais capazes de administrar", resposta.text
            )

if __name__ == "__main__":
    carregador = unittest.TestLoader()
    testes = unittest.TestSuite()

    testes.addTest(carregador.loadTestsFromTestCase(TesteBSI))

    executor = unittest.TextTestRunner()
    executor.run(testes)