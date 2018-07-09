playlist = {
    'title':"ABC",
    'author': "aut1",
    'song': [{'name': 'DMCLDS', 'artist': ['abdbs', 'kdcndks'], 
'duration': 3.55},
{'name': 'RRDTCHMMD', 'artist': ['ksnjn'], 
'duration': 2.1},
{'name': 'RNKASXSKAC', 'artist': ['abdbs'], 
'duration': 5.2}]
}
total_duration =0
for song in playlist.get('song'):
    total_duration +=song.get('duration')
print('Total length of playlist:', total_duration)