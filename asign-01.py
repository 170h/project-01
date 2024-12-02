import requests

movie_ids = [
    238, 680, 550, 185, 641, 515042, 152532, 120467, 872585, 906126, 840430
]

url = "https://nomad-movies.nomadcoders.workers.dev/movies/"

for movie_id in movie_ids:
  response = requests.get(f"{url}{movie_id}")
  movie = response.json()
  
  title = movie["title"]
  vote = movie["vote_average"]
  overview = movie["overview"]
  
  print(f"\n{title} - {vote}")
  print(f"\n{overview}\n")
