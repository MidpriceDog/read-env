import requests
from dotenv import load_dotenv
from pathlib import Path
import os
import time
import urllib.parse
import hashlib
import hmac
import base64


def read_pair_from_env(abs_path: str, api_key='API_KEY', api_sec='API_SEC'):
    """Read key pair from specified env file

    Parameters
    ----------
    abs_path : str
        Absolute file path to the .env file
    api_key : str, optional
        Name of the api key in the .env file, by default 'API_KEY'
    api_sec : str, optional
        Name of the api secret key in the .env file, by default 'API_SEC'

    Returns
    -------
    tuple
        ordered pair of the API key value followed by the API secret value from the .env file
    """
    dotenv_path = Path(abs_path)
    load_dotenv(dotenv_path=dotenv_path)
    return (os.getenv(api_key), os.getenv(api_sec))


def read_key_from_env(abs_path: str, api_key='API_KEY'):
    """Read API key from specified env file

    Parameters
    ----------
    abs_path : str
        Absolute file path to the .env file
    api_key : str, optional
        Name of the api key in the .env file, by default 'API_KEY'

    Returns
    -------
    str
        Value of the API key stored in the .env file
    """
    dotenv_path = Path(abs_path)
    load_dotenv(dotenv_path=dotenv_path)
    return os.getenv(api_key)


def read_sec_from_env(abs_path: str, api_sec='API_SEC'):
    """Read API secret from specified env file

    Parameters
    ----------
    abs_path : str
         Absolute file path to the .env file
    api_sec : str, optional
        Name of the api secret key in the .env file, by default 'API_SEC'

    Returns
    -------
    str
        Value of the API secret stored in the .env file
    """
    dotenv_path = Path(abs_path)
    load_dotenv(dotenv_path=dotenv_path)
    return os.getenv(api_sec)
