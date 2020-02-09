import os
import AudioFFmpeg as ffmpeg
import AudioFeatures as af

## Global Parameters
song_directory = 'media/songs/'
segments_len = 30
id = 1

## Get All Songs
for song in list(os.walk(song_directory))[1::]:
    song_directory = song[0]
    song_full_name = ''.join(song[2])
    song_path = song_directory + "/" + song_full_name
    song = ffmpeg.AudioFFmpeg(song_directory, segments_len)

    ## Generate Segments
    song.generate_audio_segments()

    ## Get Audio File Features    
    length = song.get_audio_length()
    segments = round(round(length / segments_len) / 2)
    song_features = af.AudioFeatures(song_directory)

    ## Show Features
    song_path_info = song_directory.split("/")
    print(song_features.format_song_features(id, song_path_info[2], length, (segments, segments + 1)))
    id = id + 1
    break