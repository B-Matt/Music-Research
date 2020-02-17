Značajke koje se vade iz .wav datoteka:
----------------------------------------------
1. LENGTH [s] - Dužina pjesme u sekundama.
2. SEGMENTS - Broj segmenata izrezanih iz pjesme (LENGTH/SEGMENT_LEN).
2. TEMPO (Beats Per Minute) - Vrijednost koja prikazuje tempo pjesme.
3. BEATS - Vrijednost koja prikazuje koliko ritma ima u pjesmi.
4. ZERO CROSSING RATE [https://en.wikipedia.org/wiki/Zero-crossing_rate] (ZCR) - Vrijednost promjene signala od pozitivne do negativne vrijednosti.
5. SPECTRAL CENTROID (SC) - Vrijednost koja prikazuje "centar mase" za zvuk. Sporiji žanrovi (blues) imaju SC relativno unutar središta dok užurbaniji žanrovi (metal ili hip-hop) imaju SC izvan središta. 
6. SPECTRAL ROLLOFF (SR) - Vrijednost koja prikazuje oblik signala.
7. MEL-FREQUENCY CEPSTRAL COEFFICIENTS [https://en.wikipedia.org/wiki/Mel-frequency_cepstrum] (MFCC) - Vrijednost kratkih spektara snage zvuka. Obično se koristi za modeliranje karakteristika ljudskog glasa.
8. CHROMA FREQUENCIES [https://labrosa.ee.columbia.edu/matlab/chroma-ansyn/] (CF) - Vrijednost 12 različitih semitonova (chroma) od glazbene oktave.
9. TONNETZ - Vrijednost koja predstavlja tonski prostor unutar pjesme.
10. HARMONIC - Vrijednost koja prikazuje harmonike unutar signala pjesme.
11. PERCUSSIVE - Vrijednost koja prikazuje broj udara unutar pjesme.

Za sve ove značajke se unutar dataseta spremaju vrijednosti medijana, standardne devijacije i varijance kako bi se lakše prepoznao žanr pjesme (label).

Literatura:
----------------------------------------------
https://towardsdatascience.com/music-genre-classification-with-python-c714d032f0d8

https://musicinformationretrieval.com/exercise_genre_recognition.html

https://towardsdatascience.com/how-i-understood-what-features-to-consider-while-training-audio-files-eedfb6e9002b

https://www.kaggle.com/varanr/audio-feature-extraction

https://github.com/danz1ka19/Music-Emotion-Recognition