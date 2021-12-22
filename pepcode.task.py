from bs4 import BeautifulSoup
from requests import get

data = get("https://en.wikipedia.org/wiki/N")
soup = BeautifulSoup(data.content, "html.parser")
# soup.prettify()
print("History: \n", (soup.find_all("p"))[2], "\n")
print("Use in writing systems: \n", (soup.find_all("p"))[3], "\n")
print("Other uses: \n", (soup.find_all("p"))[4])
