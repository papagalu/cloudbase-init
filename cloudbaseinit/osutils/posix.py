# Copyright 2012 Cloudbase Solutions Srl
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import os
import subprocess

from cloudbaseinit.osutils import base


class PosixUtils(base.BaseOSUtils):

    def reboot(self):
        os.system('reboot')

    def set_host_name(self, new_hostname):
        # os.system('hostname ' + new_hostname)
        subprocess.call(['hostname', new_hostname])

    def get_config_value(self, name, instance_id):
        pass

    def set_config_value(self, plugin_name, status, instance_id):
        pass
