import librosa
import numpy as np
import pandas as pd

class AudioFeatures(object):
    """
    Class that handles feature extraction from the given audio file

    (c) 2020. Matej Arlović
    """
    def __init__(self, segment_path):
        self.audio, self.sample_rate = librosa.load(segment_path)
        self.harmonic = librosa.effects.harmonic(self.audio)

    def extract_tempo_beats(self):
        """
        Extracts songs tempo, total beats and average beats.

        Returns
        -------
        tempo : float 
            global tempo inside audio track

        total_beats : float
            sum of beats inside audio track

        average_beats : float
            average beats inside audio track
        """
        tempo, beats = librosa.beat.beat_track(y=self.audio, sr=self.sample_rate)
        return tempo, sum(beats), np.average(beats)

    def extract_zero_crossing(self):
        """
        Extracts zero crossing of a signal inside audio file.

        Returns
        -------
        zcr_mean : float 
            mean of a zero crossing

        zcr_var : float
            variance of a zero crossing

        zcr_std : float
            standard deviation of a zero crossing
        """
        zcr = librosa.feature.zero_crossing_rate(self.audio)
        return np.mean(zcr), np.var(zcr), np.std(zcr)

    def extract_spectral_centroid(self):
        """
        Extracts the Spectral Centroid of a signal inside audio file.

        Returns
        -------
        cent_mean : float 
            mean of a Spectral Centroid

        cent_var : float
            variance of a Spectral Centroid

        cent_std : float
            standard deviation of a Spectral Centroid
        """
        cent = librosa.feature.spectral_centroid(self.audio, sr=self.sample_rate)
        return np.mean(cent), np.var(cent), np.std(cent)

    def extract_spectral_rolloff(self):
        """
        Extracts the Spectral Rolloff of a signal inside audio file.

        Returns
        -------
        rolloff_mean : float 
            mean of a Spectral Rolloff

        rolloff_var : float
            variance of a Spectral Rolloff

        rolloff_std : float
            standard deviation of a Spectral Rolloff
        """
        rolloff = librosa.feature.spectral_rolloff(self.audio, sr=self.sample_rate)
        return np.mean(rolloff), np.var(rolloff), np.std(rolloff)

    def extract_chroma_freq(self):
        """
        Extracts the Chroma Frequency of a signal inside audio file.

        Returns
        -------
        chroma_mean : float 
            mean of a Chroma Frequency

        chroma_var : float
            variance of a Chroma Frequency

        chroma_std : float
            standard deviation of a Chroma Frequency
        """
        stft = np.abs(librosa.stft(self.audio))
        chroma = librosa.feature.chroma_stft(S=stft, sr=self.sample_rate)
        return np.mean(chroma), np.var(chroma), np.std(chroma)

    def extract_mccs(self):
        """
        Extracts the Mel-Frequency Cepstral Coefficients of a signal inside audio file.

        Returns
        -------
        mfccs_mean : float 
            mean of a Mel-Frequency Cepstral Coefficients

        mfccs_var : float
            variance of a Mel-Frequency Cepstral Coefficients

        mfccs_std : float
            standard deviation of a Mel-Frequency Cepstral Coefficients
        """
        mfccs = librosa.feature.mfcc(y=self.audio, sr=self.sample_rate, n_mfcc=40)
        return np.mean(mfccs), np.var(mfccs), np.std(mfccs)

    def extract_tonnetz(self):
        """
        Extracts the Tonnetz of a signal inside audio file.

        Returns
        -------
        tonnetz_mean : float 
            mean of a Tonnetz

        tonnetz_var : float
            variance of a Tonnetz

        tonnetz_std : float
            standard deviation of a Tonnetz
        """
        tonnetz = librosa.feature.tonnetz(y=self.harmonic, sr=self.sample_rate)
        return np.mean(tonnetz), np.var(tonnetz), np.std(tonnetz)

    def extract_harmonics(self):
        """
        Extracts the Harmonics of a signal inside audio file.

        Returns
        -------
        harmonic_mean : float 
            mean of a Harmonics

        harmonic_var : float
            variance of a Harmonics

        harmonic_std : float
            standard deviation of a Harmonics
        """
        return np.mean(self.harmonic), np.var(self.harmonic), np.std(self.harmonic)

    def extract_percussive(self):
        """
        Extracts the Percussive of a signal inside audio file.

        Returns
        -------
        percussive_mean : float 
            mean of a Percussive

        percussive_var : float
            variance of a Percussive

        percussive_std : float
            standard deviation of a Percussive
        """
        percussive = librosa.effects.percussive(self.audio)
        return np.mean(percussive), np.var(percussive), np.std(percussive)

    def extract_all_features(self, song_name, song_length):
        """
        Extracts all features from the audio file.

        Returns
        -------
        features : directory
            directory of all features
        """
        features = pd.DataFrame()
        features['name'] = song_name
        features['length'] = song_length
        features['tempo'], features['total_beats'], features['average_beats'] = self.extract_tempo_beats()
        features['zcr_mean'], features['zcr_var'], features['zcr_std'] = self.extract_zero_crossing()
        features['cent_mean'], features['cent_var'], features['cent_std'] = self.extract_spectral_centroid()
        features['rolloff_mean'], features['rolloff_var'], features['rolloff_std'] = self.extract_spectral_rolloff()
        features['chroma_mean'], features['chroma_var'], features['chroma_std'] = self.extract_chroma_freq()
        features['mfccs_mean'], features['mfccs_var'], features['mfccs_std'] = self.extract_mccs()
        features['tonnetz_mean'], features['tonnetz_var'], features['tonnetz_std'] = self.extract_tonnetz()
        features['harmonic_mean'], features['harmonic_var'], features['harmonic_std'] = self.extract_harmonics()
        features['percussive_mean'], features['percussive_var'], features['percussive_std'] = self.extract_percussive()
        return features