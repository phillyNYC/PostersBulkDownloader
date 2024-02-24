# Movie Poster Downloader

This Python script automatically fetches and downloads movie posters based on a list of movie names. It uses The Movie Database (TMDb) API to retrieve movie information and poster URLs.

## Configuration

Before running the script, you'll need to make a few edits to include your specific details:

1. **API Key**: Obtain an API key from TMDb and replace the placeholder value in the script with your actual API key. Find the line containing **api_key = "YOUR_API_KEY_GOES_HERE"** and replace **"YOUR_API_KEY_GOES_HERE"** with your TMDb API key.
2. **Text File Location**: Replace the placeholder value in the script with the path to your text file containing the list of movies. Find the line containing **movies_filepath = "C:\\path\\to\\your\\movies_list.txt"** and replace **"C:\\path\\to\\your\\movies_list.txt"** with the actual location of your txt file.

MOVIE NAMES HAVE TO BE IN "Movie Name Release Year" FORMAT. NO DOTS, NO DASHES!!! Example:
*The Great Garsby 2013
I Care a Lot 2020
Iron Man 2008*
4. **Export Folder Location**: Replace the placeholder value in the script with the folder path where you want the posters to be downloaded. Find the line containing **posters_folder_path = "C:\\path\\to\\your\\export_folder"** and replace **"C:\\path\\to\\your\\export_folder"** with the actual location of your folder.
5. Specify the path to the folder where you want the posters to be downloaded.

### Obtaining a TMDb API Key

To get an API key from TMDb, follow these steps:

1. Sign up for an account or log in on [The Movie Database (TMDb)](https://www.themoviedb.org/).
2. Navigate to your account settings and select the API section from the sidebar.
3. Follow the instructions to request an API key. When asked, select "Developer" and provide the necessary information.

### Running the Script

Download the latest version of the script from [here](https://github.com/phillyNYC/PostersBulkDownloader/releases/download/Script/PostersBulkDownloader.py). With Python installed on your system, open your command line interface and navigate to the directory containing the script. Run the script using the following command:

```bash
python PostersBulkDownloader.py
```

Make sure you have the requests library installed. If not, you can install it using pip:
```bash
pip install requests
```
