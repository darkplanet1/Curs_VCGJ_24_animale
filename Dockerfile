FROM python:3.8-alpine

ENV FLASK_APP 442D_tigru
RUN adduser -D LeoGeanovu

USER LeoGeanovu

WORKDIR /home/git/curs_vcgj_442D_tigru
COPY app app
RUN python -m venv .venv
RUN .venv/bin/pip install -r app/requirements.txt
USER root
RUN chmod +x app/dockerstart.sh
USER LeoGeanovu
WORKDIR /home/git/curs_vcgj_442D_tigru/app
EXPOSE 5011
CMD ["./dockerstart.sh"]
