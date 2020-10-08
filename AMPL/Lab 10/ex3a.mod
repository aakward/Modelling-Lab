param n;   #no. of months
set S:=1..n;
var x{S}>=0,<=10000, integer; #Qty of steel wires manufactured in the i th month
param VCOST{S};
param D{S};  #demand in i th month
param h; #holding cost per month

minimize cost: sum{i in S}(x[i]*VCOST[i]+(12-i)*h*(x[i]-D[i]));

s.t. con{i in S}: sum{j in 1..i} (x[j]-D[j])>=0;
s.t. ucon: sum{i in S}(x[i]-D[i])=0;


