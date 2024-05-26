FROM python:3.8-alpine

ENV FLASK_APP 442D_Rechin
RUN adduser -D Andrei0302

USER Andrei0302

WORKDIR /home/git/Curs_VCGJ_24_animale
COPY app app
RUN python -m venv .venv
RUN .venv/bin/pip install -r app/requirements.txt
USER root
RUN chmod +x app/dockerstart.sh
USER Andrei0302
WORKDIR /home/git/Curs_VCGJ_24_animale/app
EXPOSE 5011
CMD ["./dockerstart.sh"]
