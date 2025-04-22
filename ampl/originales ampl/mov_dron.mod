#Datos (Conjuntos y par�metros)
#Conjuntos:
set C;			#Conjunto de condicionantes
set L;			#Conjunto de casillas en las que movilizar el dron

#Par�metros:
param Y {i in C} >=0;	#Coeficiente de importancia de cada condicionante a cada acci�n
param S {i in C} binary;	#Se da o no cada condicionante
param D {j in L} >=0;	#Distancia de la casilla a la base a�rea desde donde se despliega

#Variables:
var X {j in L} binary;	#Decisi�n sobre si se lleva a cabo la acci�n o no

#Funci�n objetivo: Maximizar la puntuaci�n en funci�n de escoger una casilla u otra
maximize FO: sum {i in C, j in L} [Y[i] * S[i]] * X[j];

#Restricciones:
#1) No se puede colocar el mismo avi�n de caza en m�s de una casilla
R1 sum X[j] =1

#2) La distancia de la casilla debe ser igual o inferior al alcance m�ximo del dron
R2 D[j] <=16
