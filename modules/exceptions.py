class DuplicateArgumentError(Exception):
    """
    Raise when duplicate arguments are found
    """
    pass

class InvalidProfileFileError(Exception):
    """
    Raise when an invalid profile file is received
    """
    pass

class MandatoryParamsMissingError(Exception):
    """
    Raise when mandatory parameters are missing
    """
    pass

class LoginFailedError(Exception):
    """
    Raise in case of an unsuccessful login
    """
    pass

class ConflictingParamsError(Exception):
    """
    Raise when conflicting parameters are found
    """
    pass

class InvalidAccountError(Exception):
    """
    Raise when an invalid account is found
    """
    pass

class InvalidBrowserError(Exception):
    """
    Raise when an invalid browser is specified
    """
    pass

class InvalidBrowserProfileError(Exception):
    """
    Raise when an invalid browser profile path is received
    """
    pass