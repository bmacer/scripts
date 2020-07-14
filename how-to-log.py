import logging
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("--debug", "-d",
                                       help="Display debug logs.",
                                       action="store_true")
    return parser.parse_args()

def init_logger(log_level=logging.INFO, log_filename="log.log"):
    log = logging.getLogger(__file__)
    log.setLevel(log_level)
    console_handler = logging.StreamHandler()
    file_handler = logging.FileHandler(log_filename)
    formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s')
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)
    log.addHandler(console_handler)
    log.addHandler(file_handler)
    return log

if __name__ == "__main__":
    args = parse_arguments()
    if args.debug:
        log = init_logger(logging.DEBUG)
    else:
        log = init_logger()
    log.warning("warn!")
    log.debug("debug!")