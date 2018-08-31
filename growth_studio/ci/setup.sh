# Setup a proper path, I call my virtualenv dir "py35env" and
# I've got the virtualenv command installed in /usr/local/bin
PATH=$WORKSPACE/py35env/bin:/usr/bin:$PATH
if [ ! -d "py35env" ]; then
  virtualenv --distribute -p /usr/bin/python3.5 py35env
fi
. py35env/bin/activate
pip3 install fabric3
