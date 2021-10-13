import enum
from common.image_utils import b64_to_img
import streamlit as st
import numpy as np


class StreamLitResponse:
    def __init__(self, data: dict, data_type: str) -> None:
        self.data = data
        self.data_type = data_type

    def show(self):
        if self.data_type == "string":
            st.write(self.data)
        elif self.data_type == "image":
            st.image(b64_to_img(self.data["image"]))
        elif self.data_type == "text":
            st.write(self.data)
        elif self.data_type == "audio":
            st.audio(np.array(self.data["audio"]))
        else:
            raise ValueError(f"Error in data_type {self.data_type}")


class TxType(enum.Enum):
    test = "Test"
    image = "Image"
    audio = "Audio"
    text = "Text"

    @classmethod
    def has_value(cls, item):
        return item in cls.__members__.values()
