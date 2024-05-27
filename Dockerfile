FROM python:3.8-alpine

ENV FLASK_APP 442D_Leu
RUN adduser -D Valentin886

USER Valentin886

WORKDIR /home/git/Curs_VCGJ_24_animale
COPY app app
RUN python -m venv .venv
RUN .venv/bin/pip install -r app/requirements.txt
USER root
RUN chmod +x app/dockerstart.sh
USER Valentin886
WORKDIR /home/git/Curs_VCGJ_24_animale/app
EXPOSE 5011
CMD ["./dockerstart.sh"]
