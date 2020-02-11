import os
import re
import AudioFFmpeg as ffmpeg
import AudioFeatures as af

## Global Parameters
song_directory = 'media/songs/'
csv_directory = 'media/dataset.csv'
segments_len = 30
id = 1

## Get All Songs
for song in list(os.walk(song_directory))[1::]:
    song_directory = song[0]
    song_full_name = ''.join(song[2])
    song_path = song_directory + "/" + song_full_name
    print(song_directory)
    song = ffmpeg.AudioFFmpeg()

    ## Generate Segments
    song.generate_audio_segments(song_path, song_directory, segments_len)

    ## Get Audio File Features    
    length = song.get_audio_length(song_path)
    segments = round(round(length / segments_len) / 2)
    song_features = af.AudioFeatures(song_directory, csv_directory)

    ## Show Features
    song_path_info = song_directory.split("/")
    regex = r"(.mp3)|(.wav)"
    song_full_name = re.sub(regex, "", song_full_name)
    song_features.format_song_features(id, song_path_info[2], song_full_name, length, (segments, segments + 1))
    id = id + 1