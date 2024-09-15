from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Load your dataset
data = pd.read_csv(r"C:\Users\USER\Desktop\chat\music.csv")

# Define chatbot logic

def get_music_by_artist(artist):
    result = data[data['artist'].str.lower() == artist.lower()]
    return result

def get_music_by_genre(genre):
    return data[data['genre'].str.lower() == genre.lower()]

def get_music_by_name(name):
    song_info = data[data['track'].str.lower() == name.lower()]
    return song_info

def get_similar_music(name):
    song_info = get_music_by_name(name)
    if not song_info.empty:
        similar_genre = song_info.iloc[0]['genre']
        similar_songs = get_music_by_genre(similar_genre)
        top_songs = similar_songs.sort_values(by='popularity', ascending=False).head(10)
        return top_songs
    return None

def respond_to_query(query):
    query = query.lower().strip()
    
    # Casual conversation responses
    if query in ['hello', 'hey', 'hi']:
        return "Hello! How can I assist you today?"
    elif query in ['how are you', 'how are you doing', 'how’s it going']:
        return "I'm just a bot, but I'm here and ready to help you!"
    elif query in ['i love you', 'love you']:
        return "I appreciate the sentiment! How can I assist you with your music today?"
    
    # Music-related queries
    if query.startswith('genre'):
        genre = query.split(' ', 1)[1]
        return get_music_by_genre(genre)
    elif query.startswith('artist'):
        artist = query.split(' ', 1)[1]
        return get_music_by_artist(artist)
    elif query.startswith('music'):
        music_name = query.split(' ', 1)[1]
        info = get_music_by_name(music_name)
        if not info.empty:
            return f"The song '{info.iloc[0]['track']}' is by '{info.iloc[0]['artist']}' and belongs to the genre '{info.iloc[0]['genre']}'." 
        return "Music not found."
    elif query.startswith('similar'):
        music_name = query.split(' ', 1)[1]
        similar_songs = get_similar_music(music_name)
        if similar_songs is not None:
            return similar_songs
        return "No similar music found."
    else:
        return "Sorry, I didn't understand that."

@app.route("/", methods=["GET", "POST"])
def chatbot():
    response = ""
    result_html = None
    if request.method == "POST":
        user_input = request.form["user_input"]
        if user_input.lower() == "quit":
            response = "Goodbye! Enjoy your music!"
        else:
            result = respond_to_query(user_input)
            if isinstance(result, pd.DataFrame):
                # Convert DataFrame to HTML table
                result_html = result.to_html(classes='table table-striped', index=False)
            else:
                response = result
    return render_template("index.html", response=response, result_html=result_html)

@app.route("/results")
def results():
    result_table = pd.read_csv(r"C:\Users\USER\Downloads\music.csv")  # Example DataFrame, replace with your actual DataFrame
    html_table = result_table.to_html(classes='table table-striped', index=False)
    return render_template('result.html', table_html=html_table)

if __name__ == "__main__":
    app.run(debug=True)
