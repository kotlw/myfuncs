import functions_framework

from shared import constant
from shared import models
from dataclasses import dataclass, field
import os
import json
from common import constants


@dataclass
class Settings:
    hello: dict = field(default_factory=lambda: json.loads(os.getenv("JSON"))["hello"])
    bye: dict = field(default_factory=lambda: json.loads(os.getenv("JSON"))["bye"])
    st: str = field(default_factory=lambda: os.getenv("ST"))


settings = Settings()

print(settings)

print(constants.COMMON_CONSTANT)
print(constant.MY_CONSTANT)


@functions_framework.http
def handler(request):
    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
        <https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data>
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        <https://flask.palletsprojects.com/en/1.1.x/api/#flask.make_response>.
    Note:
        For more information on how Flask integrates with Cloud
        Functions, see the `Writing HTTP functions` page.
        <https://cloud.google.com/functions/docs/writing/http#http_frameworks>
    """
    print("func2")
    print(constant.MY_CONSTANT)
    return "Hello World!"
