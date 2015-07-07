from expressions import *
constants = None

def generate_output(song, output_file):
    ntracks = len(song.voices) + 1
    clicks_per_beat = 384
    midi_bar = "{0}/{1}".format(song.time_signature.beats_per_bar, song.time_signature.beat_length)
    midi_tempo = 1000000 * 60 * song.tempo.figure.value / (4 * song.tempo.per_minute)
    
    output_file.write('MFile 1 %d %d\n' % (ntracks, clicks_per_beat))
    output_file.write('MTrk\n' % ())
    output_file.write('000:00:000 Tempo %d\n' % (midi_tempo))
    output_file.write('000:00:000 TimeSig %s 24 8\n' % (midi_bar))    
    output_file.write('000:00:000 Meta TrkEnd\n' % ())
    output_file.write('TrkEnd\n' % ())
    
    i = 1
    for voice in song.voices:
        generate_track(voice, i, song.time_signature, clicks_per_beat, output_file)
        i = i + 1

def generate_track(voice, voice_number, time_signature, clicks_per_beat, output_file):
    output_file.write('MTrk\n' % ())
    output_file.write('000:00:000 Meta TrkName "Voz %d"\n' % (voice_number))
    output_file.write('000:00:000 ProgCh ch=%d prog=%d\n' % (voice_number, voice.instrument))
    
    bar_num = 0
    beat_num = 0
    click_num = 0

    for bar in voice.get_bar_executions():
        for action in bar.content:
            
            if type(action) is Note:
                output_file.write('%03d:%02d:%03d On  ch=%d note=%s vol=70\n' % (bar_num, beat_num, click_num, voice_number, action.american_tone_with_octave().ljust(3)))
                temp_click = click_num + action.figure.clicks(clicks_per_beat, time_signature.beat_length)
                click_num = temp_click % clicks_per_beat
                
                temp_beat = beat_num + (temp_click / clicks_per_beat)
                beat_num =  temp_beat % time_signature.beats_per_bar
                
                bar_num = bar_num + (temp_beat / time_signature.beats_per_bar)
                output_file.write('%03d:%02d:%03d Off ch=%d note=%s vol=0\n' % (bar_num, beat_num, click_num, voice_number, action.american_tone_with_octave().ljust(3)))
            else:
                temp_click = click_num + action.figure.clicks(clicks_per_beat, time_signature.beat_length)
                click_num = temp_click % clicks_per_beat                
                temp_beat = beat_num + (temp_click / clicks_per_beat)
                beat_num =  temp_beat % time_signature.beats_per_bar                
                bar_num = bar_num + (temp_beat / time_signature.beats_per_bar)
    
    output_file.write('%03d:%02d:%03d Meta TrkEnd\n' % (bar_num, beat_num, click_num))
    output_file.write('TrkEnd\n' % ())
