program sumAverage;
const
  numInt = 5;
var
  n1, n2, n3, n4, n5, sum : integer;
  average : real;
begin
     n1 := 45;
     n2 := 7;
     n3 := 68;
     n4 := 2;
     n5 := 34;
     sum := n1 + n2 + n3 + n4 + n5;
     average := sum / numInt;
     writeln ('Number of integers = ', numInt);
     writeln ('Number 1 = ', n1);
     writeln ('Number 2 = ', n2);
     writeln ('Number 3 = ', n3);
     writeln ('Number 4 = ', n4);
     writeln ('Number 5 = ', n5);
     writeln ('Sum = ', sum);
     writeln ('Average = ', average);
     readln
end.

