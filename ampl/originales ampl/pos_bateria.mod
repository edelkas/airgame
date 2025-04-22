#Datos (Conjuntos y parámetros)
#Conjuntos:
set C;			#Conjunto de condicionantes
set L;			#Conjunto de casillas en las que colocar la batería

#Parámetros:
param Y {i in C} >=0;	#Coeficiente de importancia de cada condicionante a cada acción
param S {i in C} binary;	#Se da o no cada condicionante
param A {j in L} binary;	#Existe superioridad aérea del propio jugador o no en esa casilla

#Variables:
var X {j in L} binary;	#Decisión sobre si se lleva a cabo la acción o no

#Función objetivo: Maximizar la puntuación en función de escoger una casilla u otra
maximize FO: sum {i in C, j in L} [Y[i] * S[i]] * X[j];

#Restricciones:
#1) No se puede colocar el mismo radar en más de una casilla
R1 sum X[j] =1

#2) Se debe colocar el radar en una casilla con superioridad aérea del propio jugador
R2 A[j] =1
