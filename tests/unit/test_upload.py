# Copyright 2017 Google Inc.
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

import pytest

import gooresmed.upload as upload_mod


def test_constructor():
    upload = upload_mod.Upload()
    assert upload.total_bytes is None
    assert upload.bytes_transmitted == 0
    assert upload.chunk_size is None


def test_transmit():
    upload = upload_mod.Upload()
    with pytest.raises(NotImplementedError):
        upload.transmit()


def test_transmit_chunk():
    upload = upload_mod.Upload()
    with pytest.raises(NotImplementedError):
        upload.transmit_chunk()