vendedores_cadastrados = []
produtos_cadastrados = []
produtos_comprados = []

def cadastrar_vendedor():
    novo_vendedor = {}
    novo_vendedor["nome"] = input("Digite o nome completo do vendedor: ")
    novo_vendedor["cnpj"] = input("Digite o CNPJ do vendedor (No mínimo 14 dígitos): ")

    
    if len(novo_vendedor["cnpj"]) < 14:
        print("\nCNPJ digitado incorretamente. O mesmo deve ter no minimo 14 caracteres.")
        

    if not novo_vendedor["cnpj"].isdigit():
        print("\nCNPJ digitado incorretamente. O mesmo deve conter apenas numeros.")
    
    novo_vendedor["telefone"] = input("Digite o telefone do vendedor (No mínimo 11 dígitos incluindo o DDD): ")

    if len(novo_vendedor["telefone"]) < 11:
        print("\nTelefone digitado incorretamente. O mesmo deve ter no minimo 11 caracteres, incluindo o DDD.")
        

    if not novo_vendedor["telefone"].isdigit():
        print("\nTelefone digitado incorretamente. O mesmo deve conter apenas numeros.")
        

    novo_vendedor["senha"] = input("Digite a senha do vendedor: ")
    novo_vendedor["email"] = input("Digite o email do vendedor: ")

    contador = 1

    for caractere in novo_vendedor["email"]:
        if (caractere == "@"):
            if (contador < 3 or contador > 5):
                print("\nNumero de caracteres menor que 3 ou maior que 5 antes do @. Isso nao e permitido.")
                raise SystemExit

        elif not (caractere.isalnum() or caractere == "_" or caractere == "."):
            print("\n Você digitou algum caractere que nao e permitido. Sao permitidos apenas letras de A a Z, numeros e os caracteres '_' e '.'")
            raise SystemExit
        contador += 1

    novo_vendedor["login"] = input("Digite o nome de login do vendedor: ")

    for caractere in novo_vendedor["login"]:
        if caractere.isupper():
            print("\n Nao sao permitidos caracteres em letra Maiuscula. O seu nome de login deve ter no minimo 5 caracteres e todos minusculos.")
            break

    if len(novo_vendedor["login"]) < 5:
        print("\nNome de login digitado incorretamente. O mesmo deve ter no minimo 5 caracteres.")


    email_existente = False
    login_existente = False
    senha_existente = False
    telefone_existente = False
    cnpj_existente = False
    for vendedor in vendedores_cadastrados:
        if vendedor["email"] == novo_vendedor["email"]:
            email_existente = True
        if vendedor["login"] == novo_vendedor["login"]:
            login_existente = True
        if vendedor["senha"] == novo_vendedor["senha"]:
            senha_existente = True
        if vendedor["telefone"] == novo_vendedor["telefone"]:
            telefone_existente = True
        if vendedor["cnpj"] == novo_vendedor["cnpj"]:
            cnpj_existente = True


    if email_existente:
        print("Email já cadastrado.")
    elif login_existente:
        print("Nome de login já cadastrado.")
    elif senha_existente:
        print("Senha já cadastrada.")
    elif telefone_existente:
        print("Telefone já cadastrado.")
    elif cnpj_existente:
        print("CNPJ já cadastrado.")
    else:
        vendedores_cadastrados.append(novo_vendedor)
        print("Cadastro de vendedor realizado com sucesso!")

