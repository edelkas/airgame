#Datos (Conjuntos y par�metros)
#Conjuntos:
set C;				#Conjunto de condicionantes
set A;				#Conjunto de acciones que se pueden tomar

#Par�metros:
param Y {i in C, j in A} >= 0; #Coeficiente de importancia de cada condicionante a cada acci�n
param S {i in C} binary;       #Se da o no cada condicionante
param K {j in A} >= 0;         #Coste de la acci�n a tomar
param P >= 0;                  #Presupuesto actual

#Variables:
var X {j in A} binary;         #Decisi�n sobre si se lleva a cabo la acci�n o no

#Funci�n objetivo: Maximizar puntuaci�n obtenida por las acciones llevadas a cabo
maximize FO: sum {i in C, j in A} Y[i,j] * S[i] * X[j];

#Restricciones:
#1) La suma de los costes de las acciones debe ser inferior o igual al presupuesto actual
s.t. R1: sum {j in A} K[j] * X[j] <= P

#2) La relaci�n puntuaci�n de la acci�n realizada / coste de la acci�n debe ser mayor que 3
s.t. R2 {j in A}: sum {i in C} Y[i,j] * S[i] / K[j] >= 3 * X[j] - 100000 * (1 - X[j])