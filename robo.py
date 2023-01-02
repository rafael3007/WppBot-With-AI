from chatterbot import ChatBot
from difflib import SequenceMatcher

CONFIANCA_MINIMA = 0.65


def comparar_mensagens(mensagem_digitada, mensagem_candidata):
    confianca = 0.0

    digitada = mensagem_digitada.text
    candidata = mensagem_candidata.text
    if digitada and candidata:
        confianca = SequenceMatcher(None, 
            digitada,
            candidata)
        confianca = round(confianca.ratio(), 2)

    return confianca

def iniciar():
    robo = ChatBot("Robô de Atendimento do IFBA",
                   read_only=True,
                #    statement_comparison_function=comparar_mensagens,     
                   logic_adapters=[
                       {
                           "import_path": "chatterbot.logic.BestMatch"
                       }
                   ])

    return robo


def executar_robo(robo):
    while True:
        mensagem = input("Digite alguma coisa... \n")
        resposta = robo.get_response(mensagem.lower())
        print(f"o valor da confiança é: {resposta.confidence}")
        if resposta.confidence >= CONFIANCA_MINIMA:
            print(">>", resposta.text)
        else:
            print("Infelizmente, ainda não sei responder isso")
            print("Pergunte outra coisa")


if __name__ == "__main__":
    robo = iniciar()

    executar_robo(robo)
