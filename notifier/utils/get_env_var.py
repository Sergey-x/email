import os


def get_env_var(env_name: str):
    value = os.getenv(env_name, None)

    if value is None:
        raise ValueError(f"Environment variable `{env_name}` must be specified")
    return value
