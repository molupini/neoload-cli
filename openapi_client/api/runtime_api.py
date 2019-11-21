# coding: utf-8

"""
    NeoLoad API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from openapi_client.api_client import ApiClient
from openapi_client.exceptions import (
    ApiTypeError,
    ApiValueError
)


class RuntimeApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_tests_run(self, name, project_id, scenario_name, **kwargs):  # noqa: E501
        """Runs a test  # noqa: E501

        Runs a test of the Account according to the method parameters.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_tests_run(name, project_id, scenario_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str name: The name of the test (required)
        :param str project_id: The project Id of the test (required)
        :param str scenario_name: The scenario name of the test (required)
        :param str description: The description of the test
        :param str as_code: The comma-separated as-code files to use for the test. Those files must be part of the uploaded project.
        :param str reservation_id: The reservation identifier to use for the test that can be retrieved from the NeoLoad Web reservation calendar URL. If the reservation mode is enabled and \"reservationId\" value is defined, \"reservationDuration\", \"reservationWebVUs\" and \"reservationSAPVUs\" values will be ignored, otherwise if the reservation mode is disabled the value will be ignored.
        :param int reservation_duration: The duration of the reservation for the test. If the reservation mode is enabled, this value or \"reservationDuration\", \"reservationWebVUs\", \"reservationSAPVUs\" must be defined, otherwise if the reservation mode is disabled the value will be ignored. The value (in seconds) is optional when the reservation mode is enabled and ignored when reservationId value is defined or if the reservation mode is disabled. The default value is the selected scenario duration + 1200 seconds (20 minutes). All reserved resources will be released when the test ends.
        :param int reservation_web_v_us: The number of Web Virtual Users to be reserved for the test. The value is optional when the reservation mode is enabled and ignored when \"reservationId\" value is defined or if the reservation mode is disabled.
        :param int reservation_sapv_us: The number of SAP Virtual Users to be reserved for the test. The value is optional when the reservation mode is enabled and ignored when \"reservationId\" value is defined or if the reservation mode is disabled.
        :param str controller_zone_id: The controller zone Id. If empty, the default zone will be used.
        :param str lg_zones: The LG zones with the number of the LGs. Example: \"ZoneId1:10,ZoneId2:5\". If empty, the default zone will be used with one LG.
        :param bool publish_test_result: When \"true\" and the project is an collaborative project (other than git) then the test result is published onto the server. If empty, the default value is \"false\".
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: RunTestDefinition
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_tests_run_with_http_info(name, project_id, scenario_name, **kwargs)  # noqa: E501

    def get_tests_run_with_http_info(self, name, project_id, scenario_name, **kwargs):  # noqa: E501
        """Runs a test  # noqa: E501

        Runs a test of the Account according to the method parameters.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_tests_run_with_http_info(name, project_id, scenario_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str name: The name of the test (required)
        :param str project_id: The project Id of the test (required)
        :param str scenario_name: The scenario name of the test (required)
        :param str description: The description of the test
        :param str as_code: The comma-separated as-code files to use for the test. Those files must be part of the uploaded project.
        :param str reservation_id: The reservation identifier to use for the test that can be retrieved from the NeoLoad Web reservation calendar URL. If the reservation mode is enabled and \"reservationId\" value is defined, \"reservationDuration\", \"reservationWebVUs\" and \"reservationSAPVUs\" values will be ignored, otherwise if the reservation mode is disabled the value will be ignored.
        :param int reservation_duration: The duration of the reservation for the test. If the reservation mode is enabled, this value or \"reservationDuration\", \"reservationWebVUs\", \"reservationSAPVUs\" must be defined, otherwise if the reservation mode is disabled the value will be ignored. The value (in seconds) is optional when the reservation mode is enabled and ignored when reservationId value is defined or if the reservation mode is disabled. The default value is the selected scenario duration + 1200 seconds (20 minutes). All reserved resources will be released when the test ends.
        :param int reservation_web_v_us: The number of Web Virtual Users to be reserved for the test. The value is optional when the reservation mode is enabled and ignored when \"reservationId\" value is defined or if the reservation mode is disabled.
        :param int reservation_sapv_us: The number of SAP Virtual Users to be reserved for the test. The value is optional when the reservation mode is enabled and ignored when \"reservationId\" value is defined or if the reservation mode is disabled.
        :param str controller_zone_id: The controller zone Id. If empty, the default zone will be used.
        :param str lg_zones: The LG zones with the number of the LGs. Example: \"ZoneId1:10,ZoneId2:5\". If empty, the default zone will be used with one LG.
        :param bool publish_test_result: When \"true\" and the project is an collaborative project (other than git) then the test result is published onto the server. If empty, the default value is \"false\".
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(RunTestDefinition, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['name', 'project_id', 'scenario_name', 'description', 'as_code', 'reservation_id', 'reservation_duration', 'reservation_web_v_us', 'reservation_sapv_us', 'controller_zone_id', 'lg_zones', 'publish_test_result']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_tests_run" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'name' is set
        if self.api_client.client_side_validation and ('name' not in local_var_params or  # noqa: E501
                                                        local_var_params['name'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `name` when calling `get_tests_run`")  # noqa: E501
        # verify the required parameter 'project_id' is set
        if self.api_client.client_side_validation and ('project_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['project_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `project_id` when calling `get_tests_run`")  # noqa: E501
        # verify the required parameter 'scenario_name' is set
        if self.api_client.client_side_validation and ('scenario_name' not in local_var_params or  # noqa: E501
                                                        local_var_params['scenario_name'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `scenario_name` when calling `get_tests_run`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['projectId'] = local_var_params['project_id']  # noqa: E501

        query_params = []
        if 'name' in local_var_params and local_var_params['name'] is not None:  # noqa: E501
            query_params.append(('name', local_var_params['name']))  # noqa: E501
        if 'description' in local_var_params and local_var_params['description'] is not None:  # noqa: E501
            query_params.append(('description', local_var_params['description']))  # noqa: E501
        if 'as_code' in local_var_params and local_var_params['as_code'] is not None:  # noqa: E501
            query_params.append(('asCode', local_var_params['as_code']))  # noqa: E501
        if 'scenario_name' in local_var_params and local_var_params['scenario_name'] is not None:  # noqa: E501
            query_params.append(('scenarioName', local_var_params['scenario_name']))  # noqa: E501
        if 'reservation_id' in local_var_params and local_var_params['reservation_id'] is not None:  # noqa: E501
            query_params.append(('reservationId', local_var_params['reservation_id']))  # noqa: E501
        if 'reservation_duration' in local_var_params and local_var_params['reservation_duration'] is not None:  # noqa: E501
            query_params.append(('reservationDuration', local_var_params['reservation_duration']))  # noqa: E501
        if 'reservation_web_v_us' in local_var_params and local_var_params['reservation_web_v_us'] is not None:  # noqa: E501
            query_params.append(('reservationWebVUs', local_var_params['reservation_web_v_us']))  # noqa: E501
        if 'reservation_sapv_us' in local_var_params and local_var_params['reservation_sapv_us'] is not None:  # noqa: E501
            query_params.append(('reservationSAPVUs', local_var_params['reservation_sapv_us']))  # noqa: E501
        if 'controller_zone_id' in local_var_params and local_var_params['controller_zone_id'] is not None:  # noqa: E501
            query_params.append(('controllerZoneId', local_var_params['controller_zone_id']))  # noqa: E501
        if 'lg_zones' in local_var_params and local_var_params['lg_zones'] is not None:  # noqa: E501
            query_params.append(('lgZones', local_var_params['lg_zones']))  # noqa: E501
        if 'publish_test_result' in local_var_params and local_var_params['publish_test_result'] is not None:  # noqa: E501
            query_params.append(('publishTestResult', local_var_params['publish_test_result']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['NeoloadAuthorizer']  # noqa: E501

        return self.api_client.call_api(
            '/projects/{projectId}/run', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RunTestDefinition',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_upload_project(self, **kwargs):  # noqa: E501
        """Uploads a NeoLoad project zip file or a standalone as code file  # noqa: E501

        Uploads a NeoLoad project of the account corresponding to the parameters. The maximum size file is 250 MB  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_upload_project(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param file file:
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ProjectDefinition
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.post_upload_project_with_http_info(**kwargs)  # noqa: E501

    def post_upload_project_with_http_info(self, **kwargs):  # noqa: E501
        """Uploads a NeoLoad project zip file or a standalone as code file  # noqa: E501

        Uploads a NeoLoad project of the account corresponding to the parameters. The maximum size file is 250 MB  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_upload_project_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param file file:
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ProjectDefinition, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_hosts = ['https://neoload-files.saas.neotys.com/v1']  # noqa: E501
        local_var_host = local_var_hosts[0]
        if kwargs.get('_host_index'):
            if int(kwags.get('_host_index')) < 0 or int(kawgs.get('_host_index')) >= len(local_var_hosts):
                raise ApiValueError("Invalid host index. Must be 0 <= index < %s" % len(local_var_host))
            local_var_host = local_var_hosts[int(kwargs.get('_host_index'))]
        local_var_params = locals()

        all_params = ['file']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params and key != "_host_index":
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_upload_project" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'file' in local_var_params:
            local_var_files['file'] = local_var_params['file']  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['NeoloadAuthorizer']  # noqa: E501

        return self.api_client.call_api(
            '/projects', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ProjectDefinition',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            _host=local_var_host,
            collection_formats=collection_formats)
