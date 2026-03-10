# 📦 Sistema de Controle de Estoque - Eletrônicos

Sistema de gerenciamento de estoque para loja de eletrônicos desenvolvido em Python, com interface de menu via terminal.

## ✨ Funcionalidades

- **Adicionar produto** — cadastra nome, preço e quantidade
- **Atualizar produto** — edita preço e quantidade de um produto existente
- **Excluir produto** — remove produto com confirmação
- **Visualizar estoque** — exibe todos os produtos com valor total do estoque

## 🚀 Como usar

**Pré-requisito:** Python 3.x instalado.

```bash
python sistema_estoque.py
```

O menu interativo será exibido no terminal:

```
==================================================
SISTEMA DE CONTROLE DE ESTOQUE - ELETRÔNICOS
==================================================
1 - Adicionar Produto
2 - Atualizar Produto
3 - Excluir Produto
4 - Visualizar Estoque
5 - Sair do Sistema
==================================================
```

## 📁 Estrutura

```
sistema_estoque.py   # Arquivo principal
```

## ⚙️ Detalhes técnicos

- Os dados são armazenados **em memória** (dicionário Python) — não há persistência entre execuções
- Validações de entrada para preço (float ≥ 0) e quantidade (int ≥ 0)
- Confirmação obrigatória antes de excluir um produto

## 🔮 Melhorias futuras

- [ ] Persistência de dados com arquivo JSON ou banco de dados SQLite
- [ ] Busca/filtro de produtos
- [ ] Alerta de estoque baixo
- [ ] Histórico de movimentações

## 📄 Licença

Este projeto está sob a licença MIT.
