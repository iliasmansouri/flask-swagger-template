FROM python:3.6

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y

COPY back_end/requirements.txt /
RUN pip3 install --no-cache-dir -r requirements.txt

COPY back_end /back_end
COPY common /back_end/app

WORKDIR /back_end

ENTRYPOINT ["gunicorn", "--log-level", "INFO", "-b", ":8296", "-t", "120", "run:APP"]