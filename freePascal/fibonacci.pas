program fibonacci;
var
  fibNum, a, b, c, count : integer;
begin
  writeln ('How many numbers of the Fibonacci sequence?');
  readln (fibNum);
  a := 0;
  b := 1;
  for count := 1 to fibNum do
      begin
           writeln (b:1);
           c := b;
           b := a + b;
           a := c;
      end;
  readln;
end.

