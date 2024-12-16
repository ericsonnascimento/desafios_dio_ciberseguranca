import string

def verificar_phishing(mensagem):
    # Lista de palavras que indicam possíveis e-mails de phishing
    palavras_suspeitas = ["ganhe", "prêmio", "urgente", "desconto", "click", "promoção"]
    
    # Remove pontuações da mensagem
    mensagem_limpa = mensagem.translate(str.maketrans("", "", string.punctuation))
    
    # Verifica se alguma palavra suspeita está presente no corpo do e-mail
    for palavra in mensagem_limpa.lower().split():
        if palavra in palavras_suspeitas:
            return "Phishing"
    return "Seguro"

# Entrada do usuário
email_usuario = input("Digite o corpo do e-mail: ").strip()

# Verifica a classificação do e-mail
resultado = verificar_phishing(email_usuario)

print(f"Classificação: {resultado}")

'''Descrição
Crie uma solução para analisar uma lista de e-mails recebidos, verificando padrões comuns de phishing nas mensagens. Se um e-mail contiver palavras suspeitas como "ganhe", "prêmio", "urgente", "desconto", "click" e "promoção" ele deve ser classificado como "Phishing" e "Seguro".

Entrada
Uma String contendo um conteúdo único representando o corpo do e-mail.

Saída
"Phishing" ou "Seguro" para cada e-mail.

Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Entrada	
Ganhe um prêmio incrível hoje!	
Saída
Classificação: Phishing

Entrada
Não perca esta promoção exclusiva!	
Saída
Classificação: Phishing

Entrada
Você está convidado para a reunião amanhã!	
Saída
Classificação: Seguro
'''