FROM python-3.1.1

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8051

CMD ["bash","start.sh"]