function fizzBuzz()
{
for (var x = 0; x <= 100; x++)
{
	if (x % 15 == 0 && x != 0)
	{
	console.log("FizzBuzz"); //document.getElementById("fb").innerHTML = "FizzBuzz<br>"; 
	}
	else if (x % 3 == 0 && x != 0)
	{
	console.log("Fizz"); //document.getElementById("fb").innerHTML = "Fizz<br>"; 
	}
	else if (x % 5 == 0 && x != 0)
	{
	console.log("Buzz"); //document.getElementById("fb").innerHTML = "Buzz<br>"; 
	}
	else
	{
	console.log(x); //document.getElementById("fb").innerHTML = x; 
	}
}
}
window.onload = function() {
  fizzBuzz();
}