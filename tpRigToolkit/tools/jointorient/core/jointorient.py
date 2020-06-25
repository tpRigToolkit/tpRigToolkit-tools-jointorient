#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Tool to orient joints quickly
"""

from __future__ import print_function, division, absolute_import

__author__ = "Tomas Poveda"
__license__ = "MIT"
__maintainer__ = "Tomas Poveda"
__email__ = "tpovedatd@gmail.com"

import os

from tpDcc.core import tool
from tpDcc.libs.qt.widgets import toolset

# Defines ID of the tool
TOOL_ID = 'tpRigToolkit-tools-jointorient'


class JointOrientTool(tool.DccTool, object):
    def __init__(self, *args, **kwargs):
        super(JointOrientTool, self).__init__(*args, **kwargs)

    @classmethod
    def config_dict(cls, file_name=None):
        base_tool_config = tool.DccTool.config_dict(file_name=file_name)
        tool_config = {
            'name': 'Joint Orient',
            'id': 'tpRigToolkit-tools-jointorient',
            'logo': 'jointorient',
            'icon': 'jointorient',
            'tooltip': ' Tool to orient joints quickly',
            'tags': ['tpRigToolkit', 'joint', 'orient'],
            'logger_dir': os.path.join(os.path.expanduser('~'), 'tpRigToolkit', 'logs', 'tools'),
            'logger_level': 'INFO',
            'is_checkable': False,
            'is_checked': False,
            'menu_ui': {'label': 'Control Rig', 'load_on_startup': False, 'color': '', 'background_color': ''},
            'menu': [
                {'label': 'Joint Orient',
                 'type': 'menu', 'children': [{'id': 'tpRigToolkit-tools-jointorient', 'type': 'tool'}]}],
            'shelf': [
                {'name': 'Joint Orient',
                 'children': [{'id': 'tpRigToolkit-tools-jointorient', 'display_label': False, 'type': 'tool'}]}
            ]
        }
        base_tool_config.update(tool_config)

        return base_tool_config

    def launch(self, *args, **kwargs):
        return self.launch_frameless(*args, **kwargs)


class JointOrientToolset(toolset.ToolsetWidget, object):

    ID = TOOL_ID

    def __init__(self, *args, **kwargs):
        super(JointOrientToolset, self).__init__(*args, **kwargs)

    def contents(self):

        from tpRigToolkit.tools.jointorient.widgets import jointorient
        joint_orient = jointorient.JointOrientWidget(parent=self)

        return [joint_orient]
