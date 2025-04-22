#Datos (Conjuntos y parámetros)
#Conjuntos:
set C;			#Conjunto de condicionantes
set B;			#Conjunto de bases aéreas en las que colocar el helicoptero

#Parámetros:
param Y {i in C} >=0;	#Coeficiente de importancia de cada condicionante a cada acción
param S {i in C} binary;	#Se da o no cada condicionante

#Variables:
var X {j in B} binary;	#Decisión sobre si se lleva a cabo la acción o no

#Función objetivo: Maximizar la puntuación en función de escoger una base u otra
maximize FO: sum {i in C, j in B} [Y[i] * S[i]] * X[J];

#Restricciones:
#1) No se puede colocar el mismo helicóptero en más de una base aérea
R1 sum X[j] =1