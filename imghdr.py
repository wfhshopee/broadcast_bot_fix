# imghdr.py – fallback untuk Python 3.13+
import os

def what(file, h=None):
    if h is None:
        if hasattr(file, 'read'):
            pos = file.tell()
            h = file.read(32)
            file.seek(pos)
        else:
            with open(file, 'rb') as f:
                h = f.read(32)

    for name, test in tests:
        res = test(h)
        if res:
            return res
    return None

def test_jpeg(h):
    if h[6:10] in (b'JFIF', b'Exif'):
        return 'jpeg'
def test_png(h):
    if h.startswith(b'\211PNG\r\n\032\n'):
        return 'png'
def test_gif(h):
    if h[:6] in (b'GIF87a', b'GIF89a'):
        return 'gif'

tests = [
    ('jpeg', test_jpeg),
    ('png', test_png),
    ('gif', test_gif),
]
