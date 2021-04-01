# Wine quality webservice
Check the service https://firast-app.herokuapp.com/

Given certain values of different ingridents used you can predict the possible quality of the wine.
It ranges between 5-9, where 5 is okay and 9 is extraordinary.
## Want to replicate?
To get things started follow the instructions.

Creating a Virtual Envirnment
```bash
virtualenv mlops
```
Activating the envirnment(windows)
```bash
mlops\Scripts\activate
```
Installing the requirements

```bash
pip install -r requirements.txt
```

Create the necessary folders and files

```bash
python template.py
```

tox commands
```bash
tox
```
rebuilding
```bash
tox -r
```

pytest commands
```bash
pytest -v
```
setup commands
```bash
pip install -e .
```
Building the package
```bash
python setup.py sdist bdist_wheel
```
