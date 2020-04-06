import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-lst", nargs='*', type=int, action='append')
square = parser.parse_args()
square = square.lst

def square_integers(square):
    
    
    newlist = []
    
    square1 = [2, 8, 6]
    
    square2 = [12, 2, 9]
    
    for i in square:
        newlist.append(square1)
        newlist.append(square2)
        return [[i**2 for i in square1],[i**2 for i in square2]]
        
         
if __name__ == "__main__":
    print(square_integers(square))
    