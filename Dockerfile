FROM python:3.8-alpine

ENV FLASK_APP 442D_cangur
RUN adduser -D vladstoica01

USER vladstoica01

WORKDIR /home/Desktop/curs_vcgj_442D_animale
COPY app app
RUN python -m venv .venv
RUN .venv/bin/pip install -r app/requirements.txt
USER root
RUN chmod +x app/dockerstart.sh
USER vladstoica01
WORKDIR /home/Desktop/curs_vcgj_442D_animale/app
EXPOSE 5011
CMD ["./dockerstart.sh"]
