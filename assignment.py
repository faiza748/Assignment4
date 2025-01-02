# python list exercises
# chap 3:Exercise 3-1: Names
names = ["sumaira","jaweria","saba","sana"]
print(names[0])
print(names[1])
print(names[2])
print(names[3])
#Exercise 3-2: Greetings
print(f"Hi {names[0]}! congrats on a great year!sending warm wishes to uh and ur family.")
print(f"Hi {names[1]}! congrats on a great year!sending warm wishes to uh and ur family.")
print(f"Hi {names[2]}! congrats on a great year!sending warm wishes to uh and ur family.")
print(f"Hi {names[3]}! congrats on a great year!sending warm wishes to uh and ur family.")
#Exercise 3-3: Your own list
transportation_modes = ["roadster","limousine","sports car","convertible"]
print(transportation_modes)
print(f"I would like to own a {transportation_modes[0]}.")
print(f"I would like to own a {transportation_modes[1]}.")
print(f"I would like to own a {transportation_modes[2]}.")
print(f"I would like to own a {transportation_modes[3]}.")
#Exercise 3-4:Guest list
invite_poeples = ["sania","aqsa","sana"]
print(invite_poeples)
print(f"Dear {invite_poeples[0]},I would be honored to invite uh to dinner.Please join me!")
print(f"Dear {invite_poeples[1]},I would be honored to invite uh to dinner.Please join me!")
print(f"Dear {invite_poeples[2]},I would be honored to invite uh to dinner.Please join me!")
#Exercise 3-5:changing guest list

print(f"apologize,{invite_poeples[0]}can't make it to dinner!")
invite_poeples[0] = "hina"
print("\nNew invitaion:")
print(f"Dear{invite_poeples},you are invited to dinner!")

#Exercise 3-6: More guest
invite_poeples = ["sania","aqsa","sana"]
print("I can invite more poeple")
invite_poeples.insert(0,"ayesha")
invite_poeples.insert(len(invite_poeples)//2,"mani")
invite_poeples.append("hira")
print(f"Hi{invite_poeples},you're invited to my dinner party")

#Exercise 3-7:Shrinking Guest List
invite_poeples = ['ayesha', 'sania', 'mani', 'aqsa', 'sana', 'hira']
print("Unfortunately, the new dinner table won't arrive in time. I can only invite two guests.")
while len(invite_poeples) > 2:
       removed_invite_people = invite_poeples.pop()
       print(f"Sorry {removed_invite_people}, I can't invite you to dinner.")
       print(f"{invite_poeples}, you're still invited to the dinner.")
# Removing the last two peoples
del invite_poeples[0]
del invite_poeples[0]
print("invite_people:",invite_poeples)
# Exercise 3-8:Seeing The World
fav_places = ["Paris", "Turkey", "Soudia_Arabia","Italy"]
print("Original list:",fav_places)
print("Alphabetical order:", sorted(fav_places))
print("Original list after sorted():",fav_places)
print("Reverse alphabetical order:", sorted(fav_places, reverse=True))
print("Original list after reverse sorted():", fav_places)
fav_places.reverse()
print("List after reverse():", fav_places)
fav_places.reverse()
print("List after reverse() again:", fav_places)
fav_places.sort()
print("List after sort():", fav_places)
fav_places.sort(reverse=True)
print("List after sort(reverse=True):", fav_places)
#Exercise 3-9: Dinner Guest
invite_poeples = ['ayesha', 'sania', 'mani', 'aqsa', 'sana', 'hira']
print(f"you're invited to dinner:",len(invite_poeples))
# Exercise 3-10: Every Function

languages = ["English", "Urdu", "Arabic", "Punjabi"]
print("Original list:", languages)
languages.append("Spanish")
print("After appending 'Spanish':", languages)
languages.insert(2, "French")
print("After inserting 'French' at position 2:", languages)
languages.remove("Urdu")
print("After removing 'Urdu':", languages)
popped_language = languages.pop()
print("After popping the last item:", languages)
print("Popped item:", popped_language)
languages.sort()
print("After sorting alphabetically:", languages)
languages.sort(reverse=True)
print("After sorting in reverse order:", languages)
print("List after temporary sort:", languages)
languages.reverse()
print("After reversing the list:", languages)
print("Length of the list:", len(languages))
#Exercise 3-11:Intentional Error
list = ["apple", "banana", "cherry"]
try:
  print(list[3])
except IndexError as e:
  print(f"IndexError occurred: {e}")
  print("Corrected access:", list[-1])
