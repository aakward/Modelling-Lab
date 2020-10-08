param N;
param M;
set S:=1..N;
set T:=1..M;
var x{S,T}>=0;
param COSTS{S,T};

minimize cost: sum{i in S,j in T}x[i,j]*COSTS[i,j];

s.t. con1{i in S}: sum{j in T}x[i,j]=1;
s.t. con2{j in T}: sum{i in S}x[i,j]=1;
s.t. con3: x[1,2]=0;
s.t. con4: x[11,11]=0;
s.t. con5: x[8,8]=0;
