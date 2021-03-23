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

Initialize git
```bash
git init
```
Initialize dvc
```bash
dvc init
```
Add the data to dvc
```bash
dvc add actual_data\winquality.csv
```

Add files to git
```bash
git add .
```

commit

```bash
git commit -m "First commit"
```
