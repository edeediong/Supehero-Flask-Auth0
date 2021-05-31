FROM tiangolo/uwsgi-nginx-flask:python3.8

WORKDIR /app
COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

CMD [ "uwsgi", "--socket", "0.0.0.0:5000", "--protocol=http", "-w", "wsgi:app"  ]