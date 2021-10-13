import os

import cv2
import requests
from common.image_utils import img_to_b64
from scipy.io.wavfile import read
from .utils import StreamLitResponse


class PostRequest:
    def __init__(
        self, url: str = "http://localhost:8296", assets_dir: str = "./assets"
    ) -> None:
        self.assets_dir = assets_dir
        self.url = url

    def post(self, tx_type: str) -> None:
        if tx_type == "Test":
            return self.__post_test()
        elif tx_type == "Image":
            return self.__post_img()
        elif tx_type == "Audio":
            return self.__post_audio()
        elif tx_type == "Text":
            return self.__post_text()
        else:
            raise ValueError(f"Error in transmitter type {tx_type}")

    def __post_test(self) -> StreamLitResponse:
        return StreamLitResponse(
            data=requests.get(f"{self.url}/greeting").json(),
            data_type="string",
        )

    def __post_img(self) -> StreamLitResponse:
        img = cv2.imread(os.path.join(self.assets_dir, "cat.png"))
        b64_img = img_to_b64(img)
        payload = {"image": b64_img, "img_size": img.shape}

        response = requests.post(f"{self.url}/process_img", json=payload).json()
        return StreamLitResponse(
            data=response,
            data_type="image",
        )

    def __post_audio(self) -> StreamLitResponse:
        sampling_rate, audio = read(os.path.join(self.assets_dir, "meow.wav"))
        audio = audio / 2.0 ** 15
        noise_freq = 200

        payload = {
            "audio": audio.tolist(),
            "sample_rate": sampling_rate,
            "noise_freq": noise_freq,
        }
        response = requests.post(f"{self.url}/process_audio", json=payload).json()

        return StreamLitResponse(
            data=response,
            data_type="audio",
        )

    def __post_text(self) -> StreamLitResponse:
        with open("assets/felis_catus.txt") as f:
            text = f.readlines()
        response = requests.post(
            f"{self.url}/process_text", json={"text": text[0], "n_words": 10}
        ).json()
        return StreamLitResponse(
            data=response,
            data_type="text",
        )
