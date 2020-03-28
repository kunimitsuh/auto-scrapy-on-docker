# scrapy doesn't work well on alpine
FROM python:3.8.2

WORKDIR /talent

# set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY . .

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

CMD ["/bin/sh", "entrypoint.sh"]
