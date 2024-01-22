import numpy as np

# creating a person with a dictionary
person = {}


person["name"] = "andy"
person["age"] = 43
person["favorite_colors"] = ["aggie blue", "fighting white"]
person["hw_scores"] = [95, 80, 99]

print("person: ", person)
print(person["name"], person["age"], person["favorite_colors"])

# functions with dictionaries are separate
def calc_avg_grades(grades):
    return np.mean(grades)
    
print(calc_avg_grades(person["hw_scores"]))


        


# A class combines data and functions
class Person():
    def __init__(self, name, age, favorite_colors, hw_scores=[100, 100, 100]):
        self.name = name
        self.age = age
        self.favorite_colors = favorite_colors
        self.hw_scores = hw_scores
        
    def __str__(self):
        return self.name
    
    
    def calc_avg_grades(self):
        return np.mean(self.hw_scores)

    def set_name(self, name):
        self.name = name
        
    
andy_person = Person("andy", 43, ["aggie blue", "fighting white"], [95, 80, 99])

will_person = Person("will", 19, ["sky blue", "royal blue"], [96, 97, 98])
kyden_person = Person("kyden", 23, ["sunset orange", "aggie blue"], [40, 30, 96])

print(andy_person, will_person, kyden_person)


print(andy_person.calc_avg_grades())
# print(ryan.calc_avg_grades())
# print(ryan.name)

# ryan.set_name("ryan sofoul")
# print(ryan.name)

        