.\venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
reflex init
reflex export --frontend-only
rm -rf public
upzip frontend.zip -d public
rm -f frontend.zip
deactivate

