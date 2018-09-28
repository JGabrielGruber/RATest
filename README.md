# RATest
REST API Test

## Implementation

### Dependencies

* python3
* python-virtualenv
* python-pip

### Installation
On your terminal:

1. Clone the repository:
```
$ git clone https://github.com/JGabrielGruber/RATest.git
```
2. Create a VirtualEnv:
```
$ virtualenv RATest/
```
2. Go to the project folder:
```
$ cd RATest/
```
3. Change your source:
```
$ source bin/activate
```
4. Install the necessary packages:
```
$ pip install -r package.lock
```
5. Migrate the project:
```
$ python src/manage.py migrate
```
6. Create the static_cdn folder:
```
$ mkdir static_cdn/
```
7. Collect the static files:
```
$ python src/manage.py collectstatic
```
### Usage

To start the server, run:
```
$ python src/manage.py runserver
```
