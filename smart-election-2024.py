#!/usr/bin/env python3
"""
Electoral vote scraper for 270towin.com
Retrieves current electoral vote predictions for the 2024 election.
Sets smart lights to reflect the winner.
"""

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from typing import Tuple
import argparse
import logging
import sengled
import sys
import time

load_dotenv()

parser = argparse.ArgumentParser(description='Sets your smart lights to the color of the party of the winner of the 2024 presidential election')
parser.add_argument('--test-dem', action='store_true', help='Test Democrat win scenario')
parser.add_argument('--test-rep', action='store_true', help='Test Republican win scenario')
args = parser.parse_args()

api = sengled.api_from_env()

devices = api.get_device_details()

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def get_electoral_votes() -> Tuple[int, int]:
    """
    Scrapes 270towin.com for current electoral vote predictions.

    Returns:
        Tuple[int, int]: A tuple containing (republican_votes, democrat_votes)
    """
    url = "https://www.270towin.com/"
    try:
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-gpu')
        driver = webdriver.Chrome(options=options)
        driver.get(url)

        wait = WebDriverWait(driver, 10)
        dem_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "tr.party-row:nth-child(3) > td:nth-child(2)")))
        rep_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "tr.party-row:nth-child(4) > td:nth-child(2)")))

        democrat_votes = int(dem_element.text.strip())
        republican_votes = int(rep_element.text.strip())

        driver.quit()

        logger.info(f"Retrieved electoral votes - Republican: {republican_votes}, Democrat: {democrat_votes}")
        return republican_votes, democrat_votes

    except Exception as e:
        logger.error(f"Error fetching or parsing data: {e}")
        raise

def set_lights_red():
    api.set_on(devices)
    api.set_color(devices,[255,0,0])
    api.set_brightness(devices,100)

def set_lights_blue():
    api.set_on(devices)
    api.set_color(devices,[0,0,255])
    api.set_brightness(devices,100)


if __name__ == "__main__":
    if args.test_dem and args.test_rep:
        logger.error("Cannot test both scenarios simultaneously. Choose either --test-dem or --test-rep.")
        sys.exit(1)

    while True:
        try:
            if args.test_dem:
                republican_votes, democrat_votes = 268, 270
            elif args.test_rep:
                republican_votes, democrat_votes = 270, 268
            else:
                republican_votes, democrat_votes = get_electoral_votes()

            logger.info(f"\nCurrent Electoral Vote Prediction:")
            logger.info(f"Republican: {republican_votes}")
            logger.info(f"Democrat: {democrat_votes}")
        except Exception as e:
            logger.error("Failed to retrieve electoral votes")
            raise
        if democrat_votes >= 270:
            set_lights_blue()
            break
        elif republican_votes >= 270:
            set_lights_red()
            break
        if not (args.test_dem or args.test_rep):
            time.sleep(30)  # wait 30 seconds
        else:
            break  # Exit after one iteration for test scenarios


