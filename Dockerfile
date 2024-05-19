FROM python:3.8-alpine

ENV FLASK_APP 442D_lup
RUN adduser -D vlad

USER vlad

WORKDIR /home/git/vlad_scc
COPY app app
RUN python -m venv .venv
RUN .venv/bin/pip install -r app/requirements.txt
USER root
RUN chmod +x app/dockerstart.sh
USER vlad
WORKDIR /home/git/vlad_scc/app
EXPOSE 5011
CMD ["./dockerstart.sh"]
