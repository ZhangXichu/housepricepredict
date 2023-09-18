import mysql.connector
import configparser


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
