param N;
param M;
set S:=1..N;
set T:=1..M;
param b{T};
param c{S};
param A{T,S};
var x{S}>=0,<=1;

maximize cost: sum{i in S}c[i]*x[i];

s.t. ubcon{i in T}: sum{j in S}A[i,j]*x[j]<=b[i];

