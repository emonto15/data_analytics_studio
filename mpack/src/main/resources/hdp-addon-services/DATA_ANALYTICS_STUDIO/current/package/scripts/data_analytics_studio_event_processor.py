#!/usr/bin/env python
"""
  HORTONWORKS DATAPLANE SERVICE AND ITS CONSTITUENT SERVICES

  (c) 2016-2018 Hortonworks, Inc. All rights reserved.

  This code is provided to you pursuant to your written agreement with Hortonworks, which may be the terms of the
  Affero General Public License version 3 (AGPLv3), or pursuant to a written agreement with a third party authorized
  to distribute this code.  If you do not have a written agreement with Hortonworks or with an authorized and
  properly licensed third party, you do not have any rights to this code.

  If this code is provided to you under the terms of the AGPLv3:
  (A) HORTONWORKS PROVIDES THIS CODE TO YOU WITHOUT WARRANTIES OF ANY KIND;
  (B) HORTONWORKS DISCLAIMS ANY AND ALL EXPRESS AND IMPLIED WARRANTIES WITH RESPECT TO THIS CODE, INCLUDING BUT NOT
    LIMITED TO IMPLIED WARRANTIES OF TITLE, NON-INFRINGEMENT, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE;
  (C) HORTONWORKS IS NOT LIABLE TO YOU, AND WILL NOT DEFEND, INDEMNIFY, OR HOLD YOU HARMLESS FOR ANY CLAIMS ARISING
    FROM OR RELATED TO THE CODE; AND
  (D) WITH RESPECT TO YOUR EXERCISE OF ANY RIGHTS GRANTED TO YOU FOR THE CODE, HORTONWORKS IS NOT LIABLE FOR ANY
    DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, PUNITIVE OR CONSEQUENTIAL DAMAGES INCLUDING, BUT NOT LIMITED TO,
    DAMAGES RELATED TO LOST REVENUE, LOST PROFITS, LOSS OF INCOME, LOSS OF BUSINESS ADVANTAGE OR UNAVAILABILITY,
    OR LOSS OR CORRUPTION OF DATA.
"""

from resource_management.libraries.functions.check_process_status import check_process_status
from resource_management.libraries.script.script import Script

from data_analytics_studio import data_analytics_studio
from data_analytics_studio_service import data_analytics_studio_service


class DataAnalyticsStudioEventProcessor(Script):
  def install(self, env):
    self.install_packages(env)

  def configure(self, env, upgrade_type=None, config_dir=None):
    import params
    env.set_params(params)
    data_analytics_studio(name = "data_analytics_studio_event_processor")

  def start(self, env, upgrade_type=None):
    import params
    env.set_params(params)
    self.configure(env)

    data_analytics_studio_service("data_analytics_studio_event_processor", action = "start")

  def stop(self, env, upgrade_type=None):
    import params
    env.set_params(params)
    data_analytics_studio_service("data_analytics_studio_event_processor", action = "stop" )

  def status(self, env):
    import status_params
    env.set_params(status_params)
    check_process_status(status_params.data_analytics_studio_event_processor_pid_file)

  def get_log_folder(self):
    import params
    return params.data_analytics_studio_log_dir
  
  def get_user(self):
    import params
    return params.data_analytics_studio_user

  def get_pid_files(self):
    import status_params
    return [status_params.data_analytics_studio_event_processor_pid_file]

if __name__ == "__main__":
  DataAnalyticsStudioEventProcessor().execute()
