"""
    Handles formating GTZAN dataset files from blues.0000.wav to blues0.wav.

    (c) 2020. Matej Arlović
"""

import os
import classes.filemanager as fm

songs_dir = "/media/songs/raw"

file_manager = fm.FileManager(songs_dir, songs_dir)

song_genres = file_manager.get_song_geners()

for genre in song_genres:
    songs_by_genre = file_manager.get_songs_by_genre(genre)
    file_manager.format_song_name(songs_by_genre, genre, '.wav')