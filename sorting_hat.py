#Sorting Hat!
Gryffindor=0
Ravenclaw=0
Slytherin=0
Hufflepuff=0

print('-------------------')
print('The Sorting Hat')
print('-------------------')

#Question 1
print('Question-1) Do you like Dawn or Dusk?')
print('  1) Dawn')
print('  2) Dusk')

Answer= int(input('Enter answer (1-2):'))

if Answer==1:
  Gryffindor+=1
  Ravenclaw+=1
elif Answer==2:
  Slytherin+=1
  Hufflepuff+=1
else:
  print('Wrong input')    

#Question 2
print("Question-2) When I'm dead, I want people to remember me as:")
print('  1) The Good')
print('  2) The Great')
print('  3) The Wise')
print('  4) The Bold')

Answer= int(input('Enter answer (1-4):'))

if Answer==1:
  Hufflepuff+=2
elif Answer==2:
  Slytherin+=2
elif Answer==3:
  Ravenclaw+=2
elif Answer==4:
  Gryffindor+=2
else:
  print('Wrong input')      

#Question 3
print('Question-3) What kind of instrument most pleases your ear?')
print('  1) The violin')
print('  2) The trumpet')
print('  3) The piano')
print('  4) The drum')

Answer= int(input('Enter Answer (1-4):'))

if Answer==1:
  Slytherin+=4
elif Answer==2:
  Hufflepuff+=4
elif Answer==3:
  Ravenclaw+=4
elif Answer==4:
  Gryffindor+=4
else:
  print('Wrong input')    


print("Gryffindor: ", Gryffindor)
print("Ravenclaw: ", Ravenclaw)
print("Slytherin: ", Slytherin)
print("Hufflepuff: ", Hufflepuff)

most_points= max(Gryffindor, Ravenclaw, Slytherin, Hufflepuff)

if Gryffindor == most_points: 
  print('🦁 Gryffindor!')
elif Ravenclaw == most_points:
  print('🐦‍⬛ Ravenclaw!')
elif Slytherin == most_points:
  print('🐍 Slytherin!')
else:
  print('🦡 Hufflepuff!')

  
