FROM python:rc-slim-buster
RUN ["pip", "install", "web.py"]
RUN ["apt", "update"]
COPY . ./app/
WORKDIR /app/
EXPOSE 8080
# CMD ["python", "Start.py", "-f './Data/IMG_20201216_185903.jpg'"]
CMD ["python", "./app.py"]