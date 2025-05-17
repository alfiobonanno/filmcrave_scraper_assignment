from bs4 import BeautifulSoup
import pandas as pd
import requests

base_url = "https://www.filmcrave.com"
current_url = base_url + "/list_top_movie.php"
all_films = []

while current_url:
    response = requests.get(current_url)
    html = response.text
    soup = BeautifulSoup(html,"html.parser")
    film_boxes = soup.find_all("div",class_="detail-box")
    for box in film_boxes:
        rank = box.select_one("h2.large > span.orange-bold-large").get_text(strip=True).replace(".","")
        title = box.select_one("h2.large > a.blue-bold").get_text()
        try:
            year_place = box.find("span", class_="grey-bold")
            year = year_place.next_sibling
        except AttributeError as e:
            year = None
        try:
            overall_rating = box.find("span", string= "Overall Rating: ").find_next("span").get_text()
            overall_rating = overall_rating.split(" ")[0]
        except AttributeError as e:
            overall_rating = None
        try:
            language = box.find("span", string="Language: ").next_sibling.strip()
        except AttributeError as e:
            language = None
        genre = box.find("span", string= "Genre: ").next_sibling.strip()
        try:
            mpaa_rating = box.find("span", string = "MPAA Rating: ").next_sibling.strip()
        except AttributeError as e:
            mpaa_rating = None
        try:    
            director = box.find("span", string = "Director: ").next_sibling.strip()
        except AttributeError as e:
            director = None
        try:
            actors = box.find("span", string= "Actors: " ).next_sibling.strip()
        except AttributeError as e:
            actors = None
        try:
            plot = box.find("span", string="Plot: ")
            plot_lines = []
            for sibling in plot.next_siblings:
                if sibling.name == 'br':
                    continue
                if isinstance(sibling, str):
                    line = sibling.strip()
                    if line:
                        plot_lines.append(line)
            description = " ".join(plot_lines)
        except AttributeError as e:
            description = None

        all_films.append({
            'rank': rank,
            'film_title' : title,
            'film_year': year,
            'overall_rating': overall_rating,
            'language': language,
            'genre': genre,
            'mpaa_rating': mpaa_rating,
            'director': director,
            'actors':actors,
            'plot_summary': description,
        })
    navbar = soup.find("nav", attrs={"aria-label": "Page results navigation"})
    next_link = navbar.find("a", string="Next") if navbar else None
    if next_link:
        href = next_link['href']
        current_url = base_url + href
        print(f"Navigating to {current_url}")
    else:
        break

df = pd.DataFrame(all_films)
df.to_csv('films.csv',index= False)
print(df.head())