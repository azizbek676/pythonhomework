import requests
import random
API_KEY = 'YOUR_API_KEY'
BASE_URL = "https://api.themoviedb.org/3"
def get_genres():
    url = f"{BASE_URL}/genre/movie/list?api_key={API_KEY}&language=en-US"
    response = requests.get(url)
    data = response.json()
    genres = data['genres']
    return {genre['name']: genre['id'] for genre in genres}
def get_random_movie(genre_id):
    url = f"{BASE_URL}/discover/movie?api_key={API_KEY}&with_genres={genre_id}&language=en-US"
    response = requests.get(url)
    data = response.json()
    if data['results']:
        movie = random.choice(data['results'])
        return movie['title'], movie['overview'], movie['release_date']
    else:
        return None

def main():
    genres = get_genres()
    print("Available movie genres:")
    for genre in genres:
        print(f"- {genre}")
    
    user_genre = input("Please enter a genre from the above list: ").strip()
    if user_genre in genres:
        genre_id = genres[user_genre]
        movie = get_random_movie(genre_id)
        
        if movie:
            title, overview, release_date = movie
            print(f"\nMovie Recommendation: {title}")
            print(f"Release Date: {release_date}")
            print(f"Overview: {overview}")
        else:
            print("No movies found for this genre.")
    else:
        print("Invalid genre. Please try again.")

if __name__ == "__main__":