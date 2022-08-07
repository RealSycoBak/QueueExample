from queue import Queue
from colorama import init, Fore, Back, Style
import os
 
init(convert=False)
 
q = Queue()

def clear():
  os.system('clear')

def queue(ele):
  clear()
  intsructions()
  print(Fore.GREEN + f"\nEnqueued {ele}")
  q.put(ele)
  print("Current Size of Queue: ", q.qsize())

def intsructions():
  print(Fore.YELLOW + "type anything to add to the Queue")
  print(Fore.YELLOW + "type 'showqueue' to show the elements that are currently in queue")
  print(Fore.YELLOW + "type 'dequeue' to dequeue the first element that joined the queue")
  print(Fore.YELLOW + "type 'resetqueue' to reset Queue to empty")
  print(Fore.YELLOW + "type 'endprogram' to terminate the program" + Fore.RESET)

intsructions()
run = True
while run:
  b = input(Fore.WHITE + "\nWhat Do you Want to join the Queue? " + Fore.CYAN)
  if b == 'resetqueue':
    clear()
    intsructions()
    print(Fore.RED + "\nReset Queue")
    q.queue = []
  elif b == 'dequeue' and list(q.queue) != []:
    clear()
    intsructions()
    endofqueue = q.get()
    print(Fore.RED + f"\nDequeued {endofqueue}")
    print("New Size of Queue: ", q.qsize())
  elif b == 'showqueue':
    clear()
    intsructions()
    print(Fore.GREEN + "\nCurrent Queue")
    print(list(q.queue))
    print("Current Size of Queue: ", q.qsize())
  elif b == "endprogram":
    clear()
    print(Fore.RED + "ENDED PROGRAM, QUEUE DISBANDED")
    run = False
  else:
    queue(b) 


 
