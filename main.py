# 1- Import the random module
import random

# 2-
subject = [
  "Sheeba merlyn",
  "Virat kohli ",
  "Nirmala sitaraman",
  "Group of Monkey",
  "Valentine Week "
  "Hyderabad ek prem kahani "

] 

actions = [
  "Studing data scientist",
  "Dances with ",
  "Income tex",
  "Forest",
  "Hyderabad Tech Jobs",
  "solo traveller"
]

places_or_thinks = [
  "AT red fort",
  "Mumbai local train",
  "hyderabad chaaarminnar",
  "inside parliyament",
  "The ganga ghat ",
  "GVk mall"

]

# 3- start the headling genration 
while True:
  subject = random.choice(subject)
  action = random.choice(actions)
  places_or_thinks = random.choice(places_or_thinks)

  headline = f" BREAKING NEWS: {subject} {action} {places_or_thinks}"
  print("\n" + headline)

  user_input = input("\n Do you want another headline? (yes/no)").strip().lowe()
  if user_input == "no":
      break
 # print good bye message
print("\n thanks for using the fake news headline Genrater. have a fun day") 