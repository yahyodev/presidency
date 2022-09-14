from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from collections import OrderedDict

def _positive_int(integer_string, strict=False, cutoff=None):
    """
    Cast a string to a strictly positive integer.
    """
    ret = int(integer_string)
    if ret < 0 or (ret == 0 and strict) or ret > 24:
        raise ValueError()
    if cutoff:
        return min(ret, cutoff)
    return ret


class CustomLimitOffsetPaginator(LimitOffsetPagination):
    limit_query_param = 'limit'
    offset_query_param = 'offset'
    max_limit = 500

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('total_count', self.count),
            ('next_link', self.get_next_link()),
            ('previous_link', self.get_previous_link()),
            ('count', len(data)), #min(self.get_limit(self.request),  max(self.count-self.offset, 0))
            ('results', data)
        ]))