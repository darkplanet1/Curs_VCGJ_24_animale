FROM python:3.8-alpine

ENV FLASK_APP 442D_urspanda
RUN adduser -D victor

USER victor

WORKDIR /home/git/curs_vcgj_442D_urspanda
COPY app app
USER root
RUN python -m pip install --upgrade pip
RUN python -m venv .venv

RUN .venv/bin/pip install -r app/requirements.txt

RUN chmod +x app/dockerstart.sh
USER victor
WORKDIR /home/git/curs_vcgj_442D_urspanda/app
EXPOSE 5011
CMD ["./dockerstart.sh"]
