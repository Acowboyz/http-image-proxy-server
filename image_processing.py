from io import BytesIO

import requests
from PIL import Image
from typing import Union


def image_processing(url: str) -> tuple:
    img_io = None
    response = get_image(url)

    if response is None:
        return img_io, 'get_image_error', False

    img_io = resize_image(response)

    if img_io is None:
        return img_io, 'resize_error', False

    return img_io, 'success', True


def get_image(url: str) -> requests.models.Response:
    try:
        response = requests.get(url)
    except Exception as e:
        print(e)
        response = None

    return response


def resize_image(response: requests.models.Response) -> Union[BytesIO, None]:
    try:
        img = Image.open(BytesIO(response.content))
    except Exception as e:
        print(e)
        return None

    width, height = img.size

    print(img.size)

    if width == height:
        resize_t = (500, 500)
    elif width > height:  # 123 x 569
        scale_ratio = 500 / width
        resize_t = (500, int(height * scale_ratio))
    elif width < height:  # 253 x 578
        scale_ratio = 500 / height
        resize_t = (int(width * scale_ratio), 500)

    img_io = BytesIO()
    img.resize(resize_t).save(img_io, format='PNG')
    img_io.seek(0, 0)

    return img_io
