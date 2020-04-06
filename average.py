import argparse

if __name__ == '__main__':
 
    parser = argparse.ArgumentParser(description="Code to calculate average of list")
    parser.add_argument('-lst', type=int, nargs='*', help="first number to add")
    parser.add_argument('num', type=int, nargs='*', help="second number to add")
    parser.add_argument('num', type=int, nargs='*', help="third number to add")
    parser.add_argument('num', type=int, nargs='*', help="fourth number to add")
    args = parser.parse_args()
 
    print(args.lst)

   
    def Average(lst): 
        return sum(lst) / len(lst) 
  
    
lst = [2, 3, 4]
lst = [4, 8, 10, 2]
    
average = Average(lst)
print("Average =", round(average))

    
  



 
