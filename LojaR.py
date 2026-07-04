import os

#======================================================
# CLASSE BASE: PRODUTO
#======================================================
class Produto:
    def __init__(self, codigo, nome, preco, quantidade):
        self.__codigo = codigo
        self.__nome = nome
        self.__preco = preco
        self.__quantidade = quantidade

#gets;sets

def get_codigo(self):
    return self.__codigo

def set_codigo(self, codigo):
    if codigo.strip() != "":
        self.__codigo = codigo

def get_nome(self):
    return self.__nome

def set_nome(self, nome):
    if nome.strip() != "":
        self.__nome = nome

def get_preco(self):
    return self.__preco

def set_preco(self, preco):
    if preco.strip() >= 0:
        self.__preco = preco  

def get_quantidade(self):
    return self.__quantidade

def set_quantidade(self, quantidade):
    if quantidade.strip() >= 0:
        self.__quantidade = quantidade

def get_tipo(self):
    return "geral"        

# Preparação para salvar em arquivo TXT
def transformar_em_linha_txt(self):
    return f"{self.get_tipo()};{self.get_codigo()};{self.get_nome()};{self.get_preco()};{self.get_quantidade()}"

#======================================================
#  CLASSE DEPENDENTE: ROUPA
#======================================================
class Roupa(Produto):
    def __init__(self, codigo, nome, preco, tamanho, quantidade):
        super().__init__(codigo, nome, quantidade, preco)
        self.___tamanho = tamanho # P, M , G...

#gts;sets

    def get_tamanho(self):
        return self.___tamanho
    
    def set_tamanho(self, tamanho):
        if tamanho.strip() != "":
           self.__tamanho = tamanho
    
    def get_tipo(self):
        return "roupa" 

# Incluindo "Tamanho" ao TXT
def trasformar_em_linha_txt(self):
    return f"{self.get_tipo()};{self.get_tamanho()};{self.get_quantidade()};{self.get_preco()};{self.get_nome()};{self.get_codigo()}"
           
#========================================================
# CLASSE GERENCIADORA: SISTEMA DA LOJA
#========================================================
class SistemaLoja:
    def __init__(self):
        self.__produtos = []
        self.__nome.arquivo = "produtos.txt"
        self.carregar_dados()

#CREATE(função de cadastro)
def cadastrar_produto(self):
    print("\n=== CADASTRAR NOVO PRODUTO===")

    codigo = input("Código/ID do produto: ").strip()

# Validação pra n duplicar o ID
    if self.buscar_por_codigo(codigo) is not None:
         print("Erro: Já existe um produto com esse código!!!")
    return

    nome = input("Nome da roupa: ").strip()
    preco = float(input("Preço(R$): "))
    quantidade = int(input("quantidade em estoque:"))
    tamanho = input("Tamanho da Roupa(EX:P, M, G, GG): ").strip().upper()

# "Criando" a roupa
    nova_roupa = Roupa(codigo, nome, preco, quantidade, tamanho)

# add a lista de memória
    self.__produtos.append(nova_roupa)
    
# Salvando no arquivo de texto
    self.salvar_dados()
    print("Produto cadastrado e salvo com sucesso!")

def buscar_por_codigo(self, codigo):
    for produto in self.__produtos:
        if produto.get_codigo() == codigo:
            return produto
    return None    
# Gravação de arquivos (Escrita)
def salvar_dados(self):
    try:
        with open(self.__nome_arquivo, "w", encoding="utf-8") as arquivo:
            for produto in self.__produtos:
                arquivo.write(produto.transformar_em_linha_txt() + "\n")
    except Exception as erro:
        print(f"Erro ao salvar dados: {erro}")

# Gravação de arquivos (Leitura) 
def carregar_dados(self):
    if not os.path.exists(self.__nome_arquivo):
        return

    try:
        with open(self.__nome_arquivo, "r", encoding="utf-8") as arquivo:
           linhas = arquivo.readlines()

        self__produtos = []
        for linha in linhas:
            linha = linha.strip()
            if not linha:
                continue

            dados = linha.split(";")
            #Formato: codigo;nome;preco;quantidadd;tamanho;tipo
            if dados[0] == "roupa" and len(dados) == 6:
                roupa = Roupa(
                    codigo=dados[1],
                    nome=dados[2],
                    preco=float(dados[3]),
                    quantidade=int(dados[4]),
                    tamanho=dados[5]
                )
                self.__produtos.append(roupa)
    except Exception as erro:
        print(f"Erro ao carregar dados: {erro}")

#======================================================
#FUNÇÕES AUXILIARES E TRATAMENTO DE ERROS
#======================================================
def ler_inteiro(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            if valor >= 0:
                return valor
            print("Digite um valor maior ou igual a zero!")
        except ValueError:
            print("Entrada inválida. Digite um número válido!")

def exibir_menu():
    print("\n" + "=" * 40)
    print("  LOJA DE ROUPAS - MENU") 
    print("=" * 40)
    print("1 - Cadastrar Produto")
    print("0 - Sair")
    print("=" * 40)           

#=============================================
#  EXECUÇÃO PRINCIPAL
#=============================================
def main():
    loja = SistemaLoja()

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
             loja.cadastrar_produto()
        elif opcao == "0":
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()                 
