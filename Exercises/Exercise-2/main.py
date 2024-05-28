import requests
import pandas
import io


url = 'https://www.ncei.noaa.gov/data/local-climatological-data/access/2021/'
from bs4 import BeautifulSoup

def web_scrape(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('table')
    rows = soup.find_all('tr')
    values = []
    target_date = '2024-01-19 10:21'
    for row in rows:
        cells = row.find_all('td')
        for cell in cells:
            if target_date in cell.text:
                return row
            
def read_csv(content):
    content = '<html>'+str(content)+'</html>'
    bs = BeautifulSoup(content, 'html.parser')
    csv_link = bs.find('a', href=True)  # Find the first <a> tag with an href attribute

    if csv_link:
        csv_path = csv_link['href']
        csv_url = url + csv_path  # Extract the URL or path to the CSV file
        try:
            csv_df = pandas.read_csv(csv_url)
            
            return csv_df

        except Exception as e:
            print(f"Error reading CSV: {e}")
    else:
        print("No link found")

    
        
    


def main():
    html_content = web_scrape(url=url)
    csvFile = read_csv(html_content)
    csv_file = csvFile.to_csv("./csvfile.csv")
    print(csvFile['HourlyDryBulbTemperature'].max())

    
    

if __name__ == "__main__":
    main()