def gerenciar_produtos_informacoes():
    email_login = input("Digite o email (login) do vendedor: ")
    senha = input("Digite a senha do vendedor: ")

    vendedor_encontrado = None
    for vendedor in vendedores_cadastrados:
        if vendedor["email"] == email_login and vendedor["senha"] == senha:
            vendedor_encontrado = vendedor

    if vendedor_encontrado:
        print("\nBem-vindo(a),", vendedor_encontrado["nome"])

    while True:
        print("MENU")
        print("1 - Atualizar senha de login")
        print("2 - Cadastrar novo produto")
        print("3 - Remover produto")
        print("4 - Buscar produto")
        print("5 - Atualizar valor do produto")
        print("6 - Listar compras feitas pelo usuário.")
        print("7 - Digite o nome do produto para ver sua descrição")
        print("8 - Sair do gerenciamento de produtos e informações")


        

        opcao_2 = int(input("Digite o número da opção desejada: "))

        if opcao_2 == 1:
            atualizar_senha_login()

            nova_senha = input("Digite a nova senha de login: ")
            vendedor_encontrado["senha"] = nova_senha
            print("Senha atualizada com sucesso!")
        
        elif opcao_2 == 2:
            novo_produto = {}
            novo_produto["nome"] = input("\nDigite o nome do produto: ")
            novo_produto["codigo"] = input("Digite o código do produto: ")
            novo_produto["marca"] = input("Digite a marca do produto: ")
            novo_produto["valor"] = float(input("Digite o valor do produto: "))
            novo_produto["descricao"] = input("\nDigite a descrição do produto: ")
            

            codigo_existente = False
            for produto in produtos_cadastrados:
                if produto["codigo"] == novo_produto["codigo"]:
                    codigo_existente = True

            if codigo_existente:
                print("Código já cadastrado.")
            else:
                produtos_cadastrados.append(novo_produto)
                print("Cadastro de produto realizado com sucesso!")

        elif opcao_2 == 3:
            codigo_produto = input("\nDigite o código do produto que deseja remover: ")

            produto_encontrado = None
            for produto in produtos_cadastrados:
                if produto["codigo"] == codigo_produto:
                    produto_encontrado = produto

            if not produto_encontrado:
                print("Código de produto não encontrado.")
            else:
                produtos_cadastrados.remove(produto_encontrado)
                print("Produto removido com sucesso!")

        elif opcao_2 == 4:
            nome_descricao_produto = input("\nDigite o Nome ou descrição do produto que deseja buscar: ")

            produto_encontrado = None
            for produto in produtos_cadastrados:
                if produto["nome"] == nome_descricao_produto or produto["descricao"] ==  nome_descricao_produto:
                    produto_encontrado = produto

            if not produto_encontrado:
                print("\nNome ou descrição do produto não encontrada.\n")
            else:
                print("Nome:", produto_encontrado["nome"])
                print("Marca:", produto_encontrado["marca"])
                print("Valor:", produto_encontrado["valor"])

                decisao_de_compra = input("\nDeseja comprar o produto? Digite: sim ou não. ")

                if decisao_de_compra == "sim".lower():
                    print("\n Compra realizada com sucesso !")
                    produtos_comprados.append(produto_encontrado)
                    produtos_cadastrados.remove(produto_encontrado)
                else :
                    print("\n Compra não realizada.")

        elif opcao_2 == 5:
            codigo_produto = input("\nDigite o código do produto que deseja atualizar o valor: ")

            produto_encontrado = None
            for produto in produtos_cadastrados:
                if produto["codigo"] == codigo_produto:
                    produto_encontrado = produto

            if not produto_encontrado:
                print("Código de produto não encontrado.")
            else:
                novo_valor = float(input("Digite o novo valor do produto: "))
                produto_encontrado["valor"] = novo_valor
                print("Valor do produto atualizado com sucesso.")

        elif opcao_2 == 6:
            contador_produtos_comprados = 0
            for produto in produtos_comprados:
                contador_produtos_comprados = contador_produtos_comprados + 1
                print(produto)
                print(contador_produtos_comprados)

        
        elif opcao_2 == 7:
            nome_produto = input("Digite o nome do produto para ver sua descrição: ")
            for produto in produtos_cadastrados :
                if produto["nome"] == nome_produto:
                    print(produto["descricao"])


        elif opcao_2 == 8:
            print("\nFechando gerenciamento de produtos e informações")
            break

def menu_principal():
    while True:
        print("\nMENU")
        print("1 - Cadastro de Vendedor")
        print("2 - Gerenciamento de Produtos e Informações do Vendedor")
        opcao = int(input("\nDigite o número da opção desejada: "))

        if opcao == 1:
            cadastrar_vendedor()
        elif opcao == 2:
            gerenciar_produtos_informacoes()
        else:
            print("\nEntrada incorreta. Selecione 1 ou 2.")

menu_principal()


