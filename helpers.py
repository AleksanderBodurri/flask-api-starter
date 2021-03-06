from flask_apispec.views import MethodResourceMeta
from flask_restful import Resource as RestfulResource
from marshmallow import Schema, fields


class ErrorResponseSchema(Schema):
    description = fields.Str()


class BaseResource(RestfulResource, metaclass=MethodResourceMeta):
    pass
