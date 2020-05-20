"""
    (c) 2020. Matej Arlovic, Franjo Josip Jukic
"""
import ffmpeg

class AudioFFmpeg(object):
    """
    Handles all FFmpeg and FFprobe processes on an audio file and gives back information about it.
    """
    def __init__(self):
        pass

    def generate_audio_segments(self, song_path, song_dir, segments_len):
        """
        Generates equal segments of audio file that last for 30 seconds. 

        Returns
        -------

        None
        """
        ffmpeg.input(song_path) \
            .output(song_dir + '/x%d.wav', f='segment', map_metadata=-1, segment_time=segments_len) \
            .run()

    def get_audio_length(self, song_path):
        """
            Gets duration of an audio file.

            Returns
            -------

            duration : Float
                duration of an audio file
        """
        return float(ffmpeg.probe(song_path)['format']['duration'])

