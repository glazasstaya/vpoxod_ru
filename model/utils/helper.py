import os
from selene import browser, command
from datetime import datetime, timedelta
from definition import ROOT_DIR

def now_delta(delta):
    return (datetime.now() + timedelta(days=delta)).strftime("%d.%m.%Y")


def scroll_to_element(element_name):
    browser.element(element_name).perform(command.js.scroll_into_view)

def dir_checout(dir_list):
    download_dir = ROOT_DIR
    for dir in dir_list:
        download_dir = os.path.abspath(os.path.join(download_dir, dir))
    os.chdir(download_dir)

