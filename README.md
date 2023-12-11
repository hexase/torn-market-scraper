# torn-market-scraper

This is a script for a game called [Torn](torn.com). There is a player market that is entirely based on buying things and selling them to other players for slightly higher prices. 

This script uses the [Torn API](https://www.torn.com/api.html) to look for a subset of items in which it is consistently profitable to do this with, by using the API to fetch the average price, and outputting links to market listings that are less than or within a certain variance of the average.
