# Receiving message parameter issue visualized

Here the test_case_using_v2 within test_service_config.py merely fails due to the new default parameter value of max_worker_threads field in the ServiceConfig message in the interface definitions in interfaces.

From the output, one can see that the message exchanged over the wire for messages from two versions is the same (look at the line with "Received binary message = ").

## Running the code

- Ensure that you have the protocol buffers compiler installed as per [this url](https://protobuf.dev/installation/)

- Ensure that you have the uv dependency manager installed as per [this url](https://docs.astral.sh/uv/getting-started/installation/)

Then run the following commands

```bash
uv sync
mkdir ix_v1 ix_v2;
source .venv/bin/activate
sh generate_interface_code.sh;
pytest
```

---

If you are only interested in the output of the test case, then please look at out.txt
