def do_grid(val=['', '', '', '', '', '', '', '', '']):
    larg=4
    print(f"  {val[0]:^{larg}}  |  {val[1]:^{larg}}  | {val[2]:^{larg}} ")
    print("________________________")
    print(f"  {val[3]:^{larg}}  |  {val[4]:^{larg}}  | {val[5]:^{larg}} ")
    print("________________________")
    print(f"  {val[6]:^{larg}}  |  {val[7]:^{larg}}  | {val[8]:^{larg}} ")

def choose(player):
   number=0
   while number<1 or number>9:
        print(f"Player {player}, choose a number from 1 to 9")
        while True:
           try:
              number= int(input())
              break
           except ValueError:
             print("Not valid number.")
   return number

def istictac(listof, last):
   if last in [0, 1, 2]:
      if listof[0] == listof[1] and listof[1]==listof[2]:
         return True
   elif last in [3, 4, 5]:
      if listof[3]==listof[4] and listof[4]==listof[5]:
         return True
   else:
      if listof[6]==listof[7] and listof[7]==listof[8]:
         return True
   if last in [0, 3, 6]:
      if listof[0]==listof[3] and listof[3]==listof[6]:
         return True
   elif last in [1, 4, 7]:
      if listof[1]==listof[4] and listof[4]==listof[7]:
         return True
   else:
      if listof[2]==listof[5] and listof[5]==listof[8]:
         return True
   if last in [0, 4, 8]:
      if listof[0]==listof[4] and listof[4]==listof[8]:
         return True
   if last in [2, 4, 6]:
      if listof[2]==listof[4] and listof[4]==listof[6]:
         return True
   return False
    
      
choice=input("Welcome to tic tac toe, player 1 and 2. Does player 1 want to start with O or X?")

while choice not in ['x', 'X', 'o', 'O']:
    choice=input("Insert a valid choice for this game!")
choice=choice.upper()
print(f"Perfect! Player 1 will start with {choice}")
if choice=='O':
    other='X'
else:
    other='O'

turns=0
tictac=False
listofchoices=['', '','','','','','','','']
print("Make the choices of the positions through the numbers 1-9, like this!")
do_grid([1, 2, 3, 4, 5, 6, 7, 8, 9])

while turns<9:
    while turns<9:
       number=choose(1)
       if listofchoices[number-1]=='':
          listofchoices[number-1]= choice
          turns+=1
          break
       else:
          print("Position occupied")
        
    print()
    do_grid(listofchoices)
    print()

    if turns>=5:
       if istictac(listofchoices, number-1):
          print()
          print("Player 1 has won!")
          tictac=True
          break
    
    
    while turns<9:
       number=choose(2)
       if listofchoices[number-1]=='':
          listofchoices[number-1]= other
          turns+=1
          break
       else:
          print("Position occupied")
    print()
    do_grid(listofchoices)
    print()

    if turns>=5:
       if istictac(listofchoices, number-1):
          print()
          print("Player 2 has won!")
          tictac=True
          break

if not tictac:
    print("Match ended with a draw")
    

