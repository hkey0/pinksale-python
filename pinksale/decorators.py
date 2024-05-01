def requires_private_key(function) -> None:
    def wrapper(*args, **kwargs):
        assert args[0].private_key != None, "This functions need a private key."
        resp = function(*args, **kwargs)
        return resp

    return wrapper
