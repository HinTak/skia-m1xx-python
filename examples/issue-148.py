import os
import zipfile

import numpy as np
import requests
import skia
from PIL import Image


def get_font_file():
    directory = 'static/SourceSerif4/'
    font_file = 'SourceSerif4-Regular.ttf'
    path = os.path.join(directory, font_file)
    if not os.path.exists(path):
        url = 'https://fonts.google.com/download?family=Source%20Serif%204'
        r = requests.get(url)
        zip_file_name = 'fonts.zip'
        with open(zip_file_name, 'wb') as f:
            f.write(r.content)

        with zipfile.ZipFile(zip_file_name, 'r') as zip_ref:
            zip_ref.extractall(directory)
    return path


def get_font(is_custom=False):
    if not is_custom:
        return skia.Font(None, 36)
    else:
        file = get_font_file()
        with open(file, 'rb') as f:
            typeface = skia.Typeface.MakeFromData(f.read())
        return skia.Font(typeface, size=36, scaleX=1.0, skewX=0.0)


def main(is_custom=False, decrement_size=False):
    paint = skia.Paint(
        AntiAlias=True,
        Color=skia.Color(255, 0, 0, 255),
        Style=skia.Paint.kFill_Style,
    )

    font = get_font(is_custom)
    print(font.getTypeface(), font.getSize())
    blob = skia.TextBlob('Simple text 123', font=font)

    w, h = 539, 113
    if decrement_size:
        h -= 1
    xy = 10, 50
    frame = np.ones((h, w, 4), dtype=np.uint8) * 255
    print(blob.bounds())
    with skia.Surface(frame) as canvas:
        canvas.drawTextBlob(blob, *xy, paint)
    Image.fromarray(frame).save('skia!.png')



if __name__ == '__main__':
    # main(False, False)  # works
    # main(False, True)  # works
    # main(True, False)  # works
    main(True, True)  # doesnt't work!
