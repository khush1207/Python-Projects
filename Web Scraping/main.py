import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url=URL)
content = response.text

soup = BeautifulSoup(content, "html.parser")

movie_text = [text.getText() for text in soup.find_all(name="h3", class_="title")]
movie_text.reverse()
print(movie_text)

#Create a blank movies.txt file to store the extracted data
with open("movies.txt", mode="w", encoding="UTF-8") as file:
    for movie in movie_text:
        file.write(f"{movie}\n")
