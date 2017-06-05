# -*- coding: utf-8 -*-

import moviepy.editor as mp
clip = mp.VideoFileClip("sample_data/test.mp4").subclip(0,20)
clip.audio.write_audiofile("test.mp3")
