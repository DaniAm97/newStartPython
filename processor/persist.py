import logging
import logging.config
import configparser
import psycopg2
import json


class PersistData:
    logging.config.fileConfig("processor/resources/configs/logging.conf")
    logger = logging.getLogger("Persist")
    config = configparser.ConfigParser()
    config.read("processor/resources/fileprocessor.ini")

    def __init__(self, dbType):
        self.logger.debug("with persist data constractor")
        self.db_type = dbType

    def store_date(self, course_json):
        try:
            target_table = self.config.get("DATABASE_CONFIGS", "PG_TABLE")
            self.logger.debug("target table name is : " + target_table)
            self.logger.debug("storing data to " + self.db_type)
            #self.inesrt_into_pg(target_table)
            #self.read_from_pg(target_table)
            self.write_from_json_to_pg(target_table, course_json)
        except Exception as exp:
            self.logger.error("An error has found : " + str(exp))

    def read_from_pg(self, target_table):
        connection = psycopg2.connect(user='postgres',
                                      password='dani18881',
                                      host='localhost',
                                      database='postgres')
        cursor = connection.cursor()
        select_query = "SELECT * from "+f'{target_table}'
        cursor.execute(select_query)
        #print(cursor.fetchone()) gives only one record
        #cursor.fetchall() gives all records
        records = cursor.fetchall()  # prints every record in records
        for record in records:
            print(record)
        return  records

        cursor.close()
        connection.commit()

    def inesrt_into_pg(self, target_table):
        connection = psycopg2.connect(user='postgres',
                                      password='dani18881',
                                      host='localhost',
                                      database='postgres')
        cursor = connection.cursor()
        cursor.execute("select max(course_id) from "+f'{target_table}')
        max_course_id = cursor.fetchone()[0]

        insert_query = "INSERT INTO "+f'{target_table}' \
                       "(course_id, course_name, author_name, course_section, creation_date)" \
                       "VALUES (%s, %s, %s, %s, %s)"

        insert_tuple = (max_course_id+1, 'BI', 'Futurex', '{}', '2020-9-20')

        cursor.execute(insert_query, insert_tuple)
        cursor.close()
        connection.commit()

    def write_from_json_to_pg(self, target_table, course_json):
        self.logger.debug("write_from_json_to_pg method has been started")
        connection = psycopg2.connect(user='postgres',
                                      password='dani18881',
                                      host='localhost',
                                      database='postgres')
        cursor = connection.cursor()
        cursor.execute("select max(course_id) from "+f'{target_table}')
        max_course_id = cursor.fetchone()[0]


        insert_query = "INSERT INTO " + f'{target_table}' \
                                        "(course_id, course_name, author_name, course_section, creation_date)" \
                                        "VALUES (%s, %s, %s, %s, %s)"

        insert_tuple = (max_course_id+1, course_json['course_name'],
                                         course_json['authoer_name'],
                                         json.dumps(course_json['course_section']),
                                         course_json['creation_date'])

        cursor.execute(insert_query, insert_tuple)
        cursor.close()
        connection.commit()


