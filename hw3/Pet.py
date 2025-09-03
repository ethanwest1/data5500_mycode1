# Ethan Westenskow

# Create a class called Pet with attributes name and age. 
# Implement a method within the class to calculate the age of the pet in equivalent human years. 
# Additionally, create a class variable called species to store the species of the pet. 
# Implement a method within the class that takes the species of the pet as input and returns the average lifespan for that species.

    # Instantiate three objects of the Pet class with different names, ages, and species.
    # Calculate and print the age of each pet in human years.
    # Use the average lifespan function to retrieve and print the average lifespan for each pet's species.


class Pet:
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species.lower()
    
    # https://unleashpetphotography.com/animal-age-calculator
    def human_years(self): 
        if self.species == "dog":
            return self.age * 7
        elif self.species == "goldfish":
            return self.age * 18
        elif self.species == "cat":
            return self.age * 19
        else:
            return self.age * 5

    def avg_lifespan(self):
        lifespans = { 
    "dog": 12,
    "cat": 15,
    "goldfish": 10,
        }
        if self.species.lower() in lifespans:
            return lifespans[self.species.lower()]
        else:
            return "unknown"

Winnie = Pet("Winnie", 4, "Dog")
print(f"{Winnie.name} is approximately {Winnie.human_years()} years old if in human years.")
print(f"The average lifespan for a {Winnie.species} is {Winnie.avg_lifespan()}.")

Mitch = Pet("Mitch", 7, "Dog")
print(f"{Mitch.name} is approximately {Mitch.human_years()} years old if in human years.")
print(f"The average lifespan for a {Mitch.species} is {Mitch.avg_lifespan()}.")


Spirit = Pet("Spirit", 4, "Goldfish")
print(f"{Spirit.name} is approximately {Spirit.human_years()} years old if in human years.")
print(f"The average lifespan for a {Spirit.species} is {Spirit.avg_lifespan()}.")


# ChatGPT session transcript (Problem 3: Pet)
#
# Me: Let's move onto problem 3.
# ChatGPT: Outlined steps — class with name, age, species; method for human_years; 
#          method for average lifespan by species; instantiate 3 pets and print info.
#
# Me: First attempt:
#   def human_years(self): 
#       if species == "dog":
#           return self.age * 7
#       elif species == "goldfish":
#           return self.age * 18
#   Winnie = Pet("Winnie", 4, "Dog")
#   print(f"{self.name} is approximately {Winnie.human_years()}...")
# ChatGPT: Corrected mistakes — must use `self.species` not bare `species`, 
#          and can’t use `self` outside the class; must use object name instead.
#
# Me: Revised code with self.species and proper print.
# ChatGPT: ✅ Worked, produced correct output for Winnie.
#
# Me: Asked if this fully satisfies requirements.
# ChatGPT: Said almost — needed the average lifespan method and at least 3 pets.
#
# Me: Added `avg_lifespan` with dictionary: dog=12, cat=15, goldfish=10.
# ChatGPT: Approved, but pointed out assignment also requires a class variable `species`.
#
# Me: Asked how to add that.
# ChatGPT: Showed adding `species = "unknown"` at the top of the class, 
#          while still letting each pet override it in `__init__`.
#
# Final: Three pets (Winnie the dog, Mitch the dog, Spirit the goldfish) created. 
# Prints their human years and their species’ average lifespan.


        
