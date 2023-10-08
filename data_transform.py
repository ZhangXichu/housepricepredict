import mysql.connector
import configparser

sql_create = ''' CREATE TABLE IF NOT EXISTS apartment(
id VARCHAR(30) NOT NULL PRIMARY KEY, 
overall_price DECIMAL(20, 2), 
usable_area DECIMAL(10, 2), 
loggia_area DECIMAL(10, 2), 
basement_area DECIMAL(10, 2), 
dist_pub DECIMAL(10, 2), 
dist_bus DECIMAL(10, 2), 
dist_atm DECIMAL(10, 2), 
dist_train DECIMAL(10, 2), 
dist_tram DECIMAL(10, 2), 
dist_shop DECIMAL(10, 2), 
dist_rest DECIMAL(10, 2), 
longitude DECIMAL(10, 2),
latitude DECIMAL(10, 2),
has_loggia INT,
has_basement INT, 
near_pub INT, 
near_atm INT, 
near_bus INT, 
near_train INT, 
near_tram INT, 
near_shop INT, 
near_rest INT, 
apartment_type VARCHAR(255), 
building_state VARCHAR(255), 
ownership VARCHAR(255),
images VARCHAR(5000)); '''

sql_insert = ''' INSERT IGNORE INTO
apartment(id, overall_price, usable_area, loggia_area, basement_area, dist_pub, dist_bus, dist_atm, dist_train,
          dist_tram, dist_shop, dist_rest, longitude, latitude, has_loggia,
has_basement, near_pub, near_atm, near_bus, near_train, near_tram, near_shop, near_rest, apartment_type, building_state, ownership, images) 
VALUES
(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''


def connect_to_db():
    """
    connects to the database
    :return: connector object
    """
    config = configparser.ConfigParser()
    config.read('sqlconfig.config')

    mydb = mysql.connector.connect(host=config['database']['host'], user=config['database']['user'],
                                   password=config['database']['pwd'], db=config['database']['database'])

    return mydb
