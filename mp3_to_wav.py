# -*- coding: utf-8 -*-

from pydub import AudioSegment

sound = AudioSegment.from_mp3("out.mp3")
sound.export("new.wav", format="wav")
