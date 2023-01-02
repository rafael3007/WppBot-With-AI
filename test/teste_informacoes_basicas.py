import unittest

from html2text import unifiable_n
from robo import *


class TesteInformacoesBasicas(unittest.TestCase):

    def setUp(self):
        self.robo = iniciar()

    def testar_localizacao(self):
        mensagens = ["onde o IFBA está localizado?", "onde fica o IFBA?",
                     "onde vocês funcionam?", "onde o IFBA está?", "onde o IFBA funciona?"]

        for mensagem in mensagens:
            print(f"testando a mensagem: {mensagem}")

            resposta = self.robo.get_response(mensagem)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "O IFBA fica localizado na avenida Sérgio Vieria de Mello, 3150, Zabelê", resposta.text)

    def testar_horario_de_funcionamento(self):
        mensagens = [ "qual o horário de funcionamento?", "que horas vocês ficam abertos?", "que horário funciona?", 
        "ficam abertos que horas?" ]

        for mensagem in mensagens:
            print(f"testando a mensagem: {mensagem}")

            resposta = self.robo.get_response(mensagem)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn("O IFBA funciona pela manhã, tarde e noite", resposta.text)


if __name__ == "__main__":
    carregador = unittest.TestLoader()
    testes = unittest.TestSuite()

    testes.addTest(carregador.loadTestsFromTestCase(TesteInformacoesBasicas))

    executor = unittest.TextTestRunner()
    executor.run(testes)
