set S:=1..5;
var x{S}>=0, integer;

maximize cost: 2*x[1]+x[2]+2*x[3]+x[4]+2*x[5];

s.t. con1: 3*x[1]+3*x[2]+2*x[3]+2*x[4]+3*x[5]<=13;
s.t. con2: 2*x[1]+x[2]+3*x[3]+x[4]+2*x[5]<=11;