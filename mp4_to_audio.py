# -*- coding: utf-8 -*-

import moviepy.editor as mp
clip = mp.VideoFileClip("myvideo.mp4").subclip(0,20)
clip.audio.write_audiofile("theaudio.mp3")
