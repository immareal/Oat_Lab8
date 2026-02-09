import matplotlib.pyplot as plt
import librosa
import librosa.display

y, sr = librosa.load("825417_843915-hq.mp3", duration=180)

fig, (ax) = plt.subplots(nrows=1, sharex=True, figsize=(10, 4))

ax.set(
    title='Sample view'
)

librosa.display.waveshow(
    y, sr=sr, ax=ax, marker='.', label='Full signal'
)

ax.label_outer()
ax.legend()

plt.show()
