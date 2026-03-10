"""
Sistema de Controle de Estoque para Loja de Eletrônicos
Desenvolvido em Python
"""

# Dicionário para armazenar os produtos do estoque
estoque = {}

def exibir_menu():
    """Exibe o menu principal do sistema"""
    print("\n" + "="*50)
    print("SISTEMA DE CONTROLE DE ESTOQUE - ELETRÔNICOS")
    print("="*50)
    print("1 - Adicionar Produto")
    print("2 - Atualizar Produto")
    print("3 - Excluir Produto")
    print("4 - Visualizar Estoque")
    print("5 - Sair do Sistema")
    print("="*50)

def adicionar_produto():
    """Adiciona um novo produto ao estoque"""
    print("\n--- ADICIONAR PRODUTO ---")
    
    nome = input("Nome do produto: ").strip()
    
    # Verifica se o produto já existe no estoque
    if nome in estoque:
        print(f"\nErro: O produto '{nome}' já existe no estoque!")
        print("Use a opção 'Atualizar Produto' para modificá-lo.")
        return
    
    # Validação do preço
    while True:
        try:
            preco = float(input("Preço do produto (R$): "))
            if preco < 0:
                print("Erro: O preço não pode ser negativo!")
                continue
            break
        except ValueError:
            print("Erro: Digite um valor numérico válido!")
    
    # Validação da quantidade
    while True:
        try:
            quantidade = int(input("Quantidade em estoque: "))
            if quantidade < 0:
                print("Erro: A quantidade não pode ser negativa!")
                continue
            break
        except ValueError:
            print("Erro: Digite um número inteiro válido!")
    
    # Adiciona o produto ao estoque
    estoque[nome] = {
        'preco': preco,
        'quantidade': quantidade
    }
    
    print(f"\n✓ Produto '{nome}' adicionado com sucesso!")

def atualizar_produto():
    """Atualiza as informações de um produto existente"""
    print("\n--- ATUALIZAR PRODUTO ---")
    
    if not estoque:
        print("\nEstoque vazio! Não há produtos para atualizar.")
        return
    
    nome = input("Nome do produto para atualizar: ").strip()
    
    # Verifica se o produto existe
    if nome not in estoque:
        print(f"\nErro: Produto '{nome}' não encontrado no estoque!")
        return
    
    print(f"\nProduto encontrado: {nome}")
    print(f"Preço atual: R$ {estoque[nome]['preco']:.2f}")
    print(f"Quantidade atual: {estoque[nome]['quantidade']}")
    
    # Atualização do preço
    while True:
        try:
            preco = float(input("\nNovo preço do produto (R$): "))
            if preco < 0:
                print("Erro: O preço não pode ser negativo!")
                continue
            break
        except ValueError:
            print("Erro: Digite um valor numérico válido!")
    
    # Atualização da quantidade
    while True:
        try:
            quantidade = int(input("Nova quantidade em estoque: "))
            if quantidade < 0:
                print("Erro: A quantidade não pode ser negativa!")
                continue
            break
        except ValueError:
            print("Erro: Digite um número inteiro válido!")
    
    # Atualiza o produto
    estoque[nome]['preco'] = preco
    estoque[nome]['quantidade'] = quantidade
    
    print(f"\n✓ Produto '{nome}' atualizado com sucesso!")

def excluir_produto():
    """Exclui um produto do estoque"""
    print("\n--- EXCLUIR PRODUTO ---")
    
    if not estoque:
        print("\nEstoque vazio! Não há produtos para excluir.")
        return
    
    nome = input("Nome do produto para excluir: ").strip()
    
    # Verifica se o produto existe
    if nome not in estoque:
        print(f"\nErro: Produto '{nome}' não encontrado no estoque!")
        return
    
    # Confirmação de exclusão
    confirmacao = input(f"\nTem certeza que deseja excluir '{nome}'? (S/N): ").strip().upper()
    
    if confirmacao == 'S':
        del estoque[nome]
        print(f"\n✓ Produto '{nome}' excluído com sucesso!")
    else:
        print("\nOperação cancelada.")

def visualizar_estoque():
    """Exibe todos os produtos do estoque"""
    print("\n--- ESTOQUE ATUAL ---")
    
    if not estoque:
        print("\nEstoque vazio! Nenhum produto cadastrado.")
        return
    
    print("\n" + "-"*70)
    print(f"{'PRODUTO':<30} {'PREÇO':<15} {'QUANTIDADE':<15}")
    print("-"*70)
    
    # Percorre todos os produtos do estoque
    for nome, dados in estoque.items():
        preco_formatado = f"R$ {dados['preco']:.2f}"
        quantidade = dados['quantidade']
        print(f"{nome:<30} {preco_formatado:<15} {quantidade:<15}")
    
    print("-"*70)
    print(f"Total de produtos cadastrados: {len(estoque)}")
    
    # Calcula o valor total do estoque
    valor_total = sum(dados['preco'] * dados['quantidade'] for dados in estoque.values())
    print(f"Valor total do estoque: R$ {valor_total:.2f}")

def main():
    """Função principal que executa o sistema"""
    print("\n🔌 Bem-vindo ao Sistema de Controle de Estoque! 🔌")
    
    while True:
        exibir_menu()
        
        opcao = input("\nEscolha uma opção: ").strip()
        
        if opcao == '1':
            adicionar_produto()
        elif opcao == '2':
            atualizar_produto()
        elif opcao == '3':
            excluir_produto()
        elif opcao == '4':
            visualizar_estoque()
        elif opcao == '5':
            print("\n" + "="*50)
            print("Encerrando o sistema...")
            print("Obrigado por utilizar o Sistema de Controle de Estoque!")
            print("="*50)
            break
        else:
            print("\n⚠ Opção inválida! Por favor, escolha uma opção de 1 a 5.")

# Execução do programa
if __name__ == "__main__":
    main()