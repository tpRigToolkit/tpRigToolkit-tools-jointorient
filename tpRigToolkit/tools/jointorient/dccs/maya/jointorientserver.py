#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module that contains tpRigToolkit-tools-jointorient server implementation
"""

__author__ = "Tomas Poveda"
__license__ = "MIT"
__maintainer__ = "Tomas Poveda"
__email__ = "tpovedatd@gmail.com"

from tpDcc.core import server


class JointOrientServer(server.DccServer, object):

    PORT = 17231

    def _process_command(self, command_name, data_dict, reply_dict):
        super(JointOrientServer, self)._process_command(command_name, data_dict, reply_dict)