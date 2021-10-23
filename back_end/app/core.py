import logging
import math

import config
import cv2
import numpy as np

from .common.image_utils import b64_to_img, img_to_b64

logging.basicConfig(level=config.LOGLEVEL)
logger = logging.getLogger(__name__)


def word_count(text: str) -> dict:
    counts = dict()
    words = text.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts


def keep_n_words(data: dict, n_rows: int) -> dict:
    return dict(sorted(data.items(), key=lambda x: x[1], reverse=True)[:n_rows])


def process_image(payload: dict, scale: int = 1.5) -> dict:
    image = b64_to_img(payload["image"])
    img = cv2.resize(image, None, fx=scale, fy=scale, interpolation=cv2.INTER_LINEAR)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    return {"image": img_to_b64(img)}


def process_audio(payload: dict) -> dict:
    audio = np.array(payload["audio"])
    sine_noise = np.array(
        [
            math.sin(2 * math.pi * payload["noise_freq"] * (x / payload["sample_rate"]))
            for x in range(len(audio))
        ]
    )

    combined_signal = audio + sine_noise[:, None]

    return {"audio": combined_signal.tolist()}


def process_text(payload: dict) -> dict:
    all_words = word_count(payload["text"])
    return keep_n_words(all_words, payload["n_words"])
