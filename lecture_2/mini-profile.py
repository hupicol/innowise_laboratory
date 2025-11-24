while True:

  user_name=input("Enter you full name: ")
  if not user_name:
        print("Name cannot be empty(")
        continue
  if any(char.isdigit() for char in user_name):
      print("Name should not contain numbers(")
      continue
  parts = user_name.split()
  if len(parts) < 2:
      print("Please enter your full name correctly")
      continue

  break


while True:
  birth_year_str=input("Enter your birth year: ")
  birth_year=int(birth_year_str)
  current_age = 2025 - birth_year
  if current_age < 0 or current_age > 120:
      print("Age seems incorrect. Try again.")
      continue
  if not birth_year_str.isdigit():
      print("Please enter numbers only")
      continue

  break

def generate_profile(current_age):
    if current_age<=12:
        stage="Child"
        return stage
    elif (current_age>=13)and(current_age<=19):
        stage="Teenager"
        return stage
    else:
        stage="Adult"
        return stage
life_stage=generate_profile(current_age)
hobbies=[]
while True:
    hobby=input("Enter a favourite hobby or type 'stop' to finish: ")
    if any(char.isdigit() for char in hobby):
        print("Hobby should not contain numbers(")
        continue
    if hobby.lower()=="stop":
        break
    hobbies.append(hobby)
user_profile={'name':user_name,'age':current_age,'stage':life_stage,'hobbies':hobbies}
print(f"----------")
print(f"Profile Summary:")
print(f"Name: {user_profile['name']}")
print(f"Age: {user_profile['age']}")
print(f"Life Stage: {user_profile['stage']}")
if user_profile['hobbies']==[]:
    print(f"You didn't mention any hobbies..")
else:
    print(f"Favourite hobbies({len(user_profile['hobbies'])}):")
    for hobby in user_profile['hobbies']:
        print(f"-{hobby}")
print(f"----------")