FROM tiangolo/uwsgi-nginx-flask:python3.8

WORKDIR /app
COPY . /app/

RUN pip install -r requirements.txt

# ENV API_ACCESS_KEY API_ACCESS_KEY
# ENV CLIENT_ID CLIENT_ID
# ENV CLIENT_SECRET CLIENT_SECRET
# ENV API_BASE_URL API_BASE_URL

EXPOSE 5000

CMD [ "uwsgi", "--socket", "0.0.0.0:5000", "--protocol=http", "-w", "wsgi:app"  ]