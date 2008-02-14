# Author: Dimitri Fontaine <dim@tapoueh.org>
#
# pgloader logging facility
#
# standard error levels are used for code and configuration error messages
# data error logging is managed by tools.Reject class

from tools import PGLoader_Error
import logging

def init(client_min_messages = logging.INFO,
         log_min_messages = logging.DEBUG, filename = '/tmp/pgloader.log'):
    """ set the console logging """

    fmt = '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'

    try:
        logging.basicConfig(level    = log_min_messages,
                            format   = fmt,
                            datefmt  = '%d-%m-%Y %H:%M:%S',
                            filename = filename,
                            filemode = 'w')
    except IOError, e:
        raise PGLoader_Error, e

    console = logging.StreamHandler()
    console.setLevel(client_min_messages)

    formatter = logging.Formatter('%(name)-12s %(levelname)-8s %(message)s')
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)

    return logging.getLogger('pgloader')

def getLogger(name):
    """ return a new logger instance named name, properly configured """
    return logging.getLogger(name)

def level(name):
    """ return a logging level from user string """

    if name.upper() == 'DEBUG':
        return logging.DEBUG

    elif name.upper() == 'INFO':
        return logging.INFO

    elif name.upper() == 'WARNING':
        return logging.WARNING

    elif name.upper() == 'ERROR':
        return logging.ERROR

    elif name.upper() == 'CRITICAL':
        return logging.CRITICAL

    else:
        return logging.NOTSET