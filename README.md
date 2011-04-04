Minno Python SDK
================

This is the basic Python SDK for synchronous server-side integration with Minno.

For more information, visit our [API Documentation page](https://www.minno.co/docs).

Usage
-----

This SDK contains a single function `is_purchase_valid()` that returns a boolean
indicating whether the purchase was valid. To start, here is an example of its
server-side usage:

    from project.path import minno

    # Receive these POST variables from your minnoCallback() function
    user_id = request.params["userId"]
    invitem_id = request.params["invitemId"]
    verif_token = request.params["verifToken"]

    if minno.is_purchase_valid(user_id, invitem_id, verif_token):
        # Deliver the purchased item to your user!
    else:
        # Oops, the user hasn't purchased this item!

You receive the `userId`, `invitemId`, and `verifToken` request parameters from
the client-side `minnoCallback()` function that gets executed after a user
purchases an item. You can then POST these parameters to your server endpoint
for verification before giving the user access to your premium item.

The implementation of the verification is very simple--it uses Python's urllib2
module to perform a synchronous GET request to our purchase-verification
endpoint. This can be fairly easily adapted for those running asynchronous web
servers if needed.

Feedback
--------

If you have any questions or comments about this package, feel free to email us
at support@minno.co! We'd love to hear your thoughts!
