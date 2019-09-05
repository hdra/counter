FROM python:3

WORKDIR /usr/src/app

COPY . .

ENV step 1

CMD ["./run.sh"]
