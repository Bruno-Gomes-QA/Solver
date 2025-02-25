from model import Model

# Criar modelo
model = Model('Maximização Inteira')

# Adicionar variáveis contínuas
model.integer_var('x3', initial_value=0.0)
model.integer_var('x1', initial_value=0.0)
model.integer_var('x2', initial_value=0.0)

# Definir função objetivo
model.maximize('100*x3 + 4*x1 + x2')

# Adicionar restrições
model.add_constraint('180*x3 + 9*x1 + x2 <= 360')
model.add_constraint('60*x3 + 3*x1 + x2 <= 240')

# Resolver
model.solve()
