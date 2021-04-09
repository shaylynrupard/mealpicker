# meal types
BREAKFAST = 'breakfast'
LUNCH     = 'lunch'
DINNER    = 'dinner'
MEAL_TYPES = [BREAKFAST, LUNCH, DINNER]

# number of meals per type
NUM_BREAKFAST = 7
NUM_LUNCH     = 7
NUM_DINNER    = 7

# maximum number of times a meal can repeat
BREAKFAST_REPEAT = 3
LUNCH_REPEAT     = 3
DINNER_REPEAT    = 2

# max caloric value of daily meals (TODO: add this funcitonality)
CALORIE_MAX   = 1870

# file constants
SEPARATOR               = ', '
DATABASE_FILE_NAME      = 'testdatabase.db'
SHOPPING_LIST_FILE_NAME = 'shopping_list_'
MEAL_LIST_FILE_NAME     = 'meal_list_'
FILE_EXT                = '.txt'

# sql command to create meal table if it doesn't exist
CREATE_TABLE_SQL = """CREATE TABLE IF NOT EXISTS meals (
                        id integer PRIMARY KEY AUTOINCREMENT,
                        name text NOT NULL,
                        meal_type text NOT NULL,
                        ingredients text NOT NULL   
                      );"""