#written for http://codegolf.stackexchange.com/questions/78845/run-through-an-array

from random import*
def a(x,y):
 ptr=0
 for z in x:
  if random()>0.5:
   x[ptr]=z+y
  ptr+=1
 print(x)
        
def main():
    test = [1, 2, 3, 4, 5]
    testAdds = [0, 1, 2, 3, 4]
    for l in testAdds:
        a(test, l)
		
if __name__ == '__main__':
    main()
