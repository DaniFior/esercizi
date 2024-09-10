mkdir /home/user/cercastringa
copy ./cerca.py home/user/cercastringa
copy ./requirements.txt /home/user/cercastringa
cd /home/user/cercastringa
pip install virtualenv
viritualenv cercastringa
source cerca/bin/activate
pip install -r requirements.txt