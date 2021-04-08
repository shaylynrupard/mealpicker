import math
import os
import random
import sqlite3

from meal_constants import *

def connect_to_db():
    database_filepath = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', DATABASE_FILE_NAME))
    return sqlite3.connect(database_filepath)

def add_meals_to_db():
    name = input('meal name: ')
    meal_type = None

    valid_type = False
    while not valid_type:
        meal_type = input('meal type (breakfast, lunch, dinner): ').lower()
        if meal_type not in MEAL_TYPES:
            print('invalid meal type')
        else:
            valid_type = True

    ingredients = []
    more_ingredients = True
    while more_ingredients:
        ingredient = input("ingredients (type 'end' when finished): ")
        if ingredient.lower() == 'end':
            more_ingredients = False
        else:
            ingredients.append(ingredient)

    print("Adding meal '%s' of type '%s' with ingredients: " % (name, meal_type))
    for ingredient in ingredients:
        print('    - %s'% ingredient)

    try:
        conn = connect_to_db()
        cur = conn.cursor()

        cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='meals'")
        table_exists = cur.fetchall()
        if not table_exists:
            cur.execute(CREATE_TABLE_SQL)

        sql = ''' INSERT INTO meals(name, meal_type, ingredients) VALUES(?,?,?)'''
        meal_entry = (name, meal_type, SEPARATOR.join(ingredients))
        cur.execute(sql, meal_entry)
        conn.commit()

        conn.close()
    except Exception as e:
        print('ERROR: %s' % e)

    print("Added meal '%s'!" % name)

def delete_meals_in_db():
    view_meals_in_db()

    delete_id = input("ID of meal to delete from database: ")
    try:
        conn = connect_to_db()
        cur = conn.cursor()

        query_sql = 'SELECT * FROM meals WHERE id=?'
        cur.execute(query_sql,(delete_id,))
        delete_row = cur.fetchall()
        if not delete_row:
            print("Meal with ID %s does not exist" % delete_id)
        else:
            #print("Deleting meal: %s" % delete_row[0])
            delete_sql = 'DELETE FROM meals WHERE id=?'
            cur.execute(delete_sql, (delete_id,))
            conn.commit()
            print("Meal deleted")

        conn.close()
    except Exception as e:
        print('ERROR: %s' % e)

def view_meals_in_db():
    print('Current meals in database: ')
    print('ID   NAME    MEAL_TYPE   INGREDIENTS')
    try:
        conn = connect_to_db()
        cur = conn.cursor()

        cur.execute("SELECT * FROM meals")
        rows = cur.fetchall()

        for row in rows:
            print(row)

        conn.close()
    except Exception as e:
        print('ERROR: %s' % e)

def pick_meals_for_week():
    print('Generating meals for the week...')
    picked_meals = []

    try:
        conn = connect_to_db()
        cur = conn.cursor()

        # get breakfast meals
        cur.execute("SELECT * FROM meals WHERE meal_type='breakfast'")
        rows = cur.fetchall()
        if len(rows) < NUM_BREAKFAST:
            print("ERROR: Not enough breakfast options (need %s; have %s).  Please add more to the database."
                  % (NUM_BREAKFAST, len(rows)))
            conn.close()
            return
        picked_meals = _choose_meals(rows, picked_meals, NUM_BREAKFAST, BREAKFAST_REPEAT)

        # get lunch meals
        cur.execute("SELECT * FROM meals WHERE meal_type='lunch'")
        rows = cur.fetchall()
        if len(rows) < math.ceil(NUM_LUNCH/LUNCH_REPEAT):
            print("ERROR: Not enough lunch options (need %s; have %s).  Please add more to the database."
                  % (math.ceil(NUM_LUNCH/LUNCH_REPEAT), len(rows)))
            conn.close()
            return
        picked_meals = _choose_meals(rows, picked_meals, NUM_LUNCH, LUNCH_REPEAT)

        # get dinner meals
        cur.execute("SELECT * FROM meals WHERE meal_type='dinner'")
        rows = cur.fetchall()
        if len(rows) < math.ceil(NUM_DINNER/DINNER_REPEAT):
            print("ERROR: Not enough dinner options (need %s; have %s).  Please add more to the database."
                  % (math.ceil(NUM_DINNER/DINNER_REPEAT), len(rows)))
            conn.close()
            return
        picked_meals = _choose_meals(rows, picked_meals, NUM_DINNER, DINNER_REPEAT)

        for meal in picked_meals:
            print(meal)

        conn.close()
    except Exception as e:
        print('ERROR: %s' % e)

    return picked_meals

def _choose_meals(rows, picked_meals, num_meals, num_repeat):
    meal_occurances = {}
    add_count = 0

    while add_count < num_meals:
        current_choice = random.choice(rows)
        if current_choice[0] in meal_occurances:
            if meal_occurances[current_choice[0]] != num_repeat:
                meal_occurances[current_choice[0]] = meal_occurances[current_choice[0]] + 1
                picked_meals.append(current_choice)
                add_count = add_count + 1
        else:
            meal_occurances[current_choice[0]] = 1
            picked_meals.append(current_choice)
            add_count = add_count + 1

    return picked_meals

def generate_shopping_list(last_picked_meals):
    pass