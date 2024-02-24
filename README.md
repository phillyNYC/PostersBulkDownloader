# Movie Poster Downloader

This Python script automatically fetches and downloads movie posters based on a list of movie names. It uses The Movie Database (TMDb) API to retrieve movie information and poster URLs.

## GUI Usage on Windows

To run the GUI application, follow these steps:

1. **Download the Executable**: Download the latest release from the [Releases](https://github.com/phillyNYC/PostersBulkDownloader/releases/latest) section.
2. **Launch the Application**: Double-click on the downloaded `.exe` file to launch the GUI.
3. **Configure Settings**:
   - Enter your TMDb API Key in the "TMDb API Key" field.
   - Use the "Browse..." buttons to select the location of your movie list file and to choose the export location for the downloaded posters.
4. **Start Download**: Click on the "Start Download" button to begin downloading posters. The application will display the progress and notify you once the download is complete.

## Note on Antivirus False Positives

Some antivirus programs may flag the downloaded executable as a potential threat (false positive). This is a common issue with executables created using tools like PyInstaller, which is used to package this Python application.

If your antivirus software alerts you about the executable, you can safely allow the application to run. I ensure that the executable is clean and free of any malware. Anyways, if you don't trust, you can do it manually by running the script. A guide is provided below.


## Configuration

Before running the script, you'll need to make a few edits to include your specific details:

1. **API Key**: Obtain an API key from TMDb and replace the placeholder value in the script with your actual API key. Find the line containing **api_key = "YOUR_API_KEY_GOES_HERE"** and replace **"YOUR_API_KEY_GOES_HERE"** with your TMDb API key.
2. **Text File Location**: Replace the placeholder value in the script with the path to your text file containing the list of movies. Find the line containing **movies_filepath = "C:\\path\\to\\your\\movies_list.txt"** and replace **"C:\\path\\to\\your\\movies_list.txt"** with the actual location of your txt file.

**MOVIE NAMES HAVE TO BE IN "Movie Name Release Year" FORMAT. NO DOTS, NO DASHES!!! Example:**

   - *The Great Gatsby 2013*
   - *I Care a Lot 2020*
   - *Iron Man 2008*

3. **Export Folder Location**: Replace the placeholder value in the script with the folder path where you want the posters to be downloaded. Find the line containing **posters_folder_path = "C:\\path\\to\\your\\export_folder"** and replace **"C:\\path\\to\\your\\export_folder"** with the actual location of your folder.

### Obtaining a TMDb API Key

To get an API key from TMDb, follow these steps:

1. Sign up for an account or log in on [The Movie Database (TMDb)](https://www.themoviedb.org/).
2. Navigate to your account settings and select the API section from the sidebar.
3. Follow the instructions to request an API key. When asked, select "Developer" and provide the necessary information.

### Running the Script

Download the latest version of the script from [here](https://github.com/phillyNYC/PostersBulkDownloader/releases/latest). With Python installed on your system, open your command line interface and navigate to the directory containing the script. Run the script using the following command:

```bash
python PostersBulkDownloader.py
```

Make sure you have the requests library installed. If not, you can install it using pip:
```bash
pip install requests
```

The script will create a log file named **missing_posters.log** in the posters directory with the movie names it couldn't identify, if there are any.
