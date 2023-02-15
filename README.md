# read-env
Boilerplate code to read API keys from a .env file in Python

## Quickstart

Clone the repo to your computer. Place the `read_env.py` file in any directory where you need to read from a `.env` file. Import the necessary functions from the file as usual. The function options are described in brief below.

- `read_pair_from_env`: Read key pair from specified env file
- `read_key_from_env`: Read API key from specified env file
- `read_sec_from_env`: Read API secret from specified env file

See the source code doc strings for more detailed exaplantion of function behavior.

## Example

The example below assumes you have cloned the repo to the directory where your .env file is to be read from.

```python
from read_env import *

key = read_key_from_env("/Users/MyName/Desktop/PythonFiles/MyPythonProject/my_env_file.env")
```

## Requirements

Run 

```
pip install -r requirements.txt
```
