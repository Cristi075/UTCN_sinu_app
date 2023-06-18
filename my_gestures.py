from kivy.gesture import GestureDatabase, Gesture

gdb = GestureDatabase()


def simplegesture(name, point_list):
    """
    A simple helper function
    """
    g = Gesture()
    g.add_stroke(point_list)
    g.normalize()
    g.name = name
    return g

circle = gdb.str_to_gesture(
    'eNq1WNtyGzcMfd8fiV+iIS4EyB9QXzuTD+g4icbxpLU1ttI2f18QoHa5jpy12qlGAyUw9hA4B'
    'yQh3dx/vf/z++7u8Hz69nSYfumfxzTdfD7C9OHdw+0fh3fTEe2f9kHT84d3z6enx6+HZ/svTz'
    'e/H/N0cxHkg4dNR2lQas8fH+8fTu2x0h6rrzz2a4uajhAZtBS+2yOA0z7tCDMkqjk1y0W1pfN'
    '3+zNN+/dpl0pGqmdLJcv0/PH25+uwr5Onu74EMxErVLeGMT3fNXQDT4C1kopbLVBhG92LB91G'
    'h6RJinRb5A2ZF8euM/aP5JyxhVVShbBiJW9ho7OPcMZG1YTzWzTP2LgAm8XyBmx0bJqxsfSkm'
    '8UqMzaRluVduW5ju5o4qwkKmFWruM28cGLNcW3eriXOWi5kv8zbNK7GcwmbabtP0LXEWcuB7M'
    'Y3pSVxVuRMiGFJaBOcXEzqYrZtwglLEsluBdOSen7R5LiN7nISzehAwsQZwC3yfwJ3PSnP4FZ'
    '31fnNrZX/PS8uKOkCvpBiFkfSF2Sz3PpoC9wVpTqDExXKmkvYmoc274S8nRZ2RXlR1B5u5xGG'
    '1bKcK7a5rtz77ILyIihVSVzL2bb8zuB4LefsgnJ+AzjQtTuUXVBeBCVRTKSMbq1HA/u9b7DMo'
    'hpWSLbPFnZFuf4/6NklzYOki57N1rzAQ8YV/HY3Ztc0L5piXR0BMqAj1GItLmELb/OeXdQ87F'
    'KB8QhIOKDXOXGzOb2BGVc1D9sUaNxJNiPM6LQkbpbS9lbKrmpeVAXluRtTTloXdDs2B95z3UY'
    'XV1UWVe2aPydutqAO6HIt7+KqCm0f7A2+Fk1JkNyiTQ+b8C6rzJdpyrkoQUlhUx6IZ61XEi8u'
    'qyzXKSODTSphAcsAjnBlz4irKvN9CjVxsXEwu2UZ9iopXcmLuqgKWwOMb2JJNoh2y284B9Q11'
    'WU6En2NFuRrFVVXVJdhN71QdDhjBIe3a/3xtg3/n54Oh4d5lFdps7zNmjd7Rt2laY9ad3V88X'
    'Q6apluW0TxiAL2Yc7qTkqjs6RwSjgxnOBOhpUTw6krJ7kz06up2D3iETUiNB7L7pT+WLZhf3h'
    'Ji5CIiLyU4zENZ5SlPYWoVSNZTeGMWv25vWnqzhq1amBKYNaotcTjuUdGrSXy8+rMGbWW7E6u'
    '66SpRUStJRbgvGZDW0QUXqICjgqqjE6q4dSVM19Yrawi4MJqwUIJyTBqg5TGOpC6F1be9ON6t'
    'tdGVkB+XNA2ZYREjwFfCgmSNJKC8/JBjMbyAN0bzLjS5k3dG9RoLJJK95axY9K52KBAohGShB'
    'eCAgncdIFcABj79nJI8JHzT0L6/kg/CQk+mFd5Q/BBtKoRZNzXZz4g+MC0YhSCD+hqXWhGgCA'
    'n1dcFxWAqdV0uND1gMJWCTIyeBnRy7CtZeLl7KbxRLPaykMObXu1k+1rpIb2VL20Hm9siJFKl'
    'TiTqylu7t4SXx31o35ZW3p4zpZVXLyxNsAq5xBIFH/1syH1FCj76Hs69PSn4KHU8k2w+D5aCZ'
    '+lbhKLqGvVJF5+i6hp0yRk3WiLFWSedfepdQOMBCtyFl/GsBe5a9xO4r8axESCNh7UNo+GFVw'
    '95YB57VHuaHL0Pebwy7DYPb79IevLcex/W3n7/0dobhWI+X1buzVEoytprhcYN/OVwf/fl1H7'
    '0sql+ry83CbbfxP66/3z64iF2m9sJZxjmPT3+fni6ffh08L9w/IixfkGL68PDb8enx8/fPsVS'
    'edrnnc05diDYoIA2CpbUvu7t/gFuoPx3')
