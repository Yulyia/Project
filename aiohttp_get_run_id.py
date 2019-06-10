import asyncio
import sys

from aiohttp import web
from subprocess import Popen


async def handler(request):
    data = await request.json()
    run_id = data["run_id"]
    print(run_id)
    Popen([sys.executable, "setup.py", "--run_id=%s" % run_id])
    return web.Response(text="Tests run")


if True:
    app = web.Application()
    app.router.add_route("POST", "/run_id", handler)
    loop = asyncio.get_event_loop()
    f = loop.create_server(app.make_handler(), "127.0.0.1", 1111)
    srv = loop.run_until_complete(f)
    print("serving on", srv.sockets[0].getsockname())

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass
