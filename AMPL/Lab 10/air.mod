param n;

set N := 1..n;

var x{N} >= 0 integer;

param CAP{N};
param COST{N};
param SPACE{N};

maximize obj: sum{i in N}x[i]*CAP[i];

s.t. s_con: sum{i in N}x[i]*SPACE[i] <= 11;
s.t. b_con: sum{i in N}x[i]*COST[i] <= 13;

