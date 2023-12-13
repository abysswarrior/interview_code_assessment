FROM python:3.9
ENV PYTHONUNBUFFERED 1

RUN apt-get update;
RUN apt-get install -y git curl gnupg binutils libproj-dev gdal-bin gettext postgresql-client supervisor

RUN pip install --no-cache-dir -U pip
RUN pip install --no-cache-dir -U gunicorn

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get remove git -y; apt-get autoremove -y; apt-get clean
ENV C_FORCE_ROOT=1

COPY . /code
WORKDIR /code

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
CMD ["/usr/bin/supervisord"]
