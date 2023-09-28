
band = {
    'vocals': 'Jackson',
    'guitar': 'Hendrix'
}

band2 = dict(vocals= 'Jackson', guitar= 'Hendrix')

print(band)
print(band2)

print(band.items())

print('guitar' in band)
print('bass' in band2)

band['vocals'] = 'Jara'

band.update({'bass': 'Slash'})

print(band)

print(band.pop('bass'))
print(band)

band['drums'] = 'Stark'

print(band)

print(band.popitem())

print(band)

band['drums'] = 'Stark'

print(band)

del band['drums']

print(band)

band2.clear()

print(band2)

del band2


band2 = band.copy()

print(band2)

band3 = dict(band)

print(band3)
