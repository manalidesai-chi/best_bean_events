import wordcloud
import numpy as np
from PIL import Image
import csv

data = {}
with open('data.csv', 'r') as f:
    for row in csv.DictReader(f):
        data[row['text']] = int(row['y'])**0.7
mask = np.array(Image.open('mask.jpg'))
color = wordcloud.ImageColorGenerator(np.array(Image.open('color.jpeg')))

wc = wordcloud.WordCloud(
    scale=4,
    max_words=2000,
    mask=mask,
    color_func=color,
    prefer_horizontal=1,
)
wc.generate_from_frequencies(data)
wc.to_file('cloud.png')
