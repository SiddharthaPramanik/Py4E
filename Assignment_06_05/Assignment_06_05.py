text = "X-DSPAM-Confidence:    0.8475"

spos = text.find('0')
num = float(text[spos:])
print(num)
