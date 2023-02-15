# read-env
Boilerplate code to read API keys from a .env file in Python

# Quickstart

Functions to choose from include 

- `read_pair_from_env`: Read key pair from specified env file
- `read_key_from_env`: Read API key from specified env file
- `read_sec_from_env`: Read API secret from specified env file

You can install the <code>read-env-keys</code> package via pip

```
pip3 install read-env-keys
```

After installing, you will be able to import the module using

```
from read_env_keys import *
```

or

```
import read_env_keys
```

## Read an API key from your .env file

After you have installed the package, create an env file (if you do not have one already) in your current working directory (cwd). 

- ### MacOS / Unix

  Get the current working directory's absolute path by typing
  ```
  pwd
  ```
  in the terminal. Copy and paste this as a string with the name of your env file appended (including the `.env` extension) as an argument.

- ### Windows

  Get the current working directory's absolute path by typing
  ```
  cd
  ```
  in the command line.

Once you have the full path to the env file, pass it as an argument. You can optionally specifiy the API key name to read. 

```python 
from read_env_keys import *

# Read an API Key. Default key name is 'API_KEY'
api_key_value = read_key_from_env(YOUR_ENVS_ABSOLUTE_FILEPATH)
# Read an API Key and specify the key name in the env file
api_key_value = read_key_from_env(YOUR_ENVS_ABSOLUTE_FILEPATH, api_key='my_key')
```


