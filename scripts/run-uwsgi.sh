DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )
echo $DIR
. ../env/bin/activate
pip install webapp2
pip install rethinkdb
uwsgi --uid www-data --gid www-data --socket 127.0.0.1:3031 --chdir $DIR/../backend/ --wsgi-file main.wsgi --master --processes 4 --threads 2 --stats 127.0.0.1:9191 --die-on-term --chmod-socket