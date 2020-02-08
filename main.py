import AudioFile as afile
import AudioFeatures as af

## Global Parameters
song_path = 'media/songs/'
segments_len = 30

## Generate Audio File Segments

## Get Audio File Features
song = afile.AudioFile(song_path, segments_len)
length = song.get_audio_length()

segments = round(length / segments_len)
segment_path = 'media/segments/segment_%d.wav' % round(segments / 2)
song_features = af.AudioFeatures(segment_path)


## Show Features
print(song_features.extract_all_features("test", length))