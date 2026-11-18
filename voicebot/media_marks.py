async def send_mark(connection, stream_sid, mark_queue):
    if stream_sid:
        await connection.send_json({
            "event": "mark",
            "streamSid": stream_sid,
            "mark": {"name": "responsePart"}
        })
        mark_queue.append("responsePart")
