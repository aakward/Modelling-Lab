set S:=1..18;
var x{S}>=0, integer;   #xi denotes the no. of sheets that is to be cut in pattern i

minimize cost: sum{i in S}x[i];

s.t. con1: 5*x[1]+4*x[2]+3*x[3]+3*x[4]+2*x[5]+2*x[6]+2*x[7]+x[8]+x[9]+x[10]+x[11]>=2350;
s.t. con2: x[2]+2*x[5]+x[6]+3*x[8]+x[10]+4*x[12]+2*x[13]+2*x[14]+x[15]+x[16]>=970;
s.t. con3: x[3]+x[6]+2*x[9]+x[11]+x[14]+2*x[16]+x[17]>=6100;
s.t. con4: x[4]+x[10]+x[11]+x[13]+2*x[18]>=3950;
s.t. con5: x[7]+x[15]+x[17]>=2110;

