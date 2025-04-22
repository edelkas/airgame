#Datos (Conjuntos y parámetros)
#Conjuntos:
set C;			#Conjunto de condicionantes
set L;			#Conjunto de casillas a las que atacar con el avión de ataque

#Parámetros:
param Y {i in C} >=0;	#Coeficiente de importancia de cada condicionante a cada acción
param S {i in C} binary;	#Se da o no cada condicionante
param D {j in L} >=0;	#Distancia de la casilla a la aeronave desde donde se ataca

#Variables:
var X {j in L} binary;	#Decisión sobre si se lleva a cabo la acción o no

#Función objetivo: Maximizar la puntuación en función de escoger una casilla u otra
maximize FO: sum {i in C, j in L} [Y[i] * S[i]] * X[j];

#Restricciones:
#1) No se puede colocar el mismo avión de caza en más de una casilla
R1 sum X[j] =1

#2) La distancia de la casilla debe ser igual o inferior al alcance de ataque máximo de la aeronave
R2 D[j] <=11
