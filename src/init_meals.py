# old init_meals

import meal_module as mealmod
from meal_constants import *

def _check_min_freqency(meals):
    total_freq = 0
    for meal in meals:
        total_freq = total_freq + meal.get_frequency()

    return total_freq

def init_meals(time_type):
    """Funciton for setting meal options"""
    meals = []

    if time_type == BREAKFAST:
        meals.append(mealmod.meal_module('avocado toast', 'breakfast', 'american', 2, 'none', 470, False))
        meals.append(mealmod.meal_module('strawberry cream cheese bagel', 'breakfast', 'american', 2, 'none',
                                         400, False))
        meals.append(mealmod.meal_module('oatmeal with berries', 'breakfast', 'american', 1, 'none', -1, False))
        meals.append(mealmod.meal_module('omelette', 'breakfast', 'american', 2, 'egg, deli meat', 320, False))

        if _check_min_freqency(meals) < NUM_BREAKFAST:
            raise ValueError('ERROR: Not enough {type} meals for minimum requirement.  Please add more meals or ' + \
                             'increase meal frequencies'.format(type=BREAKFAST))

    elif time_type == LUNCH:
        if _check_min_freqency(meals) < NUM_LUNCH:
            raise ValueError('ERROR: Not enough {type} meals for minimum requirement.  Please add more meals or ' + \
                             'increase meal frequencies'.format(type=LUNCH))
    else:
        meals.append(mealmod.meal_module('frozen pizza', 'dinner', 'italian', 1, 'pepperoni, sausage', 1050, False))
        meals.append(mealmod.meal_module('frozen chicken and potatoes', 'dinner', 'american', 1, 'chicken', 650, False))
        meals.append(mealmod.meal_module('spaghetti and meatballs', 'dinner', 'italian', 1, 'ground beef', 750, False))
        meals.append(mealmod.meal_module('chicken, beans, and rice', 'dinner', 'mexican', 1, 'chicken', 765, False))
        meals.append(mealmod.meal_module('chili and sweet potato', 'dinner', 'american', 1, 'ground pork', 690, False))

        if _check_min_freqency(meals) < NUM_DINNER:
            raise ValueError('ERROR: Not enough {type} meals for minimum requirement.  Please add more meals or ' + \
                             'increase meal frequencies'.format(type=DINNER))

    return meals