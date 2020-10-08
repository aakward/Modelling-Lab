param N;
set S:=1..N;
var x{S}, binary;
param W{S,S};
var y{S,S}, binary;

maximize cost: sum{i in S,j in S}W[i,j]*(x[i]+x[j]-2*y[i,j])/2;

s.t. con1{i in S,j in S}: y[i,j]<=x[i];
s.t. con2{i in S,j in S}: y[i,j]<=x[j];
s.t. con3{i in S,j in S}: -1.4+x[j]+x[i]/2<=y[i,j];

