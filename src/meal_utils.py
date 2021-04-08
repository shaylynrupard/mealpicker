import sqlite3
import random
from meal_constants import *

def add_meals_to_db():
    name = input('meal name: ')

    valid_type = False
    while not valid_type:
        meal_type = input('meal type (breakfast, lunch, dinner): ')
        if meal_type.lower() not in MEAL_TYPES:
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
        conn = sqlite3.connect(DATABASE_FILE)
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
        conn = sqlite3.connect(DATABASE_FILE)
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
        conn = sqlite3.connect(DATABASE_FILE)
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
        conn = sqlite3.connect(DATABASE_FILE)
        cur = conn.cursor()

        cur.execute("SELECT * FROM meals")
        rows = cur.fetchall()

        print(random.choice(rows))

        conn.close()
    except Exception as e:
        print('ERROR: %s' % e)

    return picked_meals

def generate_shopping_list(last_picked_meals):
    pass