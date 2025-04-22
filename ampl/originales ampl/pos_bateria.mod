#Datos (Conjuntos y par�metros)
#Conjuntos:
set C;			#Conjunto de condicionantes
set L;			#Conjunto de casillas en las que colocar la bater�a

#Par�metros:
param Y {i in C} >=0;	#Coeficiente de importancia de cada condicionante a cada acci�n
param S {i in C} binary;	#Se da o no cada condicionante
param A {j in L} binary;	#Existe superioridad a�rea del propio jugador o no en esa casilla

#Variables:
var X {j in L} binary;	#Decisi�n sobre si se lleva a cabo la acci�n o no

#Funci�n objetivo: Maximizar la puntuaci�n en funci�n de escoger una casilla u otra
maximize FO: sum {i in C, j in L} [Y[i] * S[i]] * X[j];

#Restricciones:
#1) No se puede colocar el mismo radar en m�s de una casilla
R1 sum X[j] =1

#2) Se debe colocar el radar en una casilla con superioridad a�rea del propio jugador
R2 A[j] =1
