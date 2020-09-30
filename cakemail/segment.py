from cakemail_openapi import SegmentApi


class Segment:
    def __init__(self, api):
        self.__api = SegmentApi(api)
        self.create = self.__api.create_segment
        self.delete = self.__api.delete_segment
        self.get = self.__api.get_segment
        self.list = self.__api.list_segments
        self.update = self.__api.patch_segment

    create: SegmentApi.create_segment
    delete: SegmentApi.delete_segment
    get: SegmentApi.get_segment
    list: SegmentApi.list_segments
    update: SegmentApi.patch_segment
