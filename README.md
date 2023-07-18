# Grade-Scraper

This web scraper uses Scrapy to collect grade distribution data for math courses at MU. The plotting file includes code that generates a scatter plot and linear regression model for the distributions of A, C, and F grades. 

## Guide

The following command 
```
scrapy crawl grades
```
can be given at the top level directory of the project. The user is then prompted to enter a mathematics course number. The average course grades and distribution of letter grades are then stored in a JSON file called data (this can be modified in the settings page). 
