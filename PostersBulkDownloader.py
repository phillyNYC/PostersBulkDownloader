import requests
import os

def read_movies(filepath):
    movies = []
    with open(filepath, 'r') as file:
        for line in file:
            # Assuming each line is "MovieName Year"
            parts = line.strip().split(" ")
            if len(parts) > 1:  # Basic validation
                movie_name = " ".join(parts[:-1])  # All but the last part
                release_year = parts[-1]
                movies.append((movie_name, release_year))
    return movies

def fetch_movie_data(movie_name, release_year, api_key):
    url = "https://api.themoviedb.org/3/search/movie"
    params = {
        'api_key': api_key,
        'query': movie_name,
        'year': release_year
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        if data['results']:
            # Just get the first result for simplicity
            first_result = data['results'][0]
            return {
                'title': first_result.get('title'),
                'release_date': first_result.get('release_date'),
                'poster_path': "https://image.tmdb.org/t/p/original" + first_result.get('poster_path') if first_result.get('poster_path') else None
            }
    return None

def download_poster(url, movie_name, folder_path):
    if url:
        response = requests.get(url)
        if response.status_code == 200:
            # Clean up file name
            safe_movie_name = "".join(x for x in movie_name if x.isalnum())
            filename = os.path.join(folder_path, f"{safe_movie_name}.jpg")
            with open(filename, 'wb') as file:
                file.write(response.content)
            print(f"Downloaded {filename}.")
        else:
            print(f"Failed to download poster for {movie_name}.")
    else:
        print(f"No poster URL for {movie_name}.")

def main():
    api_key = "YOUR_API_KEY_GOES_HERE"
    movies_filepath = "C:\\path\\to\\your\\movies_list.txt"
    posters_folder_path = "C:\\path\\to\\your\\export_folder"

    # Ensure the Posters directory exists
    if not os.path.exists(posters_folder_path):
        os.makedirs(posters_folder_path)

    movies_list = read_movies(movies_filepath)
    for movie_name, release_year in movies_list:
        movie_data = fetch_movie_data(movie_name, release_year, api_key)
        if movie_data:
            print(f"Movie: {movie_data['title']}, Release Date: {movie_data['release_date']}, Poster URL: {movie_data['poster_path']}")
            download_poster(movie_data['poster_path'], movie_data['title'], posters_folder_path)
        else:
            print(f"Movie: {movie_name} - Data not found.")

if __name__ == "__main__":
    main()
