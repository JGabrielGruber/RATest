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
3. Go to the project folder:
```
$ cd RATest/
```
4. Change your source:
```
$ source bin/activate
```
5. Install the necessary packages:
```
$ pip install -r package.lock
```
6. Migrate the project:
```
$ python src/manage.py migrate
```
7. Create the static_cdn folder:
```
$ mkdir static_cdn/
```
8. Collect the static files:
```
$ python src/manage.py collectstatic
```
### Usage

To start the server, run:
```
$ python src/manage.py runserver
```
