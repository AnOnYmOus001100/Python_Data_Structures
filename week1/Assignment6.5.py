text = "X-DSPAM-Confidence:    0.8475";
num = 0.8475
fd = text.find(str(num))
print(float(text[fd:]))
