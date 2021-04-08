# old meal_module:
# - contains meal info
# 	- name
# 	- time type
# 	- cuisine type
# 	- frequency
# 	- main protein
# 	- produces leftovers

class meal_module:
    def __init__(self, name, timeperiod, cuisine, frequency, protein, calories, leftovers):
        self.name = name
        self.timeperiod = timeperiod
        self.cuisine = cuisine
        self.frequency = frequency
        self.protein = protein
        self.calories = calories
        self.leftovers = leftovers

    def get_name(self):
        return self.name

    def get_timeperiod(self):
        return self.timeperiod

    def get_cuisine(self):
        return self.cuisine

    def get_frequency(self):
        return self.frequency

    def get_protein(self):
        return self.protein

    def get_calories(self):
        return self.calories

    def get_leftovers(self):
        return self.leftovers

