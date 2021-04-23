import os
import config
import utils


def working_dir_not_exists():
    os.remove(config.WORKING_DIR)

    exists = not utils.check_working_dir()
    assert exists


def working_dir_exists():
    os.mkdir(config.WORKING_DIR)

    exists = utils.check_working_dir()
    assert exists
