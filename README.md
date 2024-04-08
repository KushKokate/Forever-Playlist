<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
</head>
<body>
    <h1>Billboard Hot 100 Playlist Creator</h1>
    <p>The Billboard Hot 100 Playlist Creator is a Python script that automates the process of creating Spotify playlists based on the Billboard Hot 100 chart for a specific date.</p>

  <h2>Overview</h2>
    <p>The script utilizes web scraping techniques to extract the top songs from the Billboard website for the user-provided date. It then interfaces with the Spotify API using the Spotipy library to search for these songs and create a new playlist on the user's Spotify account.</p>

  <h2>Features</h2>
    <ul>
        <li><strong>Dynamic Playlist Generation:</strong> Users can specify a date in the format YYYY-MM-DD to generate a playlist reflecting the Billboard Hot 100 songs for that date.</li>
        <li><strong>Spotify Integration:</strong> Seamless interaction with the Spotify API allows for the creation of playlists directly on the user's Spotify account.</li>
        <li><strong>Customization Options:</strong> Users can choose playlist privacy settings (public or private) and decide whether the playlist should be collaborative.</li>
        <li><strong>Error Handling:</strong> The script includes robust error handling to manage scenarios where songs are not found on Spotify or when the user's Spotify credentials are incorrect.</li>
    </ul>

  <h2>Usage</h2>
    <ol>
        <li><strong>Installation:</strong> Ensure the required Python packages, including Spotipy, Requests, and Beautiful Soup, are installed.</li>
        <li><strong>Spotify API Credentials:</strong> Obtain client ID and client secret from the Spotify Developer Dashboard and update the placeholders in the script.</li>
        <li><strong>Running the Script:</strong> Execute the script and follow the prompts to input the desired date.</li>
        <li><strong>Playlist Creation:</strong> The script will create a new Spotify playlist with the Billboard Hot 100 songs for the specified date.</li>
    </ol>

  <h2>License</h2>
    <p>This project is licensed under the <a href="LICENSE">MIT License</a>. See the LICENSE file for details.</p>

  <h2>Author</h2>
    <p>Created by KUSH KOKATE. For inquiries and feedback, please contact kokatekush@gmail.com.</p>
</body>
</html>
