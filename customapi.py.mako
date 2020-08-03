from cakemail.wrapper import WrappedApi
from cakemail_openapi import ${super_api_class}


class ${api_class}(WrappedApi):
    """ ${api_class} view of ${super_api_class} """
% for method in methods:
    ${method.name}: ${super_api_class}.${method.super}
% endfor
