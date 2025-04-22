import logging
import os

#Additional log file creation and formatting


class LogGen:
    @staticmethod
    def loggen():
     
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        logs_dir = os.path.join(project_root, "Logs")
        if not os.path.exists(logs_dir):
            os.makedirs(logs_dir)

        log_file_path = os.path.join(logs_dir, "automation.log")
        

        formatter = logging.Formatter(
            '%(asctime)s - %(levelname)s - %(name)s - %(message)s',
            datefmt='%m/%d/%Y %I:%M:%S %p'
        )

        file_handler = logging.FileHandler(log_file_path)
        file_handler.setFormatter(formatter)
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        

        if logger.handlers:
            logger.handlers.clear()
            
        logger.addHandler(file_handler)
        return logger