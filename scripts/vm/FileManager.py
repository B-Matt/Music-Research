"""
    (c) 2020. Matej Arlović, Franjo Josip Jukić
"""
import os
import re
from shutil import copyfile

class FileManager(object):
    """
        Handles files and folder when user wants to extract features for custom dataset.
    """
    def __init__(self, raw_path, formated_path):
        self.raw_path = os.path.normpath(os.getcwd() + raw_path)
        self.formated_path = os.path.normpath(os.getcwd() + formated_path)

    def get_song_geners(self):
        """
            Gets list of all music geners from raw directory. 
            Every directory inside raw directory is a gener.

            Returns
            -------

            geners : List
                list of geners inside raw directory
        """
        geners = []
        for (_, dirnames, _) in os.walk(self.raw_path):
            geners.extend(dirnames)
        return geners

    def get_songs_by_genre(self, song_genre):
        """
            Gets list of all song files inside given directory.

            Returns
            -------

            songs : List
                list of audio files inside given directory
        """
        songs = []
        for (_, _, filenames) in os.walk(os.path.join(self.raw_path, song_genre)):
            songs.extend(filenames)
        return songs 

    def format_song_name(self, songs, song_genre, song_extension):
        """
            Renames songs name from GTZAN notation to ours (blues.00000.wav -> blues0.wav).

            Returns
            -------

            None
        """
        song_dir = os.path.join(self.raw_path, song_genre)
        song_id = 0

        for (root, _, filenames) in os.walk(song_dir):
            for file in filenames:
                old_name = os.path.join(root, file)
                new_name = os.path.join(root, "gtzan_" + song_genre + str(song_id) + song_extension)                
                os.rename(old_name, new_name)
                song_id = song_id + 1

    def format_raw_data(self, song, song_genre):
        """
            Makes new directory, copy audio file there and renames file according to our format.

            Returns
            -------

            None
        """        
        songs_old_path = os.path.join(self.raw_path, song_genre)
        songs_old_path_full = os.path.join(songs_old_path, song)
        _, song_extension = os.path.splitext(songs_old_path_full)

        regex = r"(\s.mp3)|(\s.wav)"
        song = re.sub(regex, song_extension, song)
        songs_new_path = os.path.join(self.formated_path, song)
        regex = r"(.mp3)|(.wav)"
        songs_new_path = re.sub(regex, "", songs_new_path)

        songs_new_path_full = os.path.join(songs_new_path, song)        
        songs_new_name = os.path.join(songs_new_path, (song_genre + song_extension))

        os.mkdir(songs_new_path)
        copyfile(songs_old_path_full, songs_new_path_full)
        os.rename(songs_new_path_full, songs_new_name)