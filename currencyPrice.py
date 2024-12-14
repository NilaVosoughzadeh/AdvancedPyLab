import requests
import bs4

print("dollar | eur | try | krw | cad | aud")
currency = input("Enter Currency : ")

url = f"https://www.tgju.org/profile/price_{currency}"

response = requests.get(url)

soup = bs4.BeautifulSoup(response.text , 'html.parser')
title = soup.find_all("td" , attrs={"class":"text-left"})

print("Current Price : " , title[0].text)
print("Current Price : " , title[1].text)
print("Current Price : " , title[2].text)