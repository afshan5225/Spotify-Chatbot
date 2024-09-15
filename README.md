# Spotify Chat Bot

This project is a chatbot application that provides information about music tracks from a dataset of Spotify music data. The bot can respond to queries about genres, artists, and songs, as well as suggest similar songs.

## Problem Statement

The goal of this project is to create a chatbot that can interact with users to provide music-related information based on a dataset of Spotify tracks. The bot can:
- Retrieve songs by genre or artist.
- Provide details about a specific song.
- Suggest similar songs based on genre.

## Libraries Used

- `pandas` - For data manipulation and analysis.
- `numpy` - For numerical operations.
- `nltk` - For natural language processing and chatbot functionality.

## Execution Methodology

1. **Data Preparation**:
   - Load the dataset from a CSV file.
   - Clean and preprocess the data by removing unnecessary columns and handling missing values.
   - Transform and rename columns for consistency.

2. **Chatbot Initialization**:
   - Define patterns and responses for the chatbot using `nltk`.
   - Implement functions to handle different types of queries related to music data (e.g., by genre, artist, song name).

3. **User Interaction**:
   - The chatbot runs in a loop, accepting user input and responding based on predefined patterns.
   - The conversation continues until the user decides to quit.

4. **Saving Data**:
   - The cleaned dataset is saved to a CSV file for future reference.

