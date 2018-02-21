program sumAverageIO;
const
  numInt = 5;
var
  n1, n2, n3, n4, n5, sum : integer;
  average : real;
begin
  writeln ('Enter 5 numbers separated by spaces: ');
  readln (n1, n2, n3, n4, n5);
  sum := n1 + n2 + n3 + n4 + n5;
  average := sum / numInt;
  writeln ('Number of integers = ', numInt);
  writeln ('Number 1: ', n1:10);
  writeln ('Number 2: ', n2:10);
  writeln ('Number 3: ', n3:10);
  writeln ('Number 4: ', n4:10);
  writeln ('Number 5: ', n5:10);
  writeln ('====================');
  writeln ('Sum: ', sum:15);
  writeln ('Average: ', average:13:1);
  readln
end.

