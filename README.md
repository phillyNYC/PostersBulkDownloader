# Movie Poster Downloader

This Python script automatically fetches and downloads movie posters based on a list of movie names. It uses The Movie Database (TMDb) API to retrieve movie information and poster URLs.

## Configuration

Before running the script, you'll need to make a few edits to include your specific details:

1. **API Key**: Obtain an API key from TMDb and insert it into the script.
2. **Text File Location**: Specify the path to your text file containing the list of movies.
3. **Export Folder Location**: Specify the path to the folder where you want the posters to be downloaded.

### Obtaining a TMDb API Key

To get an API key from TMDb, follow these steps:

1. Sign up for an account or log in on [The Movie Database (TMDb)](https://www.themoviedb.org/).
2. Navigate to your account settings and select the API section from the sidebar.
3. Follow the instructions to request an API key. When asked, select "Developer" and provide the necessary information.

### Running the Script

With Python installed on your system, open your command line interface and navigate to the directory containing the script. Run the script using the following command:

```bash
python read_movies.py
