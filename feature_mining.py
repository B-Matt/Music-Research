import os
import re
from joblib import Parallel, delayed
import AudioFFmpeg as ffmpeg
import AudioFeatures as af

## Global Parameters
song_directory = 'media/songs/'
csv_directory = 'media/dataset.csv'
segments_len = 30
id = 1
n_jobs = 4

## Process Songs
def process_songs(song):
    global id
    song_directory = song[0]
    song_full_name = song[2][0]
    song_path = song_directory + "/" + song_full_name
    ffmpeg_song = ffmpeg.AudioFFmpeg()

    ## Generate Segments
    length = ffmpeg_song.get_audio_length(song_path)
    if length > 30:
        try:
            if song[2][1] is None:
                pass
        except IndexError:
            ffmpeg_song.generate_audio_segments(song_path, song_directory, segments_len)        

    ## Get Audio File Features
    segments = round(round(length / segments_len) / 2)
    song_features = af.AudioFeatures(song_directory, csv_directory)

    ## Show Features
    song_path_info = song_directory.split("/")
    regex = r"(.mp3)|(.wav)"
    song_full_name = re.sub(regex, "", song_full_name)
    song_features.format_song_features(id, song_path_info[2], song_full_name, length, (segments, segments + 1))
    id = id + 1

## Paralel Feature Extraction
Parallel(n_jobs=n_jobs, prefer="threads")(delayed(process_songs)(song) for song in list(os.walk(song_directory))[1::])