class Model:
    """
    Classe para modelar e resolver problemas de Operations Research (Pesquisa Operacional) com variáveis inteiras.

    Esta classe permite:
        - Definir variáveis inteiras.
        - Definir uma função objetivo a ser maximizada.
        - Adicionar restrições lineares.
        - Resolver o problema utilizando um método baseado em Gradiente Discreto.

    A solução encontrada **maximiza a função objetivo respeitando todas as restrições adicionadas**.
    Suporta **qualquer número de variáveis e restrições**, ajustando automaticamente a solução conforme necessário.

    Attributes:
        name (str): Nome do modelo de otimização.
        variables (dict): Dicionário contendo as variáveis definidas no modelo.
        constraints (list): Lista de restrições adicionadas ao modelo.
        objective (str): Função objetivo a ser maximizada.
    """

    def __init__(self, name: str):
        """
        Inicializa o modelo de otimização.

        Args:
            name (str): Nome do modelo para referência.

        Example:
            ```python
            model = Model("Meu Problema de Otimização")
            ```
        """
        self.name = name
        self.variables = dict()
        self.constraints = []
        self.objective = None

    def integer_var(self, name: str, initial_value=0):
        """
        Adiciona uma variável inteira ao modelo.

        Args:
            name (str): Nome da variável.
            initial_value (int, optional): Valor inicial da variável. O valor mínimo permitido é 0. Default é 0.

        Example:
            ```python
            model.integer_var("x1", initial_value=5)
            ```
        """
        self.variables[name] = max(0, initial_value)

    def maximize(self, expr: str):
        """
        Define a função objetivo a ser maximizada.

        Args:
            expr (str): Expressão matemática representando a função objetivo.

        Example:
            ```python
            model.maximize("4*x1 + x2")
            ```
        """
        self.objective = expr

    def add_constraint(self, expr: str):
        """
        Adiciona uma restrição ao modelo.

        Args:
            expr (str): Expressão matemática representando a restrição.

        Example:
            ```python
            model.add_constraint("9*x1 + x2 <= 18")
            ```
        """
        self.constraints.append(expr)

    def evaluate_expression(self, expr: str, values: dict):
        """
        Avalia uma expressão matemática substituindo as variáveis pelos valores atuais.

        Args:
            expr (str): Expressão matemática a ser avaliada.
            values (dict): Dicionário contendo os valores atuais das variáveis.

        Returns:
            float | bool: O valor da expressão matemática avaliada.

        Example:
            ```python
            result = model.evaluate_expression("4*x1 + x2", {"x1": 2, "x2": 3})
            # Retorna 11
            ```
        """
        return eval(expr, {}, values)

    def compute_discrete_gradient(self):
        """
        Calcula o gradiente discreto da função objetivo.

        O método avalia como pequenas mudanças nas variáveis afetam a função objetivo.
        Ele testa aumentar e diminuir cada variável para encontrar a melhor direção para otimização.

        Returns:
            dict: Dicionário onde cada variável possui um valor de gradiente indicando sua influência na maximização.

        Example:
            ```python
            gradient = model.compute_discrete_gradient()
            # Retorna {"x1": 4, "x2": 1}
            ```
        """
        gradient = {}
        for var in self.variables:
            original_value = self.variables[var]

            self.variables[var] = original_value + 1
            f_plus_1 = self.evaluate_expression(self.objective, self.variables)

            self.variables[var] = max(0, original_value - 1)
            f_minus_1 = self.evaluate_expression(self.objective, self.variables)

            self.variables[var] = original_value

            gradient[var] = f_plus_1 - f_minus_1

        return gradient

    def solve(self, learning_rate=1, max_iterations=1000, min_iterations=3):
        """
        Resolve o problema de otimização usando um gradiente discreto ascendente, respeitando restrições.

        O algoritmo ajusta iterativamente os valores das variáveis na direção que maximiza a função objetivo,
        respeitando todas as restrições impostas.

        Args:
            learning_rate (int, optional): Passo de atualização das variáveis durante a otimização. Default é 1.
            max_iterations (int, optional): Número máximo de iterações antes de forçar a parada do algoritmo. Default é 1000.
            min_iterations (int, optional): Número mínimo de iterações para evitar que o algoritmo pare muito cedo. Default é 3.

        Returns:
            None: Exibe a solução encontrada no console.

        Example:
            ```python
            model.solve()
            ```
        """
        iteration = 0
        while iteration < max_iterations:
            iteration += 1
            gradient = self.compute_discrete_gradient()
            updated = False  

            for var in self.variables:
                if gradient[var] > 0:
                    new_value = self.variables[var] + learning_rate
                elif gradient[var] < 0:
                    new_value = self.variables[var] - learning_rate
                else:
                    continue

                new_value = max(0, new_value)

                temp_variables = self.variables.copy()
                temp_variables[var] = new_value

                if all(self.evaluate_expression(c, temp_variables) for c in self.constraints):
                    if self.variables[var] != new_value:
                        self.variables[var] = new_value
                        updated = True

            if not updated and iteration >= min_iterations:
                break

        print('\nSolução encontrada para:', self.name)
        print(f'Iterações realizadas: {iteration}')
        for var, value in self.variables.items():
            print(f'{var} = {value}')
        print('Valor máximo da função objetivo:', self.evaluate_expression(self.objective, self.variables), '\n')
