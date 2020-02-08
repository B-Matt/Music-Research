import ffmpeg
import librosa
import numpy
import sklearn

## Global Parameters
song_path = 'media/songs/1.mp3'
num_segments = 30

## Spliting Audio File Into Segments
in_file = ffmpeg.input(song_path) \
        .output('media/segments/segment_%d.wav', f='segment', segment_time=num_segments, map=0) \
        .run()