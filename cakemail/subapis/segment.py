from cakemail.wrapper import WrappedApi
from cakemail_openapi import SegmentApi


class Segment(WrappedApi):
    """ Segment view of SegmentApi """
    create: SegmentApi.create_segment
    delete: SegmentApi.delete_segment
    get: SegmentApi.get_segment
    list: SegmentApi.list_segments
    update: SegmentApi.patch_segment
