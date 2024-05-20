#!/bin/sh
echo `pwd`
echo "Activare venv:"
. ../.venv/bin/activate
echo `pwd`
echo "Configurare variabila mediu FLASK_APP"
export FLASK_APP=442D_koala
echo "Start server:"
exec flask run -h 0.0.0.0 -p 5020 --reload
