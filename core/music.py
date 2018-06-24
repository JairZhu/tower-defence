import pyaudio
import wave
import pygame


def play_music1():
    # 循环播放音乐（解析度低，音质差）
    pygame.mixer.init()
    music = pygame.mixer.Sound('music/001.wav')
    while True:
        music.play()


def play_music2():
    # 循环播放音乐（音质正常，但音乐不会随游戏的结束而停止）
    while True:
        play()

def play():
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
