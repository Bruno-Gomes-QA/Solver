# Criando um gráfico corrigido para visualizar a navegação contínua
# np não existe
import numpy as np

# Criando uma grade de pontos para visualizar a função objetivo
x1_vals = np.linspace(0, 5, 100)
x2_vals = np.linspace(0, 10, 100)
X1, X2 = np.meshgrid(x1_vals, x2_vals)
Z = 4 * X1 + X2  # Função objetivo (lucro)

# Criando o gráfico
plt.figure(figsize=(8, 6))

# Contorno do lucro
contour = plt.contourf(X1, X2, Z, levels=20, cmap='coolwarm', alpha=0.6)
plt.colorbar(contour, label='Lucro')

# Recalculando as restrições corretamente para o eixo x1
x1 = np.linspace(0, 5, 100)
x2_1 = 18 - 9 * x1  # Restrição: 9x1 + x2 <= 18
x2_2 = 12 - 3 * x1  # Restrição: 3x1 + x2 <= 12

# Plotar as restrições corrigidas
plt.plot(x1, x2_1, label=r'$9x_1 + x_2 \leq 18$', color='red')
plt.plot(x1, x2_2, label=r'$3x_1 + x_2 \leq 12$', color='green')

# Preencher a região viável
plt.fill_between(
    x1,
    np.minimum(x2_1, x2_2),
    0,
    where=(np.minimum(x2_1, x2_2) >= 0),
    color='lightblue',
    alpha=0.5,
    label='Região Viável',
)

# Caminho da solução ótima contínua (exemplo de navegação)
nav_x = [0, 0.5, 1, 1.5, 2, 1]  # Exemplo de navegação suave até o ótimo
nav_y = [0, 2, 5, 7, 9, 9]
plt.plot(
    nav_x,
    nav_y,
    marker='o',
    linestyle='dashed',
    color='black',
    label='Navegação Suave',
)

# Solução ótima contínua
plt.scatter(
    x1_cont,
    x2_cont,
    color='blue',
    s=100,
    marker='*',
    label='Solução Ótima Contínua',
)

# Configuração do gráfico
plt.xlim(0, 5)
plt.ylim(0, 10)
plt.xlabel(r'$x_1$ (Mouses)')
plt.ylabel(r'$x_2$ (Teclados)')
plt.title('Navegação Contínua na Região Viável')
plt.legend()
plt.grid()

# Exibir o gráfico
plt.show()
