BREAKFAST = 'breakfast'
LUNCH     = 'lunch'
DINNER    = 'dinner'

MEAL_TYPES = [BREAKFAST, LUNCH, DINNER]

NUM_BREAKFAST = 7
NUM_LUNCH     = 7
NUM_DINNER    = 7

BREAKFAST_REPEAT = 3
LUNCH_REPEAT     = 3
DINNER_REPEAT    = 2

CALORIE_MAX   = 1870

SEPARATOR = ', '
DATABASE_FILE_NAME = 'testdatabase.db'

CREATE_TABLE_SQL = """CREATE TABLE IF NOT EXISTS meals (
                        id integer PRIMARY KEY AUTOINCREMENT,
                        name text NOT NULL,
                        meal_type text NOT NULL,
                        ingredients text NOT NULL   
                      );"""