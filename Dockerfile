FROM python:3.8-alpine

ENV FLASK_APP 442D_arici
RUN adduser -D oni



WORKDIR /home/git/mihai
COPY app app
RUN python -m venv .venv
RUN .venv/bin/pip install -r app/requirements.txt

RUN chmod +x app/dockerstart.sh

WORKDIR /home/git/mihai/app
EXPOSE 5011
CMD ["./dockerstart.sh"]
