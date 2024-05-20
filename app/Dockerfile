FROM python:3.8-alpine

ENV FLASK_APP 442D_foca
RUN adduser -D natys12

USER oni

WORKDIR /home/git/curs_vcgj_442D_foca
COPY app app
RUN python -m venv .venv
RUN .venv/bin/pip install -r app/requirements.txt
USER root
RUN chmod +x app/dockerstart.sh
USER oni
WORKDIR /home/git/curs_vcgj_442D_foca/app
EXPOSE 5011
CMD ["./dockerstart.sh"]
