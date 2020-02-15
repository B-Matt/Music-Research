"""
    (c) 2020. Matej Arlović, Franjo Josip Jukić
"""
import librosa
import numpy as np
import itertools 
from concurrent.futures import ThreadPoolExecutor

class AudioFeatures(object):
    """
        Handles feature extraction from the given audio file.
    """
    executors_list = []    

    def __init__(self, segment_path):
        self.segment_path = segment_path

    def extract_segment_features(self, audio_file):
        """
            Extracts features from the segments of an audio file.

            Returns
            -------
            features : List
                List of all features
        """
        audio, sample_rate = librosa.load(audio_file)
        stft = np.abs(librosa.stft(audio))

        harmonic = librosa.effects.harmonic(audio)
        percussive = librosa.effects.percussive(audio)
        tempo, beats = librosa.beat.beat_track(y=audio, sr=sample_rate)
        zcr = librosa.feature.zero_crossing_rate(y=audio)
        cent = librosa.feature.spectral_centroid(y=audio, sr=sample_rate)
        rolloff = librosa.feature.spectral_rolloff(y=audio, sr=sample_rate)
        chroma = librosa.feature.chroma_stft(S=stft, sr=sample_rate)
        chroma_cqt = librosa.feature.chroma_cqt(y=audio, sr=sample_rate)
        chroma_cens = librosa.feature.chroma_cens(y=audio, sr=sample_rate)
        mfccs = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=40)
        mfcc_delta = librosa.feature.delta(mfccs)
        mel = librosa.feature.melspectrogram(y=audio, sr=sample_rate)
        tonnetz = librosa.feature.tonnetz(y=harmonic, sr=sample_rate)
        spec_bw = librosa.feature.spectral_bandwidth(y=audio, sr=sample_rate)
        spec_con = librosa.feature.spectral_contrast(S=stft, sr=sample_rate)        

        features = []
        features.append(tempo)
        features.append(sum(beats))
        features.append(np.average(beats))

        features.append(np.mean(zcr))
        features.append(np.var(zcr))
        features.append(np.std(zcr))

        features.append(np.mean(cent))
        features.append(np.var(cent))
        features.append(np.std(cent))

        features.append(np.mean(rolloff))
        features.append(np.var(rolloff))
        features.append(np.std(rolloff))

        features.append(np.mean(chroma))
        features.append(np.var(chroma))
        features.append(np.std(chroma))

        features.append(np.mean(chroma_cqt))
        features.append(np.var(chroma_cqt))
        features.append(np.std(chroma_cqt))

        features.append(np.mean(chroma_cens))
        features.append(np.var(chroma_cens))
        features.append(np.std(chroma_cens))

        features.append(np.mean(mfccs))
        features.append(np.var(mfccs))
        features.append(np.std(mfccs))

        features.append(np.mean(mfcc_delta))
        features.append(np.var(mfcc_delta))
        features.append(np.std(mfcc_delta))

        features.append(np.mean(mel))
        features.append(np.var(mel))
        features.append(np.std(mel))

        features.append(np.mean(tonnetz))
        features.append(np.var(tonnetz))
        features.append(np.std(tonnetz))

        features.append(np.mean(spec_bw))
        features.append(np.var(spec_bw))
        features.append(np.std(spec_bw))

        features.append(np.mean(spec_con))
        features.append(np.var(spec_con))
        features.append(np.std(spec_con))

        features.append(np.mean(harmonic))
        features.append(np.var(harmonic))
        features.append(np.std(harmonic))

        features.append(np.mean(percussive))
        features.append(np.var(percussive))
        features.append(np.std(percussive))
        return features

    def format_song_features(self, song_id, song_name, song_class, song_length, segments):
        """
            Extracts features from given segments and saves mean into DataFrame.

            Returns
            -------
            None
        """

        # Extract Segments
        with ThreadPoolExecutor(max_workers=50) as executor:            
            if song_length > 31:
                self.executors_list.append(executor.submit(self.extract_segment_features, (self.segment_path + '/x%d.wav' % segments[0])))
                self.executors_list.append(executor.submit(self.extract_segment_features, (self.segment_path + '/x%d.wav' % segments[1])))
            else:
                self.executors_list.append(executor.submit(self.extract_segment_features, (self.segment_path + '/%s.wav' % song_class)))
        
        segment_results = []
        for x in self.executors_list:
            segment_results.append(x.result())
        
        segment_results = np.average(np.array(segment_results), axis=0)

        # Create Returning DataFrame
        features = []
        features.append(song_id)
        features.append(song_name)
        features.append(song_length)
        features = list(itertools.chain(features, segment_results))
        features.append(song_class)
        return features
