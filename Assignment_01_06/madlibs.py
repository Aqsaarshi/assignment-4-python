# ------- MADLIBS GAME -----------
name = input("Name: ")
animal = input("Animal: ")
adj = input("Adjective: ")
verb = input("Verb: ")
place = input("Place: ")
number = input("Number: ")
food = input("Food: ")
sound = input("Sound: ")

madlibs = f"""Today, I went to the zoo with my friend {name}. 
We saw a(n) {adj} {animal} that could {verb}!
It was so crazy! Then we walked to the {place} where we fed it {number} {food}s.
Suddenly, it made a loud {sound.upper()} and ran away! What a wild day!
"""

print("\n" + madlibs)
