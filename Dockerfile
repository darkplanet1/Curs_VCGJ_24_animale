FROM python:3.8-alpine

ENV FLASK_APP 442D_pinguin
RUN adduser -D bee-root

USER bee-root

WORKDIR /home/git/Curs_VCGJ_442D_pinguin
COPY app app
RUN python -m venv .venv
RUN .venv/bin/pip install -r app/requirements.txt
USER root
RUN chmod +x app/dockerstart.sh
USER bee-root
WORKDIR /home/git/Curs_VCGJ_442D_pinguin/app
EXPOSE 5011
CMD ["./dockerstart.sh"]
