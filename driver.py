import ingest
import persist
import logging
import logging.config
class DriverProgram:
    logging.config.fileConfig("resources/configs/logging.conf")

    def __init__(self, fileType):
        logging.debug(" I am with the constructor")
        self.file_type = fileType

    def my_function(self):
        logging.debug("inside my function ... Processing " + self.file_type + " file")
        reader = ingest.FileReader(self.file_type)
        writer = persist.PersistData("postgres")
        reader.read_file()
        writer.store_date()


def print_hi(name):
    logging.debug(f' hi {name}')


if __name__ == '__main__':
    print("hey")
    driver = DriverProgram("csv")
    driver.my_function()
