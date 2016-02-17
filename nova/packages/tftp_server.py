# -*- encoding: utf-8 -*-
'''
:rational: TFTP does not support authentication nor does it ensure the
confidentiality of integrity of data. It is recommended that TFTP be removed,
unless there is a specific need for TFTP. In that case, extreme caution must be
used when configuring the services.

:maintainer: HubbleStack
:maturity: 20160216
:depends: SaltStack
:platform: Linux
:compatibility: all

'''
from __future__ import absolute_import
from nova import *
import logging


def __virtual__():
    '''
    Compatibility Check
    '''
    if not salt.utils.is_windows():
        return True
    return False


def audit():
    if not _package('tftp-server'):
        return True
    return False
