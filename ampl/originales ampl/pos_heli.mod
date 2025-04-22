#Datos (Conjuntos y par�metros)
#Conjuntos:
set C;			#Conjunto de condicionantes
set B;			#Conjunto de bases a�reas en las que colocar el helicoptero

#Par�metros:
param Y {i in C} >=0;	#Coeficiente de importancia de cada condicionante a cada acci�n
param S {i in C} binary;	#Se da o no cada condicionante

#Variables:
var X {j in B} binary;	#Decisi�n sobre si se lleva a cabo la acci�n o no

#Funci�n objetivo: Maximizar la puntuaci�n en funci�n de escoger una base u otra
maximize FO: sum {i in C, j in B} [Y[i] * S[i]] * X[J];

#Restricciones:
#1) No se puede colocar el mismo helic�ptero en m�s de una base a�rea
R1 sum X[j] =1