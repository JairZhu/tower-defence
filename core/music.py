import pyaudio
import wave


def play_music():
    """ 循环播放音乐 """
    while True:
        file = wave.open('music/001.wav', 'rb')
        audio = pyaudio.PyAudio()
        stream = audio.open(format=audio.get_format_from_width(file.getsampwidth()),
                            channels=file.getnchannels(),
                            rate=file.getframerate(),
                            output=True)
        data = file.readframes(1024)

        while data != '':
            stream.write(data)
            data = file.readframes(1024)

        stream.stop_stream()
        stream.close()
        file.close()
        audio.terminate()