import numpy as np

### Array Unidimensional ###

array_np = np.array([20, 30, 40, 50, 60, 70, 80, 90])
type(array_np)

print(array_np.shape)  # .shape mostra a quantidade de colunas e linhas
print(array_np.ndim)   # .ndim mostra a quantidade de 

### Array Multidimensional ###

array_np_2d = np.array( [ [1,2,3,4,5], [6,7,8,9,10] ] )
print(array_np_2d.shape)

### Matrizes ###

Matrix = np.matrix( [ [1,2,3], [4,5,6] ] )
print(Matrix.shape) 
print(type(Matrix))