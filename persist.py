import logging
import logging.config
import configparser
class PersistData:
    logging.config.fileConfig("resources/configs/logging.conf")
    logger = logging.getLogger("Persist")
    config = configparser.ConfigParser()
    config.read("resources/fileprocessor.ini")

    def __init__(self,dbType):
        self.logger.debug("with persist data constractor")
        self.db_type = dbType
    def store_date(self):
        try:
            target_table = self.config.get("DATABASE_CONFIGS","PG_TABLE")
            self.logger.debug("target table name is : "+target_table)
            self.logger.debug("storing data to "+self.db_type + " file")
            var1 = 100/0
        except Exception as exp:
            self.logger.error("An error has found : "+str(exp))