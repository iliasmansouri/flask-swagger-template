import streamlit as st

from .post import PostRequest
from .utils import TxType


def run():
    post_request = PostRequest()
    radio_value = st.sidebar.radio("Select task", tuple(t.value for t in TxType))
    st_response = post_request.post(radio_value)
    st_response.show()


if __name__ == "__main__":
    run()
