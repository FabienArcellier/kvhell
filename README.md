## Motivation

Welcome in hell. As a students you will have to implement your own key value store.

That's a way to discuss all the abstraction and component you will have to think to produce
a system reliable and finally visualize the real challenge to create a pretty simple database.

## Synopsis

kvhell is a simple kvalue store that expose service as REST API.

```bash
curl -X PUT http://localhost:8888/france_capital -d "PARIS"

# fetch the value from the key france_capital
curl http://localhost:8888/france_capital

# remove all the key france_capital
curl -X DELETE http://localhost:8888/france_capital

# remove all the keys from the storage
curl -X DELETE http://localhost:8888
```

You can use postman as a browser extension to send http request.```

## The latest version

You can find the latest version to git@github.com:FabienArcellier/kvhell.git

```bash
git clone git@github.com:FabienArcellier/kvhell.git
```

## Installation

Use make to instanciate a python virtual environment in ./venv and install the
python dependencies.

```bash
virtualenv venv
source venv/bin/activate
pip install -r requirements_dev.txt
```

## Usage

Kvhell is a webserver you can run with this command

```python
python -m kvhell
```

From here, you can use curl to run and execute commands

## Benchmark

```
cd kvhell_benchmark; pytest
```

![simple benchmark](https://cloud.githubusercontent.com/assets/159559/24716739/42601394-1a30-11e7-8e40-207eff69b0a4.png)

## Contributors

* Fabien Arcellier

## License

A short snippet describing the license (MIT, Apache, etc.)
