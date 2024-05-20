FROM python:3.8-alpine

ENV FLASK_APP 442D_elefant
RUN adduser -D oni

USER oni

WORKDIR /home/git/curs_vcgj_442D_elefant
COPY app app
RUN python -m venv .venv
RUN .venv/bin/pip install -r app/requirements.txt
USER root
RUN chmod +x app/dockerstart.sh
USER oni
WORKDIR /home/git/curs_vcgj_442D_elefant/app
EXPOSE 5011
CMD ["./dockerstart.sh"]
