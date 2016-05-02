#written for http://codegolf.stackexchange.com/questions/78845/run-through-an-array

from random import*
def a(x,y):
 p=0
 for z in x:
  if random()>.5:x[p]=z+y
  p+=1
 print(x)
        
def main():
    test = [1, 2, 3, 4, 5]
    testAdds = [0, 1, 2, 3, 4]
    for l in testAdds:
        a(test, l)
		
if __name__ == '__main__':
    main()
