#!/usr/bin/env python3
# coding: utf-8

"""
Web Image Downloader Using Regex

This script downloads images from a specified webpage using regular expressions (regex) for parsing HTML content.
The script demonstrates an alternative approach to BeautifulSoup for extracting image URLs from a webpage. It uses
regex to find 'img' tags and their 'src' attributes, then downloads each image found into a specified directory.

Key Concepts Covered:
- Regex for simple HTML parsing.
- Handling HTTP requests and responses using the 'requests' library.
- Working with Python's file and OS operations for saving images.
- Basic command-line argument parsing.

Usage:
    python script.py <URL>
"""

import os
import re
import sys
from urllib.parse import urljoin

import requests

def download_images(url, folder_name):
    """Downloads all images from a given webpage URL.

    * Use the requests.get() function to send a GET request to the URL and store the response
    * Use response.raise_for_status() to raise an exception for HTTP errors
    * Use the re.findall() function to find all image URLs in the response text using a regex pattern
      and store them in a variable named 'image_urls'
    * Check if the 'image_urls' set is empty and print "No images found on the page." if it is
    * Create the target folder using os.makedirs(folder_name, exist_ok=True)
    * Loop through each URL in 'image_urls', resolve relative URLs, and download the image using the
      download_image() function
    """
    pass  # Remove this and add your code

def download_image(img_url, folder_name):
    """Downloads a single image and saves it to a specified folder.

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
