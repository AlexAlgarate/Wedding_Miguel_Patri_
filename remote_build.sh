python -m pip install --upgrade pip
pip install -r requirements.txt
rm -fr public
isort wedding/
black wedding/
ruff check --fix wedding/ 
reflex init
reflex export --frontend-only
unzip frontend.zip -d public
rm -f frontend.zip