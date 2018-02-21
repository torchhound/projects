program powersTwo;
Uses Math;
var
  a : integer;
  b : longint;
begin
  a := 1;
  b := 0;
  while b <= 20000 do
        begin
             b := 2 ** a;
             writeln (b);
             a := a + 1;
        end;
  readln
end.

