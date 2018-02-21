#written for http://codegolf.stackexchange.com/questions/79207/minimize-those-ones

def find1(num):
 z = 10
 y = 11
 while True:
  if num%z==0:
   if num/2 <= y/2:
    print(num)
    break
   else:
    print(num/y+num%y)
    break
  z += 10

def main():
 cases = [0,7,121,72,1000,2016]
 for th in range(0,5):
  find1(cases[th - 1])

if __name__ == '__main__':
 main()
