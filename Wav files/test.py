
import wave

# help(wave)

# https://docs.python.org/2/library/wave.html



wf = wave.open('pronunciation_en_anything (16).wav')
# wf = wave.open('arctic_a0001.wav')

print 'number of channels: ', wf.getnchannels() 
print 'framerate: ', wf.getframerate() 
print 'signal length: ', wf.getnframes() 
print 'bytes per frame:', wf.getsampwidth() 

