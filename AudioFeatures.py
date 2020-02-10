import librosa
import numpy as np
import pandas as pd

class AudioFeatures(object):
    """
    Class that handles feature extraction from the given audio file

    (c) 2020. Matej Arlović
    """
    def __init__(self, segment_path):
        self.segment_path = segment_path
        self.audio, self.sample_rate = None, None
        self.harmonic = None

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
        return pd.Series(tempo), pd.Series(sum(beats)), pd.Series(np.average(beats))

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
        return pd.Series(np.mean(zcr)), pd.Series(np.var(zcr)), pd.Series(np.std(zcr))

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
        return pd.Series(np.mean(cent)), pd.Series(np.var(cent)), pd.Series(np.std(cent))

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
        return pd.Series(np.mean(rolloff)), pd.Series(np.var(rolloff)), pd.Series(np.std(rolloff))

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
        return pd.Series(np.mean(chroma)), pd.Series(np.var(chroma)), pd.Series(np.std(chroma))

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
        return pd.Series(np.mean(mfccs)), pd.Series(np.var(mfccs)), pd.Series(np.std(mfccs))

    def extract_mccs_delta(self):
        """
        Extracts the delta value of a Mel-Frequency Cepstral Coefficients of a signal inside audio file.

        Returns
        -------
        mfccs_delta_mean : float 
            mean of delta value of a Mel-Frequency Cepstral Coefficients

        mfccs_delta_var : float
            variance of delta value of a Mel-Frequency Cepstral Coefficients

        mfccs_delta_std : float
            standard deviation of delta value of a Mel-Frequency Cepstral Coefficients
        """
        mfccs = librosa.feature.mfcc(y=self.audio, sr=self.sample_rate, n_mfcc=40)
        mfcc_delta = librosa.feature.delta(mfccs)
        return pd.Series(np.mean(mfcc_delta)), pd.Series(np.var(mfcc_delta)), pd.Series(np.std(mfcc_delta))


    def extract_melspectrogram(self):
        """
        Extracts the Mel Spectrogram of a signal inside audio file.

        Returns
        -------
        mel_mean : float 
            mean of a Mel Spectrogram

        mel_var : float
            variance of a Mel Spectrogram

        mel_std : float
            standard deviation of a Mel Spectrogram
        """
        mel = librosa.feature.melspectrogram(y=self.audio, sr=self.sample_rate)
        return pd.Series(np.mean(mel)), pd.Series(np.var(mel)), pd.Series(np.std(mel))

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
        return pd.Series(np.mean(tonnetz)), pd.Series(np.var(tonnetz)), pd.Series(np.std(tonnetz))

    def extract_spectral_bandwidth(self):
        """
        Extracts the Spectral Bandwidth of a signals energy.

        Returns
        -------
        spec_bw_mean : float 
            mean of a Spectral Bandwidth

        spec_bw_var : float
            variance of a Spectral Bandwidth

        spec_bw_std : float
            standard deviation of a Spectral Bandwidth
        """
        spec_bw = librosa.feature.spectral_bandwidth(y=self.audio, sr=self.sample_rate)
        return pd.Series(np.mean(spec_bw)), pd.Series(np.var(spec_bw)), pd.Series(np.std(spec_bw))

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
        return pd.Series(np.mean(self.harmonic)), pd.Series(np.var(self.harmonic)), pd.Series(np.std(self.harmonic))

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
        return pd.Series(np.mean(percussive)), pd.Series(np.var(percussive)), pd.Series(np.std(percussive))

    def extract_segment_features(self):
        """
        Extracts features from the segments of an audio file.

        Returns
        -------
        features : DataFrame
            Pandas DataFrame of all features
        """

        features = pd.DataFrame()
        features['tempo'], features['total_beats'], features['average_beats'] = self.extract_tempo_beats()
        features['zcr_mean'], features['zcr_var'], features['zcr_std'] = self.extract_zero_crossing()
        features['cent_mean'], features['cent_var'], features['cent_std'] = self.extract_spectral_centroid()
        features['rolloff_mean'], features['rolloff_var'], features['rolloff_std'] = self.extract_spectral_rolloff()
        features['chroma_mean'], features['chroma_var'], features['chroma_std'] = self.extract_chroma_freq()
        features['mfccs_mean'], features['mfccs_var'], features['mfccs_std'] = self.extract_mccs()
        features['mfccs_delta_mean'], features['mfccs_delta_var'], features['mfccs_delta_std'] = self.extract_mccs_delta()
        features['mel_mean'], features['mel_var'], features['mel_std'] = self.extract_melspectrogram()
        features['tonnetz_mean'], features['tonnetz_var'], features['tonnetz_std'] = self.extract_tonnetz()
        features['spec_bw_mean'], features['spec_bw_var'], features['spec_bw_std'] = self.extract_spectral_bandwidth()
        features['harmonic_mean'], features['harmonic_var'], features['harmonic_std'] = self.extract_harmonics()
        features['percussive_mean'], features['percussive_var'], features['percussive_std'] = self.extract_percussive()
        return features

    def format_song_features(self, song_id, song_name, song_length, segments):
        """
        Extracts features from given segments and saves mean into DataFrame.

        Returns
        -------
        features : DataFrame
            Pandas DataFrame with features
        """
        # Extract Segment #1
        self.audio, self.sample_rate = librosa.load(self.segment_path + '/segment_%d.wav' % segments[0])
        self.harmonic = librosa.effects.harmonic(self.audio)
        segment_1 = self.extract_segment_features()

        # Extract Segment #1
        self.audio, self.sample_rate = librosa.load(self.segment_path + '/segment_%d.wav' % segments[1])
        self.harmonic = librosa.effects.harmonic(self.audio)
        segment_2 = self.extract_segment_features()

        # Create Returning DataFrame
        features = pd.DataFrame()
        features['id'] = pd.Series(song_id)
        features['name'] = pd.Series(song_name)
        features['length'] = pd.Series(song_length)
        return pd.concat([features, (segment_1 + segment_2) / 2], axis=1)

        
