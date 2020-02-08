Značajke koje se vade iz .wav datoteka:
----------------------------------------------
1. LENGTH [s] - Dužina pjesme u sekundama.
2. SEGMENTS - Broj segmenata izrezanih iz pjesme (LENGTH/SEGMENT_LEN).
2. TEMPO (Beats Per Minute) - Vrijednost koja prikazuje tempo pjesme.
3. ZERO CROSSING RATE [https://en.wikipedia.org/wiki/Zero-crossing_rate] (ZCR) - Vrijednost promjene signala od pozitivne do negativne vrijednosti.
4. SPECTRAL CENTROID (SC) - Vrijednost koja prikazuje "centar mase" za zvuk. Sporiji žanrovi (blues) imaju SC relativno unutar središta dok užurbaniji žanrovi (metal ili hip-hop) imaju SC izvan središta. 
5. SPECTRAL ROLLOFF (SR) - Vrijednost koja prikazuje oblik signala.
6. MEL-FREQUENCY CEPSTRAL COEFFICIENTS [https://en.wikipedia.org/wiki/Mel-frequency_cepstrum] (MFCC) - Vrijednost kratkih spektara snage zvuka. Obično se koristi za modeliranje karakteristika ljudskog glasa.
7. CHROMA FREQUENCIES [https://labrosa.ee.columbia.edu/matlab/chroma-ansyn/] (CF) - Vrijednost 12 različitih semitonova (chroma) od glazbene oktave.


Literatura:
----------------------------------------------
https://towardsdatascience.com/music-genre-classification-with-python-c714d032f0d8

https://musicinformationretrieval.com/exercise_genre_recognition.html

https://towardsdatascience.com/how-i-understood-what-features-to-consider-while-training-audio-files-eedfb6e9002b