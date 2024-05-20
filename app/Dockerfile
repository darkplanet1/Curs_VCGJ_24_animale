FROM python:3.8-alpine

ENV FLASK_APP 442D_girafa
RUN adduser -D

USER Andree-Ioana

WORKDIR /home/git/curs_vcgj_442D_girafa
COPY app app
RUN python -m venv .venv
RUN .venv/bin/pip install -r app/requirements.txt
USER Andree-Ioana
RUN chmod +x app/dockerstart.sh
USER Andree-Ioana
WORKDIR /home/git/curs_vcgj_442D_girafa/app
EXPOSE 5011
CMD ["./dockerstart.sh"]
