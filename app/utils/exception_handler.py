from rest_framework.views import exception_handler
from rest_framework.response import Response

def custom_exception_handler(exc, context):
    handlers ={
      'ValidationError': _handle_validation_error,
      'DoesNotExist': _record_does_not_exist
    }
    response = exception_handler(exc, context)
    exception_class = exc.__class__.__name__
    if exception_class in handlers:
      return handlers[exception_class](exc,context, response)


    return Response('Something went wrong', status = 422)

def _record_does_not_exist(exc,context,response):
  return Response(str(exc), status = 404)
def _handle_validation_error(exc, context, response):
  return Response(exc, status = 422)