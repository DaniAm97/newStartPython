import logging
import logging.config
class FileReader:
    logging.config.fileConfig("resources/configs/logging.conf")
    logger = logging.getLogger("Ingest")

    def __init__(self, fileType):
        self.logger.info(" I am with the fileReader constructor")
        self.file_type = fileType
    def read_file(self):
        self.logger.debug("reading file... " + self.file_type + "file")