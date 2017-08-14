# Microbitm module mock.

import mock


class Image:
    def __init__(self, data):
        self.data = data


Image.HAPPY = Image('happy')
Image.ARROW_W = Image('arrow_w')


accelerometer = mock.MagicMock()
sleep = mock.MagicMock()
