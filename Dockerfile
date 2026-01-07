FROM python:3.11

WORKDIR /app
COPY . .

RUN pip install -U pip
RUN pip install -e . pytest

CMD ["/bin/bash"]
