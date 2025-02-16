import logging
import logging.config
import json

class FileReader:
    logging.config.fileConfig("processor/resources/configs/logging.conf")
    logger = logging.getLogger("Ingest")

    def __init__(self, fileType):
        self.logger.info(" I am with the fileReader constructor")
        self.file_type = fileType
    def read_file(self):
        self.logger.debug("reading file... " + self.file_type + "file")
        with open ('course.json') as f:
            new_course = json.load(f)
        print("new_course is "+str(new_course))
        return new_course


