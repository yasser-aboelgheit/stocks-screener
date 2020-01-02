# stocks-screener

1- Since Alpha Vantage doesnt have a list of the 500 companies. Scraping https://www.slickcharts.com/sp500 is used to get this list /n \n
2- we save each company as a record in the db
3-Each time a user enters home page, the system checks its db. If it is empty or records isnt at the current day, a new scraping is done to get the updated list
4- By clicking on any company a graph appears representing the stock data for the current day
