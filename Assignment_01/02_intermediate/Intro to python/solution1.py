# MARS Weight 
# Hamara weight earth pr 
def main():

  earth_weight = float(input("Enter a weight on Earth: "))

  # Calculate the weight on mars 
  mars_weight = earth_weight * 0.378

#Round the result to 2 Decimal places
  mars_weight = round(mars_weight)

#output the equivalent weight on mars 
  print(f"The equivalent on Mars: {mars_weight}")


# PLANETARY WEIGHT CALCULATOR 
# PLANET GRAVITY CONSTANT'S COMPARED TO EARTH'S GRAVITY 
  gravity_factors = {
    'Mercury': 0.376,
    'Venus ': 0.889,
    'Mars' :0.378,
    'Jupiter':2.36,
    'Saturn': 1.081,
    'Uranus':0.815,
    'Neptune':1.14,
}

#Prompt the user for their weight on earth 

  earth_weight = float (input("Enter a weight on Earth: "))

# PROmpt the user for the planet they are interested in 
  planet = input ("Enter a planet : ")

#Check if the planet is valid
  if planet in gravity_factors:

    planet_weight = earth_weight * gravity_factors[planet]

    planet_weight = round(planet_weight,2)

    print(f"The equivalent weight on {planet}: {planet_weight}")

  else:
    print("Invalid planet name. Please enter a valid planet. ")    

if __name__ == "__main__":
    main()
