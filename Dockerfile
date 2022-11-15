FROM alpine
WORKDIR /app
EXPOSE 9001

COPY requirements.txt /app
COPY main.py /app

USER root
#RUN sed -i 's/https/http/' /etc/apk/repositories
RUN apk  --no-cache update && apk  --no-cache add gcc linux-headers python3 python3-dev libc-dev py3-pip
RUN python3 -m pip install -r requirements.txt

ENTRYPOINT ["python3", "/app/main.py"]
