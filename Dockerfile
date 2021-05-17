FROM python:3.8.1

WORKDIR /app
COPY . /app/

RUN pip install -r requirements.txt

RUN ./bulma-setup.sh

CMD [ "/bin/bash" ]