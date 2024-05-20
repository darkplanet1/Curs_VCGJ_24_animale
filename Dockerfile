FROM python:3.8-alpine

ENV FLASK_APP 442D_vulpe
RUN adduser -D alin

USER alin

WORKDIR /home/git/curs_vcgj_442D_vulpe
COPY app app
USER root
RUN python -m venv .venv

RUN .venv/bin/pip install -r app/requirements.txt

RUN chmod +x app/dockerstart.sh
USER alin
WORKDIR /home/git/curs_vcgj_442D_vulpe/app
EXPOSE 5011
CMD ["./dockerstart.sh"]
