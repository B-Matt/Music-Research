"""
    This file helps users to create directory structure that will be used for feature_mining.py.

    (c) 2020. Matej Arlović
"""
import FileManager as fm

songs_dir = "/media/raw"
songs_format_dir = "/media/songs"

file_manager = fm.FileManager(songs_dir, songs_format_dir)
song_genres = file_manager.get_song_geners()

for genre in song_genres:
    songs_by_genre = file_manager.get_songs_by_genre(genre)
    for song in songs_by_genre:
        try:
            file_manager.format_raw_data(song, genre)
        except Exception as e:
            print(e)
            continue