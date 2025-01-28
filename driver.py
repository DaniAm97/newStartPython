from processor import persist, ingest
import logging
import logging.config
from flask import Flask, request, send_from_directory
import os

app = Flask(__name__)
@app.route('/courses',methods=['GET'])
def get_courses():
    dbObject = persist.PersistData("postgres")
    courses = dbObject.read_from_pg('futurexschema.futurex_course_catalog')
    return f"The Courses are: "f'{courses}'

@app.route('/course', methods=['POST'])
def insert_course():
    input_json = request.get_json(force=True)
    print(f'json input ------> {input_json}')

    dbObject = persist.PersistData('postgres')
    dbObject.write_from_json_to_pg('futurexschema.futurex_course_catalog',
                                    input_json)
    return "created succssfully!"


class DriverProgram:
    logging.config.fileConfig("processor/resources/configs/logging.conf")

    def __init__(self, fileType):
        logging.debug(" I am with the constructor")
        self.file_type = fileType

    def my_function(self):
        logging.debug("inside my function ... Processing " + self.file_type + " file")
        reader = ingest.FileReader(self.file_type)
        writer = persist.PersistData("postgres")
        read_json = reader.read_file()
        print("reading the json: "f'{read_json}')
        writer.store_date(read_json)



def print_hi(name):
    logging.debug(f' hi {name}')


if __name__ == '__main__':
    app.run(port=1234, debug=True)
