class Queue:

  # queue class constructor
    def __init__(self):
        self.queue = ["car", "car", "car", "car", "car"]
   
  
    def enqueue(self):
        item = input("Please enter the item you wish to add to the queue: ")
        self.queue.append(item)
   
  
   
    def dequeue(self):
        item = self.queue.pop(0)
        print("You have just removed item from queue: ", item)
    
   
  
    def size(self):
        for x in range (len(self.queue)):
            print(self.queue[x])

queue = Queue()
newitem = Queue()

while True:
    
    print("")
    print("Python Implementation of a Queue")
    print("********************************")
    print("1. Create a new object")
    print("2. Add a new item to the queue")
    print("3. Remove item from the queue")

    print("********************************")
    menu_choice = int(input("Please enter your menu choice: "))
    print("")
    print("")
    
    if menu_choice == 1:
        newitem.enqueue()
    elif menu_choice == 2:
        queue.enqueue()
    elif menu_choice == 3:
        queue.dequeue()
    
   
  
 
   



    