import ffmpeg
import librosa
import sklearn
import numpy as np
import pandas as pd

## Global Parameters
song_path = 'media/songs/1.mp3'
num_segments = 30
features = {}

## Spliting Audio File Into Segments
in_file = ffmpeg.input(song_path) \
        .output('media/segments/segment_%d.wav', f='segment', segment_time=num_segments, map=0) \
        .run()

## Feature Extraction
file_info = ffmpeg.probe(song_path)

# Feature Extraction - LENGTH & SEGMENTS
features['length'] = float(file_info['format']['duration'])
segments = round(features['length'] / num_segments)

segment_path = 'media/segments/segment_%d.wav' % round(segments / 2)
audio, sample_rate = librosa.load(segment_path)

# Feature Extraction - TEMPO & BEATS
onset_env = librosa.onset.onset_strength(audio, sr=sample_rate)
tempo, beats = librosa.beat.beat_track(y=audio, sr=sample_rate)

features['tempo'] = tempo
features['beats'] = sum(beats)

# Feature Extraction - ZERO CROSSING RATE
zero_crossings = librosa.feature.zero_crossing_rate(audio)
features['zcr_mean'] = np.mean(zero_crossings)
features['zcr_var'] = np.var(zero_crossings)
features['zcr_std'] = np.std(zero_crossings)

# Feature Extraction - SPECTRAL CENTROID
spectral_centroid = librosa.feature.spectral_centroid(audio, sr=sample_rate)
features['cent_mean'] = np.mean(spectral_centroid)
features['cent_var'] = np.var(spectral_centroid)
features['cent_std'] = np.std(spectral_centroid)

# Feature Extraction - SPECTRAL ROLLOFF
spectral_rolloff = librosa.feature.spectral_rolloff(audio, sr=sample_rate)
features['rolloff_mean'] = np.mean(spectral_rolloff)
features['rolloff_var'] = np.var(spectral_rolloff)
features['rolloff_std'] = np.std(spectral_rolloff)

# Feature Extraction - MEL-FREQUENCY CEPSTRAL COEFFICIENTS
mfccs = np.mean(librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=40).T, axis=0)
features['mfccs_mean'] = np.mean(mfccs)
features['mfccs_var'] = np.var(mfccs)
features['mfccs_std'] = np.std(mfccs)

# Feature Extraction - CHROMA FREQUENCIES
stft = np.abs(librosa.stft(audio))
chroma = np.mean(librosa.feature.chroma_stft(S=stft, sr=sample_rate).T, axis=0)
features['chroma_mean'] = np.mean(chroma)
features['chroma_var'] = np.var(chroma)
features['chroma_std'] = np.std(chroma)

# Feature Extraction - TONNETZ
tonnetz = np.mean(librosa.feature.tonnetz(y=librosa.effects.harmonic(audio), sr=sample_rate).T, axis=0)
features['tonnetz_mean'] = np.mean(tonnetz)
features['tonnetz_var'] = np.var(tonnetz)
features['tonnetz_std'] = np.std(tonnetz)

# Feature Extraction - HARMONIC
harmonic = librosa.effects.harmonic(audio)
features['harmonic_mean'] = np.mean(harmonic)
features['harmonic_var'] = np.var(harmonic)
features['harmonic_std'] = np.std(harmonic)

# Feature Extraction - PERCUSSIVE
percussive = librosa.effects.percussive(audio)
features['percussive_mean'] = np.mean(harmonic)
features['percussive_var'] = np.var(harmonic)
features['percussive_std'] = np.std(harmonic)

## Show Features
print(features)