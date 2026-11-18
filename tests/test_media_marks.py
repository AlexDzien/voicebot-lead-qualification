import unittest
from unittest.mock import AsyncMock

from voicebot.media_marks import send_mark


class MediaMarkTest(unittest.IsolatedAsyncioTestCase):
    async def test_queue_records_only_successfully_sent_marks(self):
        socket = AsyncMock()
        queue = []
        await send_mark(socket, None, queue)
        socket.send_json.assert_not_awaited()

        await send_mark(socket, "stream-fixture", queue)
        socket.send_json.assert_awaited_once_with({
            "event": "mark",
            "streamSid": "stream-fixture",
            "mark": {"name": "responsePart"},
        })
        self.assertEqual(queue, ["responsePart"])

        socket.send_json.side_effect = ConnectionError("closed")
        with self.assertRaises(ConnectionError):
            await send_mark(socket, "stream-fixture", queue)
        self.assertEqual(queue, ["responsePart"])
