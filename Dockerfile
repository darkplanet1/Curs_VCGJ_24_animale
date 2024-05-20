FROM python:3.8-alpine

ENV FLASK_APP 442D_vultur
RUN adduser -D stefan

USER stefan

WORKDIR /home/git/curs_vcgj_442D_vultur
COPY app app
USER root
RUN python -m venv .venv
RUN .venv/bin/pip install -r app/requirements.txt
USER root
RUN chmod +x app/dockerstart.sh
USER stefan
WORKDIR /home/git/curs_vcgj_442D_vultur/app
EXPOSE 5011
CMD ["./dockerstart.sh"]
