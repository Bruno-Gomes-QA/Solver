from model import Model

# Criar modelo
model = Model('Maximização Inteira')

# Adicionar variáveis
model.integer_var('x1', initial_value=0.0)
model.integer_var('x2', initial_value=0.0)
model.integer_var('x3', initial_value=0.0)

# Definir função objetivo
model.maximize('4*x1 + x2 + 100*x3')

# Adicionar restrições
model.add_constraint('9*x1 + x2 + 180*x3 <= 360')
model.add_constraint('3*x1 + x2 + 60*x3 <= 240')

# Resolver
model.solve()
