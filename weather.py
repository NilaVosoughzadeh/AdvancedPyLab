import requests
import bs4
from colorama import Fore

city = input(f"{Fore.GREEN} Enter city name : ").lower()

response = requests.get(f"https://www.timeanddate.com/weather/iran/{city}/ext")

soup = bs4.BeautifulSoup(response.text , 'html.parser')
weather = soup.find_all("div",attrs={"class":"alert__content"})

# print(weather)

for i in weather :
    text = i.text
    temp = text.split(".")[0]
    status = text.split(".")[1]
    station = text.split(".")[2]
    print(Fore.CYAN + temp.strip())
    print(Fore.MAGENTA + status.strip())
    print(Fore.BLUE + station.strip())
    print(Fore.RESET)