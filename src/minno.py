#!/usr/bin/env python
#
# Copyright 2011 Minno, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
#
# Author: Calvin Young <calvin@minno.co>

import json
import urllib2

def is_purchase_valid(user_id, invitem_id, verif_token):
    """Returns a boolean indicating whether the purchase was valid.

    Performs a synchronous GET request to the Minno purchase verification
    endpoint.

    Args:
        user_id, string: the user whose purchase we are validating
        invitem_id, string: the id of the inventory item the user purchased
        verif_token, string: your partner verification token, which can be found
          in the "Settings" tab of the Partner Dashboard

    Exceptions:
        InvalidVerifTokenException: raised if the given verifToken is invalid

    Returns:
        bool: True of the user purchased the item, False otherwise
    """
    purchase_status = urllib2.urlopen(
        "https://www.minno.co/p/%s/%s?verifToken=%s"
        % (user_id, invitem_id, verif_token))

    try:
        json_status = json.loads(purchase_status.read())
        return json_status["isValid"]
    except ValueError:
        raise InvalidVerifTokenException()

class InvalidVerifTokenException(Exception):
    pass
