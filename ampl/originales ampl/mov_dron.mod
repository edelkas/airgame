#Datos (Conjuntos y parámetros)
#Conjuntos:
set C;			#Conjunto de condicionantes
set L;			#Conjunto de casillas en las que movilizar el dron

#Parámetros:
param Y {i in C} >=0;	#Coeficiente de importancia de cada condicionante a cada acción
param S {i in C} binary;	#Se da o no cada condicionante
param D {j in L} >=0;	#Distancia de la casilla a la base aérea desde donde se despliega

#Variables:
var X {j in L} binary;	#Decisión sobre si se lleva a cabo la acción o no

#Función objetivo: Maximizar la puntuación en función de escoger una casilla u otra
maximize FO: sum {i in C, j in L} [Y[i] * S[i]] * X[j];

#Restricciones:
#1) No se puede colocar el mismo avión de caza en más de una casilla
R1 sum X[j] =1

#2) La distancia de la casilla debe ser igual o inferior al alcance máximo del dron
R2 D[j] <=16
