from ix_v1 import v1_pb2
from ix_v2 import v2_pb2


def component2(message):
    print(f"Received binary message = {message.SerializeToString().hex()}")
    assert (
        message.max_worker_threads < 6
    ), f"Max worker threads cannot be greater than 6"

    print("Configuration message accepted")


def fill_message(message):
    message.service_name = "Component2"
    message.request_timeout_ms = 3000
    return message


def test_case_using_v1():
    # simulate component 3 filling a message to send
    message = v1_pb2.ServiceConfig()
    filled_message = fill_message(message)
    component2(filled_message)


def test_case_using_v2():
    # simulate component 3 filling a message to send
    message = v2_pb2.ServiceConfig()
    filled_message = fill_message(message)
    component2(filled_message)
