#!/usr/bin/env bash

# dependencies:
# python-virtualenv
# python-pip

# Activate python environment.
python_env_activate() {
if [ ! -d venv ]; then
    virtualenv -p $(which python) venv
fi
source venv/bin/activate
}

if [ $# -ge 1 ]
then
for i in "$@"
do
case $i in
    -h | --help)
        echo "-h, --help      :Commands help."
        echo "-u, --user      :Create super user for Django."
        echo "-i, --install   :Install all dependencies from requirements.txt"
        echo "-m, --migrate   :Call Django migrate function."
        echo "-r, --run       :Run application."
        echo "-p=*, --port=*  :Run application with custom port."
    ;;
    -u | --user)
        python_env_activate
        python manage.py createsuperuser
    ;;
    -i | --install)
        python_env_activate
        pip install -r requirements.txt
    ;;
    -m | --migrate)
        python_env_activate
        python manage.py migrate
    ;;
    -r | --run)
        python_env_activate
        python manage.py runserver --noreload
    ;;
    -p=* | --port=*)
        python_env_activate
        python manage.py runserver --noreload 0.0.0.0:${i#*=}
    ;;
    *)
      echo "Unknown option."
    ;;
esac
done
else
    python_env_activate
    pip install -r requirements.txt
    python manage.py migrate
    python manage.py runserver --noreload 0.0.0.0:8000
fi