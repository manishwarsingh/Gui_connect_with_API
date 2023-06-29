# App_Gui_connect_with_API
we can get the data from the database and return to the browser through api's.

## Get Started




#### Windows

3. **Create and activate a virtual environment**
```python
python -m venv .venv
.venv\Scripts\activate
```

4. **Install dependencies**  
```python
python3 -m pip install --upgrade pip && pip3 install -r requirements.txt
```

5. **Run the server locally**  
```python
python <filename.py>
```

#### macOS/ Linux

3. **Create and activate a virtual environment**
```python
python -m venv .venv
source .venv/bin/activate
```

**or **

```python
sudo apt-get install -y python3.10-venv
python3.10 -m venv <name og the env: .venv >
source .venv/bin/activate
```

4. **Install dependencies**
```python
python3 -m pip install --upgrade pip && pip3 install -r requirements.txt
```

5. **Run the server**
```python
python <filename.py>
#or
export FLASK_APP=app.py
flask run
```
