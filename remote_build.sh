python -m pip install --upgrade pip
pip install -r requirements.txt
echo "INSTALADO"
echo "INSTALADO"
echo "INSTALADO"
echo "INSTALADO"
rm -fr public
isort wedding/
black wedding/
ruff check --fix wedding/
echo "LINTER PASADO"
echo "LINTER PASADO" 
echo "LINTER PASADO"
echo "LINTER PASADO"
reflex init
echo "REFLEX INIT"
echo "REFLEX INIT"
echo "REFLEX INIT"
echo "REFLEX INIT"
echo "REFLEX INIT"
API_URL=https://weddingmiguelpatri-production.up.railway.app reflex export --frontend-only
echo "REFLEX EXPORTED"
echo "REFLEX EXPORTED"
echo "REFLEX EXPORTED"
echo "REFLEX EXPORTED"
unzip frontend.zip -d public
echo "PUBLIC CREADO"
echo "PUBLIC CREADO"
echo "PUBLIC CREADO"
echo "PUBLIC CREADO"
rm -f frontend.zip