#!/usr/bin/env python3
# coding: utf-8

"""
Web Image Downloader Script

This script is designed to demonstrate the fundamental concepts of web scraping and file handling in Python.
It fetches all the images from a specified webpage URL and downloads them into a local directory. This script
covers several key programming concepts and Python libraries:

1. Command Line Arguments: Utilises sys.argv to accept URL input from the command line.
2. HTTP requests: Uses the 'requests' library to make HTTP requests to download webpages and images.
3. HTML parsing: Employs 'BeautifulSoup' from bs4 for parsing HTML content and extracting image URLs.
4. File handling: Demonstrates creating directories and writing binary data to files.
5. Exception handling: Implements try-except blocks to handle potential HTTP errors or request exceptions.
6. URL handling: Uses urllib.parse.urljoin to resolve relative URLs.

Usage:
    python script.py <URL>
"""

import os
import sys
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

def download_images(url, folder_name):
    """
    Downloads all images from a given URL into a specified folder.

    * Use the requests.get() function to send a GET request to the URL and store the response
    * Use response.raise_for_status() to raise an exception for HTTP errors
    * Create a BeautifulSoup object named 'soup' using response.text and 'html.parser' as parameters
    * Find all image tags using soup.find_all('img') and store them in a variable named 'images'
    * Check if the 'images' list is empty and print "No images found on the page." if it is
    * Create the target folder using os.makedirs(folder_name, exist_ok=True)
    * Loop through each image in 'images', extract the 'src' attribute, resolve relative URLs,
      and download the image using the download_image() function
    """
    pass  # Remove this and add your code

def download_image(img_url, folder_name):
    """
    Downloads a single image from a given URL and saves it to the specified folder.

    * Use the requests.get() function to send a GET request to the image URL and store the response
    * Use response.raise_for_status() to raise an exception for HTTP errors
    * Extract the image name from the URL using os.path.basename(img_url)
    * Open a file in binary write mode in the specified folder and write the response content to it
    """
    pass  # Remove this and add your code

if __name__ == "__main__":
    """
    Main function to run the image downloader script.

    * Check if the correct number of command-line arguments are provided and print the usage
      instructions if not
    * Extract the URL from sys.argv and set a folder name for downloaded images
    * Call the download_images() function with the URL and folder name as arguments
    """
    pass  # Remove this and add your code
