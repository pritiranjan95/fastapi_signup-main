import logging
logging_format= "%(asctime)s - %(message)s"

logging.basicConfig(filename="signup.log", filemode="a", level=logging.DEBUG, format= logging_format)
logg= logging.getLogger("Bapi")


if __name__=="__main__":
    logg.info("Logger started working")