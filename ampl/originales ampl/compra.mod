#Datos (Conjuntos y parámetros)
#Conjuntos:
set C;				#Conjunto de condicionantes
set A;				#Conjunto de acciones que se pueden tomar

#Parámetros:
param Y {i in C, j in A} >=0;	#Coeficiente de importancia de cada condicionante a cada acción
param S {i in C} binary;		#Se da o no cada condicionante
param K {j in A} >=0;		#Coste de la acción a tomar
param P >=0;				#Presupuesto actual

#Variables:
var X {j in A} binary;		#Decisión sobre si se lleva a cabo la acción o no

#Función objetivo: Maximizar puntuación obtenida por las acciones llevadas a cabo
maximize FO: sum {i in C, j in A}	[Y[i, j] * S[i] ] * X[j];

#Restricciones:
#1) La suma de los costes de las acciones debe ser inferior o igual al presupuesto actual
R1 sum K[j] * X[j] <= P

#2) La relación puntuación de la acción realizada / coste de la acción debe ser mayor que 3
R2 {j in A}: [[Y[i, j] * S [i] ] * X [j]]/K[j] >=3
