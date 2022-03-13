import logging
import os.path
import sys

def generate_log():
    LogFileNAME='Test.log'
    #Log_format = "%(asctime)s - %(name)-12 -%(levelname) -8s - %(message)s"
    Log_format = "%(asctime)s -%(name)s-[%(levelname)s] -%(message)s"
    Log_Name='Report_logger'
    log_path = '/result/Test.log'
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)

    log=logging.getLogger(Log_Name)
    log_formatter=logging.Formatter(Log_format)
    curr_File_path=os.path.abspath(__file__)
    #cur_dir=os.path.dirname(curr_File_path)
    #par_dir=os.path.dirname(cur_dir)
    ##path=os.path.dirname(cur_dir)
    #path=os.path.join(par_dir,log_path)
    path='../result/Test.log'
    #path=os.path.join(path,LogFileNAME)
    logg=logging.FileHandler(path,mode='w')
    logg.setFormatter(log_formatter)
    logg.setLevel(logging.DEBUG)
    log.addHandler(logg)
    log.setLevel(logging.DEBUG)
    return log




