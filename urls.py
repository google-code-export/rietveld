# Copyright 2008 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""URL mappings for Rietveld."""

# NOTE: Must import *, since Django looks for things here, e.g. handler500.
from django.conf.urls.defaults import *

urlpatterns = patterns(
    'views',
    (r'^$', 'index'),
    (r'^all$', 'all'),
    (r'^mine$', 'mine'),
    (r'^new$', 'new'),
    (r'^upload$', 'upload'),
    (r'^(\d+)$', 'show'),
    (r'^(\d+)/show$', 'show'),
    (r'^(\d+)/add$', 'add'),
    (r'^(\d+)/edit$', 'edit'),
    (r'^(\d+)/delete$', 'delete'),
    (r'^(\d+)/publish$', 'publish'),
    (r'^(\d+)/download/(\d+)', 'download'),
    (r'^(\d+)/patch/(\d+)/(\d+)$', 'patch'),
    (r'^(\d+)/diff/(\d+)/(\d+)$', 'diff'),
    (r'^(\d+)/diff2/(\d+):(\d+)/(\d+)$', 'diff2'),
    (r'^inline_draft$', 'inline_draft'),
    (r'^repos$', 'repos'),
    (r'^repo_new$', 'repo_new'),
    (r'^repo_init$', 'repo_init'),
    (r'^branch_new/(\d+)$', 'branch_new'),
    (r'^branch_edit/(\d+)$', 'branch_edit'),
    (r'^branch_delete/(\d+)$', 'branch_delete'),
    )