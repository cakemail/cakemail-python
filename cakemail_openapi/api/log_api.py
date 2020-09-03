# coding: utf-8

"""
    Cakemail API

    The Cakemail API exposes multiple APIs including Authentication, Marketing, Contact, Transactional, Analytic, Content, Account and Partner.  # noqa: E501

    The version of the OpenAPI document: 1.0.14
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from cakemail_openapi.api_client import ApiClient
from cakemail_openapi.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class LogApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_campaign_logs(self, campaign_id, **kwargs):  # noqa: E501
        """Show campaign logs  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_campaign_logs(campaign_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int campaign_id: (required)
        :param int account_id:
        :param int start_time:
        :param int end_time:
        :param int page:
        :param int per_page:
        :param bool with_count:
        :param str filter: Valid Terms:   - `additional_info`   - `link_id`   - `contact_id`   - `email`   - `uniques`   - `log_id`   - `totals`   - `type`  Valid Operators:   - `==`  Query separator:   - `;`
        :param str sort: Sort term and direction, using syntax `[-|+]term`.  Valid terms:   - `time`   - `log_id`
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: CampaignLogsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_campaign_logs_with_http_info(campaign_id, **kwargs)  # noqa: E501

    def get_campaign_logs_with_http_info(self, campaign_id, **kwargs):  # noqa: E501
        """Show campaign logs  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_campaign_logs_with_http_info(campaign_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int campaign_id: (required)
        :param int account_id:
        :param int start_time:
        :param int end_time:
        :param int page:
        :param int per_page:
        :param bool with_count:
        :param str filter: Valid Terms:   - `additional_info`   - `link_id`   - `contact_id`   - `email`   - `uniques`   - `log_id`   - `totals`   - `type`  Valid Operators:   - `==`  Query separator:   - `;`
        :param str sort: Sort term and direction, using syntax `[-|+]term`.  Valid terms:   - `time`   - `log_id`
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(CampaignLogsResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'campaign_id',
            'account_id',
            'start_time',
            'end_time',
            'page',
            'per_page',
            'with_count',
            'filter',
            'sort'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_campaign_logs" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'campaign_id' is set
        if self.api_client.client_side_validation and ('campaign_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['campaign_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `campaign_id` when calling `get_campaign_logs`")  # noqa: E501

        if self.api_client.client_side_validation and 'campaign_id' in local_var_params and local_var_params['campaign_id'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `campaign_id` when calling `get_campaign_logs`, must be a value greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and 'page' in local_var_params and local_var_params['page'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `page` when calling `get_campaign_logs`, must be a value greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and 'per_page' in local_var_params and local_var_params['per_page'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `per_page` when calling `get_campaign_logs`, must be a value greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and 'sort' in local_var_params and not re.search(r'[-|+]?.*', local_var_params['sort']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `sort` when calling `get_campaign_logs`, must conform to the pattern `/[-|+]?.*/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'campaign_id' in local_var_params:
            path_params['campaign_id'] = local_var_params['campaign_id']  # noqa: E501

        query_params = []
        if 'account_id' in local_var_params and local_var_params['account_id'] is not None:  # noqa: E501
            query_params.append(('account_id', local_var_params['account_id']))  # noqa: E501
        if 'start_time' in local_var_params and local_var_params['start_time'] is not None:  # noqa: E501
            query_params.append(('start_time', local_var_params['start_time']))  # noqa: E501
        if 'end_time' in local_var_params and local_var_params['end_time'] is not None:  # noqa: E501
            query_params.append(('end_time', local_var_params['end_time']))  # noqa: E501
        if 'page' in local_var_params and local_var_params['page'] is not None:  # noqa: E501
            query_params.append(('page', local_var_params['page']))  # noqa: E501
        if 'per_page' in local_var_params and local_var_params['per_page'] is not None:  # noqa: E501
            query_params.append(('per_page', local_var_params['per_page']))  # noqa: E501
        if 'with_count' in local_var_params and local_var_params['with_count'] is not None:  # noqa: E501
            query_params.append(('with_count', local_var_params['with_count']))  # noqa: E501
        if 'filter' in local_var_params and local_var_params['filter'] is not None:  # noqa: E501
            query_params.append(('filter', local_var_params['filter']))  # noqa: E501
        if 'sort' in local_var_params and local_var_params['sort'] is not None:  # noqa: E501
            query_params.append(('sort', local_var_params['sort']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2PasswordBearer']  # noqa: E501

        return self.api_client.call_api(
            '/logs/campaigns/{campaign_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CampaignLogsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_email_logs(self, log_type, **kwargs):  # noqa: E501
        """Show transactional email logs  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_email_logs(log_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str log_type: (required)
        :param int account_id:
        :param int start_time:
        :param int end_time:
        :param int page:
        :param int per_page:
        :param bool with_count:
        :param str filter: Valid Terms:   - `group_id`  Valid Operators:   - `==`  Query separator:   - `;`
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: EmailLogsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_email_logs_with_http_info(log_type, **kwargs)  # noqa: E501

    def get_email_logs_with_http_info(self, log_type, **kwargs):  # noqa: E501
        """Show transactional email logs  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_email_logs_with_http_info(log_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str log_type: (required)
        :param int account_id:
        :param int start_time:
        :param int end_time:
        :param int page:
        :param int per_page:
        :param bool with_count:
        :param str filter: Valid Terms:   - `group_id`  Valid Operators:   - `==`  Query separator:   - `;`
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(EmailLogsResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'log_type',
            'account_id',
            'start_time',
            'end_time',
            'page',
            'per_page',
            'with_count',
            'filter'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_email_logs" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'log_type' is set
        if self.api_client.client_side_validation and ('log_type' not in local_var_params or  # noqa: E501
                                                        local_var_params['log_type'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `log_type` when calling `get_email_logs`")  # noqa: E501

        if self.api_client.client_side_validation and 'page' in local_var_params and local_var_params['page'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `page` when calling `get_email_logs`, must be a value greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and 'per_page' in local_var_params and local_var_params['per_page'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `per_page` when calling `get_email_logs`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'log_type' in local_var_params and local_var_params['log_type'] is not None:  # noqa: E501
            query_params.append(('log_type', local_var_params['log_type']))  # noqa: E501
        if 'account_id' in local_var_params and local_var_params['account_id'] is not None:  # noqa: E501
            query_params.append(('account_id', local_var_params['account_id']))  # noqa: E501
        if 'start_time' in local_var_params and local_var_params['start_time'] is not None:  # noqa: E501
            query_params.append(('start_time', local_var_params['start_time']))  # noqa: E501
        if 'end_time' in local_var_params and local_var_params['end_time'] is not None:  # noqa: E501
            query_params.append(('end_time', local_var_params['end_time']))  # noqa: E501
        if 'page' in local_var_params and local_var_params['page'] is not None:  # noqa: E501
            query_params.append(('page', local_var_params['page']))  # noqa: E501
        if 'per_page' in local_var_params and local_var_params['per_page'] is not None:  # noqa: E501
            query_params.append(('per_page', local_var_params['per_page']))  # noqa: E501
        if 'with_count' in local_var_params and local_var_params['with_count'] is not None:  # noqa: E501
            query_params.append(('with_count', local_var_params['with_count']))  # noqa: E501
        if 'filter' in local_var_params and local_var_params['filter'] is not None:  # noqa: E501
            query_params.append(('filter', local_var_params['filter']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2PasswordBearer']  # noqa: E501

        return self.api_client.call_api(
            '/logs/emails', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='EmailLogsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_list_logs(self, list_id, **kwargs):  # noqa: E501
        """Show list logs  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_list_logs(list_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int list_id: (required)
        :param int account_id:
        :param int start_time:
        :param int end_time:
        :param int page:
        :param int per_page:
        :param bool with_count:
        :param str filter: Valid Terms:   - `additional_info`   - `contact_id`   - `email`   - `uniques`   - `track_id`   - `log_id`   - `start_id`   - `end_id`   - `totals`   - `type`  Valid Operators:   - `==`  Query separator:   - `;`
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ListLogsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_list_logs_with_http_info(list_id, **kwargs)  # noqa: E501

    def get_list_logs_with_http_info(self, list_id, **kwargs):  # noqa: E501
        """Show list logs  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_list_logs_with_http_info(list_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int list_id: (required)
        :param int account_id:
        :param int start_time:
        :param int end_time:
        :param int page:
        :param int per_page:
        :param bool with_count:
        :param str filter: Valid Terms:   - `additional_info`   - `contact_id`   - `email`   - `uniques`   - `track_id`   - `log_id`   - `start_id`   - `end_id`   - `totals`   - `type`  Valid Operators:   - `==`  Query separator:   - `;`
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ListLogsResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'list_id',
            'account_id',
            'start_time',
            'end_time',
            'page',
            'per_page',
            'with_count',
            'filter'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_list_logs" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'list_id' is set
        if self.api_client.client_side_validation and ('list_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['list_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `list_id` when calling `get_list_logs`")  # noqa: E501

        if self.api_client.client_side_validation and 'list_id' in local_var_params and local_var_params['list_id'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `list_id` when calling `get_list_logs`, must be a value greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and 'page' in local_var_params and local_var_params['page'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `page` when calling `get_list_logs`, must be a value greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and 'per_page' in local_var_params and local_var_params['per_page'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `per_page` when calling `get_list_logs`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'list_id' in local_var_params:
            path_params['list_id'] = local_var_params['list_id']  # noqa: E501

        query_params = []
        if 'account_id' in local_var_params and local_var_params['account_id'] is not None:  # noqa: E501
            query_params.append(('account_id', local_var_params['account_id']))  # noqa: E501
        if 'start_time' in local_var_params and local_var_params['start_time'] is not None:  # noqa: E501
            query_params.append(('start_time', local_var_params['start_time']))  # noqa: E501
        if 'end_time' in local_var_params and local_var_params['end_time'] is not None:  # noqa: E501
            query_params.append(('end_time', local_var_params['end_time']))  # noqa: E501
        if 'page' in local_var_params and local_var_params['page'] is not None:  # noqa: E501
            query_params.append(('page', local_var_params['page']))  # noqa: E501
        if 'per_page' in local_var_params and local_var_params['per_page'] is not None:  # noqa: E501
            query_params.append(('per_page', local_var_params['per_page']))  # noqa: E501
        if 'with_count' in local_var_params and local_var_params['with_count'] is not None:  # noqa: E501
            query_params.append(('with_count', local_var_params['with_count']))  # noqa: E501
        if 'filter' in local_var_params and local_var_params['filter'] is not None:  # noqa: E501
            query_params.append(('filter', local_var_params['filter']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2PasswordBearer']  # noqa: E501

        return self.api_client.call_api(
            '/logs/lists/{list_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ListLogsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
