import os
import re
import pandas as pd
import classes.audio_ffmpeg as ffmpeg
import classes.features as af
import time

start_time = time.time()
## Global Parameters
song_directory = os.path.normpath(os.getcwd() + "/media/songs/")
csv_directory = os.path.normpath(os.getcwd() + "/dataset/dataset_new.csv")
segments_len = 30
song_id = 3404

## Process Songs
features = []

def extract_features(song):
    global song_id, features

    song_directory = song[0]
    song_genre = song[2][0]
    song_path = song_directory + "/" + song_genre
    song_name = os.path.basename(song_directory)

    ffmpeg_song = ffmpeg.AudioFFmpeg()

    ## Generate Segments
    length = ffmpeg_song.get_audio_length(song_path)
    if length > 31:
        try:
            if song[2][1] is None:
                pass
        except IndexError:
            ffmpeg_song.generate_audio_segments(song_path, song_directory, segments_len)        

    ## Get Audio File Features
    segments = round(round(length / segments_len) / 2)
    song_features = af.AudioFeatures(song_directory)

    ## Show Features
    regex = r"(.mp3)|(.wav)"
    song_genre = re.sub(regex, "", song_genre)
    data = song_features.format_song_features(song_id, song_name, song_genre, length, (segments, segments + 1))

    features.append(data)
    print(" %s) %s" % (song_id, song_name))
    song_id = song_id + 1

def save_features_csv(csv_name, feature_list):
    """
        Appends extracted features to the CSV file.

        Returns
        -------
        None
    """
    dataset = pd.DataFrame(feature_list)
    dataset.to_csv(csv_name, mode='a', header=False, index=False)  

## Process Songs Inside Directory
for song in list(os.walk(song_directory))[1::]:
    extract_features(song)

save_features_csv(csv_directory, features)
print("  Feature extraction took: %s seconds." % (time.time() - start_time))