FROM python:3.6
ADD . /app
WORKDIR /app
ENV PYTHONPATH /
RUN pip3 install -r requirements.txt
RUN pip3 install -e .
EXPOSE 5001

