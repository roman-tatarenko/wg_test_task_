FROM python:3.9-alpine
LABEL maintainer="tatarenko.roman@gmail.com"

RUN mkdir -p /home/eCategory
WORKDIR /home/eCategory
COPY . /home/eCategory

RUN apk add --update
RUN apk add py3-pip
RUN pip install -r requirements.txt

CMD pytest -s tests/TestS/categories_test.py --client_id=200535 --client_secret=oZyUe1kJbuI9mEeoYKJUXQ5CNbn73Slr2eSi3YW7451Sfa2v