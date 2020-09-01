# Rooster Teeth Family Recent Uploads

## About

This web scraping program came to be when I started to realize how many clicks and minutes I had been spending on looking at these 4 YouTube channels upload pages to see if anything new had been added.

Basically the program will load the upload pages for all 4 channels in the channels dictionary and then scrape the entire page for videos on the initial load (it doesn't scroll down the page to load more as there is no need). After it grabs the videos it will then list the 10 most recent videos by each channel behind a selection menu for each channel (this is where the Enquiries library comes into play). When a video is selected the program will loop back to the main menu (where you can select which channels uploads to view) and will also open the url of the selected video in the users default web browser.

The program itself uses the Chrome browser to automate this process. If you do not know how to change the code to reflect a different web browser that your system uses then you will need to install Chrome.

## How to use

First you will need to clone and then pull the repo to your local machine.
Start up a new virtual enviroment (this project uses pipenv) so that the dependencies needed by Python can be installed via the Pipfile.
In your command line of choice just type in "python scraper.py"

### Dependencies

Selenium
Enquiries
Chrome
