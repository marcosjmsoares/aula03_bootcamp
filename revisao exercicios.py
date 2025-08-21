### Exercício 1: Verificação de Qualidade de Dados
# Você está analisando um conjunto de dados de vendas e precisa garantir 
# que todos os registros tenham valores positivos para `quantidade` e `preço`. 
# Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos 
# forem positivos ou "Dados inválidos" caso contrário.
# quantidade = int(input("Insira quantidade: "))
# preco = int(input("Insira preço: "))

# if quantidade > 0 and preco > 0:
#     print("Numero validos")
# else:
#     print("Numero invalidos")

### Exercício 2: Classificação de Dados de Sensor
# Imagine que você está trabalhando com dados de sensores IoT. 
# Os dados incluem medições de temperatura. Você precisa classificar cada leitura 
# como 'Baixa', 'Normal' ou 'Alta'. Considerando que:
# temperatura = int(input("Insira a temperatura: "))

# if temperatura <= 0:
#     print("Baixa")
# elif temperatura > 0 and temperatura < 18:
#     print("Media")
# else:
#     print("Alta")


### Exercício 3: Filtragem de Logs por Severidade
# Você está analisando logs de uma aplicação e precisa filtrar mensagens 
# com severidade 'ERROR'. Dado um registro de log em formato de dicionário 
# como `log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}`, 
# escreva um programa que imprima a mensagem se a severidade for 'ERROR'.
# log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}

# if log['level'] == 'ERROR': 
#     print(log['message'])


### Exercício 4: Validação de Dados de Entrada
# Antes de processar os dados de usuários em um sistema de recomendação, 
# você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha 
# fornecido um email válido. Escreva um programa que valide essas condições 
# e imprima "Dados de usuário válidos" ou o erro específico encontrado.
# idade = int(input("Insira a idade: "))
# email = str(input("Insira o email: "))

# #if (idade >=18 and idade <= 65): #errado padrao sql
# if not 18 <= idade <= 65:
#     print("Idade Invalida!")
# elif email not in "@" or email not in ".":
#     print("Email invalido!")
# else:
#     print("Dados de usuarios validos")

# nome = ['Luciano']
# for letra in nome:
#     print(nome)

### Exercício 5: Detecção de Anomalias em Dados de Transações
# Você está trabalhando em um sistema de detecção de fraude e precisa identificar 
# transações suspeitas. Uma transação é considerada suspeita se o valor for superior 
# a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h). 
# Dada uma transação como `transacao = {'valor': 12000, 'hora': 20}`, verifique se ela é suspeita.
# transacao = {'valor': 1200, 'hora': 12}

# if transacao['valor'] > 10000 and ( not 9 <= transacao['hora'] <= 18):
#     print("Fraude")
# else:
#     print("Transação normal")


### Exercício 6. Contagem de Palavras em Textos
# Objetivo:** Dado um texto, contar quantas vezes cada palavra única aparece nele.

# texto = "Hoje estou estudando o bootcamp de python. Recomendo fortemente esse bootcamp."
# novo_texto = texto.replace(",","").replace(".","")
# palavras = novo_texto.split()

# print(palavras)

# contagem = {}

# for palavra in palavras:
#     if palavra in contagem:
#         contagem[palavra] += 1
#     elif palavra not in contagem:
#         contagem[palavra] = 1

#     print(f"Palavra atual: {palavra}")
#     print(f"Estado do dicionário: {contagem}")
#     print("-----")
# print(contagem)        


### Exercício 7. Normalização de Dados
# Objetivo:** Normalizar uma lista de números para que fiquem na escala de 0 a 1.
# numeros = [10,20,30,40,50]
# minimo = min(numeros)
# maximo = max(numeros)
# normalizados = [(x - minimo) / (maximo - minimo) for x in numeros]

# print(normalizados)


### Exercício 8. Filtragem de Dados Faltantes
# Objetivo:** Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando
# usuarios = [
#     {"nome": "Alice", "email": "alice@example.com"},
#     {"nome": "Bob", "email": ""},
#     {"nome": "Carol", "email": "carol@example.com"}
# ]

# usuarios_validos = [usuario for usuario in usuarios if usuario["email"]] #if usuario["email"] apenas se nao for vazio

# print(usuarios_validos)


### Exercício 9. Extração de Subconjuntos de Dados
# Objetivo:** Dada uma lista de números, extrair apenas aqueles que são pares.
# lista_dados = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

# lista_par = [numero for numero in lista_dados if numero % 2 == 0]
# print(lista_par)


### Exercício 10. Agregação de Dados por Categoria
# Objetivo:** Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.
# vendas = [
#     {"produto": "TV Samsung 55", "Categoria": "TV", "valor": "3000"},
#     {"produto": "Macbook", "Categoria": "Computador", "valor": "10000"},
#     {"produto": "Iphone 14", "Categoria": "Celular", "valor": "5000"},
#     {"produto": "Xiaomi Poco X6", "Categoria": "Celular", "valor": "2000"},
#     {"produto": "Computador Positivo", "Categoria": "Computador", "valor": "500"},    
#     {"produto": "Notebook Dell 14", "Categoria": "Computador", "valor": "4000"},
#     {"produto": "TV 29", "Categoria": "TV", "valor": "1000"}
# ]

# soma_categoria = {}

# # ERRADO
# # for categoria in vendas: 
# #     if categoria in soma_categoria: 
# #         soma_categoria[categoria] += vendas["valor"] 
# #     elif categoria not in soma_categoria: 
# #         soma_categoria[categoria] = vendas["valor"]

# for venda in vendas:  
#     if venda["Categoria"] in soma_categoria:
#         soma_categoria[venda["Categoria"]] += int(venda["valor"])
#     else:
#         soma_categoria[venda["Categoria"]] = int(venda["valor"])

# print(soma_categoria)

### Exercícios com WHILE

### Exercício 11. Leitura de Dados até Flag
# Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.

# texto = ""
# while texto.lower() != 'sair':
#     texto = str(input("Insira uma palavra:"))
#     if texto.lower() != "sair":
#         print("Palavra Errada")

# print("Palavra correta")        

### Exercício 12. Validação de Entrada
# Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.

# numero = ""
# while numero != 5:
#     numero = int(input("Insira um número de 1 a 10:"))
#     if numero != 5:
#         print("Numero Invalido")

# print("Numero Válido")

### Exercício 13. Consumo de API Simulado
# Simular o consumo de uma API paginada, onde cada "página" de dados é processada em loop até que não haja mais páginas.
pagina_atual = 1
pagina_total = 5

while pagina_atual <= pagina_total:
    print(f"Processando página {pagina_atual} de {pagina_total}")
    pagina_atual +=1

print("Todas as páginas foram processadas")


### Exercício 14. Tentativas de Conexão
# Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.



### Exercício 15. Processamento de Dados com Condição de Parada
# Processar itens de uma lista até encontrar um valor específico que indica a parada.