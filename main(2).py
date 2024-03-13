from art import logo, vs
from game_data import data
import random
from replit import clear
print(logo)


count = 0
# Generate a random account from the game data.
def get_random_name():
  
  names = [item['name'] for item in data]
  random_name = random.choice(names)
  return random_name

def get_random_description(randomName):
  descriptions = [item['description'] for item in data if item['name'] ==   randomName]
  return descriptions

def get_random_country(randomName):
  countries = [item['country'] for item in data if item['name'] ==   randomName]
  return countries
  
def get_random_follower(randomName):
  follower =[item['follower_count'] for item in data if item['name'] ==   randomName]
  return follower

randomName = get_random_name()
randomDescription = get_random_description(randomName)
randomCountry = get_random_country(randomName)
randomFollower = get_random_follower(randomName)
  
randomName2 = get_random_name()
if randomName2 == randomName:
  randomName2 = get_random_name()
randomDescription2 = get_random_description(randomName2)
randomCountry2 = get_random_country(randomName2)
randomFollower2 = get_random_follower(randomName2)


playing = True


print(f"Compare A: {randomName}, {', '.join(randomDescription)}, from {', '.join(randomCountry)}")

print(vs)

print(f"Against B: {randomName2}, {', '.join(randomDescription2)}, from {', '.join(randomCountry2)}")

answer = input("Who has more followers? Type 'A' or 'B': ").upper()

while playing:
  
  if answer == "A" and randomFollower > randomFollower2:
    clear()
    print(logo)
    count += 1
    print(f"You are right! Current score: {count}. ")
    randomName2 = get_random_name()  
    randomDescription2 = get_random_description(randomName2)
    randomCountry2 = get_random_country(randomName2)
    randomFollower2 = get_random_follower(randomName2)

    print(f"Compare A: {randomName}, {', '.join(randomDescription)}, from {', '.join(randomCountry)}")
    print(vs)
    print(f"Against B: {randomName2}, {', '.join(randomDescription2)}, from {', '.join(randomCountry2)}")
    answer = input("Who has more followers? Type 'A' or 'B': ").upper()

  
  elif answer == "B" and randomFollower < randomFollower2:
    clear()
    print(logo)
    count+=1
    print(f"You are right! Current score: {count}. ")
    randomName = randomName2
    randomDescription = randomDescription2
    randomCountry = randomCountry2
    randomFollower = randomFollower2
  
    randomName2 = get_random_name()
    randomDescription2 = get_random_description(randomName2)
    randomCountry2 = get_random_country(randomName2)
    randomFollower2 = get_random_follower(randomName2)
    print(f"Compare A: {randomName}, {', '.join(randomDescription)}, from {', '.join(randomCountry)}")
    print(vs)
    print(f"Against B: {randomName2}, {', '.join(randomDescription2)}, from {', '.join(randomCountry2)}")
    answer = input("Who has more followers? Type 'A' or 'B': ").upper()

  else:
    clear()
    print(f"You are wrong. Your final score is: {count}\nYou loose")
    playing = False