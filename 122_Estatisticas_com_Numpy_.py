import numpy as np
array_np = np.array(range(100))
print(array_np)

# Numero minimo
print(array_np.min())
# Numero maximo
print(array_np.max())
# Media do range
print(array_np.mean())
# Mediana do range
print(np.median(array_np))
# Amplitude do range
print(array_np.ptp())
# Percentis & quartis
np.quantile(array_np,0.25) # 25% do range
np.quantile(array_np,0.5)  # 50% do range
np.quantile(array_np,0.75) # 75% do range
np.quantile(array_np,0.10) # 10% do range 

### Desvio padrao ###
print(array_np.std().round(2)) # Desvio padrao
