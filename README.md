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
Building the packahe
```bash
python setup.py sdist bdist_wheel
```
