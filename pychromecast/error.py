"""
Errors to be used by PyChromecast.
"""


class PyChromecastError(Exception):
    """ Base error for PyChromecast. """


class NoChromecastFoundError(PyChromecastError):
    """
    When a command has to auto-discover a Chromecast and cannot find one.
    """


class MultipleChromecastsFoundError(PyChromecastError):
    """
    When getting a singular chromecast results in getting multiple chromecasts.
    """


class ChromecastConnectionError(PyChromecastError):
    """ When a connection error occurs within PyChromecast. """


class LaunchError(PyChromecastError):
    """ When an app fails to launch. """


class PyChromecastStopped(PyChromecastError):
    """ Raised when a command is invoked while the Chromecast's socket_client
    is stopped.

    """


class NotConnected(PyChromecastError):
    """
    Raised when a command is invoked while not connected to a Chromecast.
    """


class UnsupportedNamespace(PyChromecastError):
    """
    Raised when trying to send a message with a namespace that is not
    supported by the current running app.
    """


class ControllerNotRegistered(PyChromecastError):
    """
    Raised when trying to interact with a controller while it is
    not registered with a ChromeCast object.
    """
