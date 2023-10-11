def needs_private_key(function):
    def wrapper(*args, **kwargs):
        assert args[0].private_key != None, "This functions needs private key."
        resp = function(*args, **kwargs)
        return resp

    return wrapper
