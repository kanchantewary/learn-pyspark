from langdetect import detect

x='This is a house'
y='eta ekta bari'
z='yeh ek garh hai'

print(detect(x))
print(detect(y))
print(detect(z))
print(detect('its a house, but eta amar bari noy'))
print(detect('eta ekta bari, but not my house you know'))
print(detect('eai bari ta darun, a beautiful house, awesome'))
