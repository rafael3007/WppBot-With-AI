import unittest
from assistente_google import *

CHAMANDO_JOANA = "/misc/ifba/workspaces/inteligencia artificial/assistente virtual com testes/audios/chamando joana.wav"
CHAMANDO_OUTRO_NOME = "/misc/ifba/workspaces/inteligencia artificial/assistente virtual com testes/audios/chamando outro nome.wav"


COMANDO_LIGAR_LAMPADA = "/misc/ifba/workspaces/inteligencia artificial/assistente virtual com testes/audios/ligar lampada.wav"
COMANDO_DESLIGAR_LAMPADA = "/misc/ifba/workspaces/inteligencia artificial/assistente virtual com testes/audios/desligar lampada.wav"
COMANDO_AUMENTAR_LUMINOSIDADE = "/misc/ifba/workspaces/inteligencia artificial/assistente virtual com testes/audios/aumentar luminosidade.wav"
COMANDO_DIMINUIR_LUMINOSIDADE = "/misc/ifba/workspaces/inteligencia artificial/assistente virtual com testes/audios/diminuir luminosidade.wav"


class TesteNomeAssistente(unittest.TestCase):

    def setUp(self):
        iniciar()

    def testar_reconhecer_nome(self):
        comando = processar_audio_do_comando(CHAMANDO_JOANA)
        comando = comando.split()

        nome_assistente = ""
        if len(comando):
            nome_assistente = comando[0].lower()
            print(f"nome do assistente: {nome_assistente}")

        self.assertIn("joana", nome_assistente)

    def testar_nao_reconhecer_outro_nome(self):
        comando = processar_audio_do_comando(CHAMANDO_OUTRO_NOME)
        comando = comando.split()

        nome_assistente = ""
        if len(comando):
            nome_assistente = comando[0].lower()
            print(f"nome do assistente: {nome_assistente}")

        self.assertNotIn("joana", nome_assistente)


class TesteLampada(unittest.TestCase):

    def setUp(self):
        iniciar()

    def testar_ligar_lampada(self):
        comando = processar_audio_do_comando(COMANDO_LIGAR_LAMPADA)
        print(f"comando reconhecido: {comando}")

        acao, objeto = tokenizar_comando(comando)
        valido = validar_comando(acao, objeto)

        self.assertTrue(valido)

    def testar_desligar_lampada(self):
        comando = processar_audio_do_comando(COMANDO_DESLIGAR_LAMPADA)
        print(f"comando reconhecido: {comando}")

        acao, objeto = tokenizar_comando(comando)
        valido = validar_comando(acao, objeto)

        self.assertTrue(valido)


class TesteLuminosidade(unittest.TestCase):

    def setUp(self):
        iniciar()

    def testar_aumentar_luminosidade(self):
        comando = processar_audio_do_comando(COMANDO_AUMENTAR_LUMINOSIDADE)
        print(f"comando reconhecido: {comando}")

        acao, objeto = tokenizar_comando(comando)
        valido = validar_comando(acao, objeto)

        self.assertTrue(valido)

    def testar_diminuir_luminosidade(self):
        comando = processar_audio_do_comando(COMANDO_DIMINUIR_LUMINOSIDADE)
        print(f"comando reconhecido: {comando}")

        acao, objeto = tokenizar_comando(comando)
        valido = validar_comando(acao, objeto)

        self.assertTrue(valido)


if __name__ == "__main__":
    carregador = unittest.TestLoader()
    testes = unittest.TestSuite()

    testes.addTest(carregador.loadTestsFromTestCase(TesteNomeAssistente))
    testes.addTest(carregador.loadTestsFromTestCase(TesteLampada))
    testes.addTest(carregador.loadTestsFromTestCase(TesteLuminosidade))

    executor = unittest.TextTestRunner()
    executor.run(testes)
