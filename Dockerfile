FROM python:3.8-alpine

ENV FLASK_APP 442D_koala
RUN adduser -D alexandrra26

USER alexandrra26

WORKDIR /home/git/curs_vcgj_442D_koala
COPY app app
USER root
RUN python -m venv .venv
RUN .venv/bin/pip install -r app/requirements.txt
USER root
RUN chmod +x app/dockerstart.sh
USER alexandrra26
WORKDIR /home/git/curs_vcgj_442D_koala/app
EXPOSE 5011
CMD ["./dockerstart.sh"]
