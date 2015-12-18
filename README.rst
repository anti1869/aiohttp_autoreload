aiohttp_autoreload
==================

Makes aiohttp server autoreload on source code change.

It's very first, heavily untested version that should be used only in development.

Code is taken from tornado.autoreload module.

call_periodic module is taken from akaIDIOT's gist https://gist.github.com/akaIDIOT/48c2474bd606cd2422ca


Instalation
-----------

.. code::

    pip install aiohttp_autoreload


Proposed usage
--------------

.. code:: python

    import asyncio
    import aiohttp_autoreload

    debug = True  # Or false

    loop = asyncio.get_event_loop()
    handler = app.make_handler(
        debug=debug,
    )

    if debug:
        aiohttp_autoreload.start()

    f = loop.create_server(handler, '0.0.0.0', 8080)
    ...


