import ffmpeg

class AudioFFmpeg(object):
    """
    Handles all FFmpeg and FFprobe processes on an audio file and gives back information about it.
    
    (c) 2020. Matej Arlović
    """
    def __init__(self, path, segments_len):
        self.song_path = path
        self.segments_len = segments_len

    def generate_audio_segments(self):
        """
        Generates equal segments of audio file that last for 30 seconds. 

        Returns
        -------

        None
        """
        ffmpeg.input(self.song_path + '/full.mp3') \
            .output(self.song_path + '/segment_%d.wav', f='segment', segment_time=self.segments_len, map=0) \
            .run()

    def get_audio_length(self):
        """
        Gets duration of an audio file.

        Returns
        -------

        duration : Float
            duration of an audio file
        """
        return float(ffmpeg.probe(self.song_path + "/full.mp3")['format']['duration'])