FROM python:3.8-alpine

ENV FLASK_APP 442D_delfin
RUN adduser -D octa

USER octa

WORKDIR /home/git/curs_vcgj_442D_delfin
COPY app app
USER root
RUN python -m venv .venv

RUN .venv/bin/pip install -r app/requirements.txt

RUN chmod +x app/dockerstart.sh
USER octa
WORKDIR /home/git/curs_vcgj_442D_delfin/app
EXPOSE 5011
CMD ["./dockerstart.sh"]
