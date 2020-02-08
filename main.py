import ffmpeg
import librosa
import numpy
import sklearn

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
features['segments'] = round(features['length'] / num_segments)

segment_path = 'media/segments/segment_%d.wav' % round(features['segments'] / 2)
audio, sample_rate = librosa.load(segment_path)

# Feature Extraction - TEMPO
onset_env = librosa.onset.onset_strength(audio, sr=sample_rate)
features['tempo'] = librosa.beat.tempo(onset_envelope=onset_env, sr=sample_rate)[0]

# Feature Extraction - ZERO CROSSING RATE
zero_crossings = librosa.zero_crossings(audio, pad=False)
features['zero_crossing_rate'] = sum(zero_crossings)

# Feature Extraction - SPECTRAL CENTROID (normalizacija podataka?)
#features['spectral_centroid'] = librosa.feature.spectral_centroid(audio, sr=sample_rate)[0]

# Feature Extraction - SPECTRAL ROLLOFF (normalizacija podataka?)
#features['spectral_rolloff'] = librosa.feature.spectral_rolloff(audio + 0.01, sr=sample_rate)[0]

# Feature Extraction - MEL-FREQUENCY CEPSTRAL COEFFICIENTS
n_mfcc = 12
mfccs = librosa.feature.mfcc(audio, sr=sample_rate, n_mfcc=n_mfcc).T
scaler = sklearn.preprocessing.StandardScaler()
print("Shape: " + str(mfccs.shape(20, 97)))
features['mfcc'] = scaler.fit_transform(mfccs)

# Feature Extraction - CHROMA FREQUENCIES
#hop_length = 512
#features['chroma'] = librosa.feature.chroma_stft(audio, sr=sample_rate, hop_length=hop_length)

## Show Features
print(features)