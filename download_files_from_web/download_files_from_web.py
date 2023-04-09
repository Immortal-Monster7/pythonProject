from urllib import request

tesla_url = 'https://query1.finance.yahoo.com/v7/finance/download/TSLA?period1=1648845017&period2=1680381017&interval=1d&events=history&includeAdjustedClose=true'

def download_stock_data(csv_url):  #we're using csv url because that is the file which we want to download
    response = request.urlopen(csv_url)  #first step to make a connection to the webpage/website
    csv = response.read()  #this step will store the read things in a variable called csv
    csv_str = str(csv)  #this will convert the csv url into string format
    lines = csv_str.split("\\n")  #this will split the data or content in lines
    dest_url = r'tesla.csv'  #we have named the file as tesla.csv on our computer
    fx = open(dest_url, 'w')  #we are opening the file and writing/making changes to it.
    for line in lines:
        fx.write(line + "\n")
    fx.close()

download_stock_data(tesla_url)
