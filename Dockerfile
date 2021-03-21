FROM python:3.8-alpine

ENV TZ=Asia/Singapore

RUN addgroup -S scraper && adduser -S scraper -G scraper
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apk --no-cache add firefox \
    wget

RUN wget -qO- https://github.com/mozilla/geckodriver/releases/download/v0.29.0/geckodriver-v0.29.0-linux64.tar.gz \
    | tar xvzf - -C /usr/local/bin \
    && chmod a+x /usr/local/bin/geckodriver

USER scraper


WORKDIR /app


COPY requirements.txt /
RUN pip3 install --upgrade pip \
  && pip3 install -r /requirements.txt \
  && rm -rf requirements.txt

COPY src /app

ENTRYPOINT ["./docker-entrypoint.sh" ]
