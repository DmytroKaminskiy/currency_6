FROM python:3.9

WORKDIR /home/build

COPY requirements.txt .

# RUN apt update -y && apt install -y curl

RUN pip install -r requirements.txt

ENV PYTHONPATH "/home/build/app"

COPY . .

CMD ["tail", "-f", "/dev/null"]
