# 🔢 Solver de Otimização Inteira com Branch and Bound

Durante as aulas de Operation Research decidi implementar as soluções das questões apresentadas através de algoritmos em Python e apartir desta ideia que surge este projeto, que implementa um **Solver de Otimização Inteira** utilizando uma abordagem baseada em **Gradiente Discreto e Branch and Bound**. Ele permite a **maximização** de uma função objetivo sujeita a **restrições lineares**, considerando apenas **variáveis inteiras**.

O objetivo no futuro é evoluir esta solução para uma **biblioteca Python robusta**, que possa ser utilizada de forma modular em projetos de otimização, como para funções contínuas e mais complexas.

---

## ⚙️ **Instalação**

### 🔹 **Requisitos**

- **Python 3.12.7**
- **Poetry** (Gerenciador de dependências)

### 🔹 **Passos de Instalação**

1. **Clone o repositório**:

   ```bash
   git clone https://github.com/Bruno-Gomes-QA/Solver.git
   cd Solver
   ```

2. **Crie um ambiente virtual com Poetry**:

   ```bash
   poetry env use python3.12
   ```

3. **Instale as dependências**:

   ```bash
   poetry install
   ```
---

## 🚀 **Como Executar?**

O solver pode ser utilizado diretamente no Python. Veja um exemplo de uso:

```python
from solver import Model

# Criando o modelo de otimização
model = Model("Problema de Otimização")
model.integer_var("x1", initial_value=0)
model.integer_var("x2", initial_value=0)
model.integer_var("x3", initial_value=0)

# Definindo a função objetivo
model.maximize("4*x1 + x2 + 3*x3")

# Adicionando restrições
model.add_constraint("9*x1 + x2 + 2*x3 <= 18")

# Executando o solver
model.solve()
```

Ao executar esse código, o solver encontrará a **melhor solução inteira** para o problema.

---

## 🎯 **Objetivo do Projeto**

O objetivo principal desta solução é criar um **solver eficiente e personalizável** para otimização de variáveis inteiras. No futuro, pretendo transformar este projeto em uma **biblioteca Python de código aberto**, facilitando seu uso e integração em diferentes sistemas.

📌 **Próximos Passos para a biblioteca:**

- Melhorar a performance do algoritmo com heurísticas avançadas.
- Criar uma API mais intuitiva e modular para facilitar o uso.
- Implementar suporte a otimizações com mais restrições complexas.

---

## 🏆 **Soluções Existentes e Mais Completas**

Este projeto visa ser uma alternativa didática e flexível a **ferramentas mais robustas**, como:

| Solução             | Descrição                                                                                  | Tipo                   |
| ------------------- | ------------------------------------------------------------------------------------------ | ---------------------- |
| **Pulp**            | Framework de programação linear em Python, suporta otimização inteira e contínua.          | **Programação Linear** |
| **Gurobi**          | Um dos otimizadores mais poderosos para programação linear e inteira. Usado em indústrias. | **Solver Comercial**   |
| **Google OR-Tools** | Pacote avançado do Google para problemas de otimização combinatória.                       | **Open-source**        |

💡 **O diferencial deste projeto** é a abordagem de aprendizado e experimentação, visando uma solução que possa ser adaptada para diferentes tipos de problemas de otimização.

---

## 📌 **Contribuições e Feedback**

Se você tiver sugestões ou quiser contribuir para o projeto, sinta-se à vontade para abrir **Issues** ou enviar um **Pull Request**! Quero transformar este solver em uma ferramenta poderosa para toda a comunidade. 🚀

---

## 📄 **Licença**

Este projeto está licenciado sob a **MIT License** - veja o arquivo [`LICENSE`](LICENSE) para mais detalhes.

