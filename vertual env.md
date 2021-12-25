### Check install packages:
$ pip list
$ pip freeze 
### create vertual environment (at first goto the file directory where we want to make the env)
$ python -m venv [name of the environment]
$
###### or
$ python3 -m venv [name of the environment]
$
###### example 
$ python -m venv env_name
$

### activate this env (supppose our env_name= 'pipenv' and we are in that folder): we need to loacte activate file and run:
$ pipenv\Scripts\activate
$
Example:
<img src="vertual env.JPG" alt="alt" width="100%">

### we can deactivate the virtual env by"
$ pipenv\Scripts\deactivate
$


# by pipenv:
1. first istall --> 
$ pip install pip env
$
### goto the directory where we want to create the environment-->
$ pipenv install requests
$ inviroment will be created and to activate $ pipenve shell

