
# old main:
# - add meals to meal list
# 	- set name, time type (breakfast, lunch, etc), cusisine type, frequency preference
# - randomly select meals based on:
# 	- open time slots
# 	- frequency
#  	- available order-out options
# 	- leftovers
# - display choices


from meal_constants import *
import meal_utils as utils

if __name__ == '__main__':
    options = ['    a / add    -- add meal to database', '    v / view   -- view meals in database',
               '    d / delete -- delete meal in database (by ID)', '    p / pick   -- pick meals for the week',
               '    l / list   -- generate shopping list of ingredients for last picked meals',
               '    q / quit   -- exit MealPicker']

    print('Welcome to MealPicker!')
    print('Choose an option:')
    for option in options:
        print(option)

    endcode = False
    last_picked_meals = None
    while not endcode:
        entry = input('enter option: ')
        if entry.lower() == 'a' or entry.lower() == 'add':
            utils.add_meals_to_db()
        elif entry.lower() == 'v' or entry.lower() == 'view':
            utils.view_meals_in_db()
        elif entry.lower() == 'd' or entry.lower() == 'delete':
            utils.delete_meals_in_db()
        elif entry.lower() == 'p' or entry.lower() == 'pick':
            generate_list_choice = input('Generate shopping list as well? (y/n): ')
            last_picked_meals = utils.pick_meals_for_week()
            if generate_list_choice.lower() == 'y':
                utils.generate_shopping_list(last_picked_meals)
        elif entry.lower() == 'l' or entry.lower() == 'list':
            if last_picked_meals:
                utils.generate_shopping_list(last_picked_meals)
            else:
                print("No meals have been picked.  Please run 'pick' option before 'list'.")
        elif entry.lower() == 'q' or entry.lower() == 'quit':
            endcode = True
        else:
            print('Invalid entry; options are:')
            for option in options:
                print(option)

