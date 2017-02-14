import logging

from aiohttp.web import Request

from opsdroid.matchers import match_webhook
from opsdroid.message import Message


_LOGGER = logging.getLogger(__name__)


@match_webhook("alert")
async def alert(opsdroid, config, message):
    if type(message) is not Message and type(message) is Request:
        # Capture the request json data and set message to a default message
        request = await message.json()
        _LOGGER.debug(request)
        connector = opsdroid.default_connector
        room = config.get("room", connector.default_room)
        message = Message("", None, room, connector)

        # Respond
        await message.respond(
            "{}\n{}".format(request["title"], request["message"]))

        if "imageUrl" in request:
            await message.respond(request["imageUrl"])
