import pytest
import requests
from pytest_testrail.plugin import pytestrail


@pytestrail.case('C13271')
def test_checkPersonesStructure_with_valid_data(host, port,
                                                payload_checkPersonesStructure,
                                                data_person, response):
    person = data_person
    payload = payload_checkPersonesStructure(
        person,
        locationOfPersones='award'
    )
    actualresult = requests.post(f'{host}:{port.eAccess}/command2', json=payload).json()

    assert actualresult == response.success


@pytestrail.case('C13272')
def test_checkPersonesStructure_without_optional_attribute_identifier_uri(host, port,
                                                                          payload_checkPersonesStructure,
                                                                          response, data_person):
    person = data_person
    del person['identifier']['uri']
    payload = payload_checkPersonesStructure(
        person,
        locationOfPersones='award'
    )
    actualresult = requests.post(f'{host}:{port.eAccess}/command2', json=payload).json()

    assert actualresult == response.success


@pytestrail.case('C13273')
def test_checkPersonesStructure_without_optional_attribute_businessFunctions_documents(host, port,
                                                                                       payload_checkPersonesStructure,
                                                                                       data_person, response):
    person = data_person
    del person['businessFunctions'][0]['documents']
    payload = payload_checkPersonesStructure(
        person,
        locationOfPersones='award'
    )
    actualresult = requests.post(f'{host}:{port.eAccess}/command2', json=payload).json()

    assert actualresult == response.success


@pytestrail.case('C13274')
def test_checkPersonesStructure_without_optional_attribute_documents_description(host, port,
                                                                                 payload_checkPersonesStructure,
                                                                                 data_person, response):
    person = data_person
    del person['businessFunctions'][0]['documents'][0]['description']
    payload = payload_checkPersonesStructure(
        person,
        locationOfPersones='award'
    )
    actualresult = requests.post(f'{host}:{port.eAccess}/command2', json=payload).json()

    assert actualresult == response.success


@pytestrail.case('C13275')
def test_checkPersonesStructure_more_than_one_document_object(host, port,
                                                              payload_checkPersonesStructure,
                                                              data_person, data_document, response):
    person = data_person
    person['businessFunctions'][0]['documents'].append(data_document)
    payload = payload_checkPersonesStructure(
        person,
        locationOfPersones='award'
    )
    actualresult = requests.post(f'{host}:{port.eAccess}/command2', json=payload).json()

    assert actualresult == response.success


@pytestrail.case('C13294')
def test_checkPersonesStructure_more_than_one_person_object(host, port,
                                                            payload_checkPersonesStructure,
                                                            data_person, response):
    person_1 = data_person
    person_2 = data_person
    payload = payload_checkPersonesStructure(
        person_1, person_2,
        locationOfPersones='award'
    )
    actualresult = requests.post(f'{host}:{port.eAccess}/command2', json=payload).json()

    assert actualresult == response.success


@pytestrail.case('C13295')
def test_checkPersonesStructure_more_than_one_businessFunction_object(host, port,
                                                                      payload_checkPersonesStructure,
                                                                      data_person, data_businessFunction, response):
    person = data_person
    person['businessFunctions'].append(data_businessFunction)
    payload = payload_checkPersonesStructure(
        person,
        locationOfPersones='award'
    )
    actualresult = requests.post(f'{host}:{port.eAccess}/command2', json=payload).json()

    assert actualresult == response.success


@pytestrail.case('C13276')
def test_checkPersonesStructure_attribute_documentType_mismatch_with_enum(host, port,
                                                                          payload_checkPersonesStructure,
                                                                          data_person, response):
    person = data_person
    person['businessFunctions'][0]['documents'][0]['documentType'] = 'x_eligibilityDocuments'
    payload = payload_checkPersonesStructure(
        person,
        locationOfPersones='award'
    )
    actualresult = requests.post(f'{host}:{port.eAccess}/command2', json=payload).json()

    response.error['result'] = [
        {
            "code": "DR-3/3",
            "description": "Attribute value mismatch with one of enum expected values."
                           " Expected values: 'regulatoryDocument',"
                           " actual value: 'x_eligibilityDocuments'.",
            "details": [{"name": "documentType"}]
        }
    ]

    assert actualresult == response.error


@pytestrail.case('C13277')
def test_checkPersonesStructure_attribute_businessFunctionType_mismatch_with_enum(host, port,
                                                                                  payload_checkPersonesStructure,
                                                                                  data_person, response):
    person = data_person
    person['businessFunctions'][0]['type'] = 'authority'
    payload = payload_checkPersonesStructure(
        person,
        locationOfPersones='award'
    )
    actualresult = requests.post(f'{host}:{port.eAccess}/command2', json=payload).json()

    response.error['result'] = [
        {
            "code": "DR-3/3",
            "description": "Attribute value mismatch with one of enum expected values."
                           " Expected values: 'chairman, procurementOfficer, contactPoint,"
                           " technicalEvaluator, technicalOpener, priceOpener, priceEvaluator',"
                           " actual value: 'authority'.",
            "details": [{"name": "businessFunction.type"}]
        }
    ]

    assert actualresult == response.error


@pytestrail.case('C16389')
def test_checkPersonesStructure_param_locationOfPersones_mismatch_with_enum(host, port,
                                                                            payload_checkPersonesStructure,
                                                                            data_person, response):
    person = data_person
    payload = payload_checkPersonesStructure(
        person,
        locationOfPersones=''
    )
    actualresult = requests.post(f'{host}:{port.eAccess}/command2', json=payload).json()

    response.error['result'] = [
        {
            "code": "DR-3/3",
            "description": "Attribute value mismatch with one of enum expected values. "
                           "Expected values: 'award, procuringEntity',"
                           " actual value: ''.",
            "details": [{"name": "locationOfPersones"}]
        }
    ]

    assert actualresult == response.error


@pytestrail.case('C17112')
def test_checkPersonesStructure_with_bussinessFunction_document_empty_array(host, port,
                                                                            payload_checkPersonesStructure,
                                                                            data_person, data_document, response):
    person = data_person
    person['businessFunctions'][0]['documents'] = {}
    payload = payload_checkPersonesStructure(
        person,
        locationOfPersones='award'
    )
    actualresult = requests.post(f'{host}:{port.eAccess}/command2', json=payload).json()
    response.error['result'] = [
        {
            "code": "RQ-02/3",
            "description": "Can not parse 'params'."

        }
    ]
    assert actualresult == response.error


@pytest.mark.parametrize("param,value,code,description",
                         [
                             pytest.param('cpid', '', "DR-5/3", "Data mismatch to pattern:"
                                                                " '^[a-z]{4}-[a-z0-9]{6}-[A-Z]{2}-[0-9]{13}$'."
                                                                " Actual value: ''.", id='cpid',
                                          marks=pytestrail.case('C13299')),
                             pytest.param('ocid', '', "DR-5/3", "Data mismatch to pattern:"
                                                                " '^[a-z]{4}-[a-z0-9]{6}-[A-Z]{2}-"
                                                                "[0-9]{13}-(AC|EI|EV|FS|NP|PN)-[0-9]{13}$'."
                                                                " Actual value: ''.", id='ocid',
                                          marks=pytestrail.case('C13300'))

                         ])
def test_checkPersonesStructure_if_data_of_attribute_mismatch_to_the_pattern(host, port,
                                                                             param, value, code, description,
                                                                             payload_checkPersonesStructure,
                                                                             data_person, response):
    payload = payload_checkPersonesStructure(locationOfPersones='award')
    payload['params'][param] = value
    actualresult = requests.post(f'{host}:{port.eAccess}/command2', json=payload).json()
    response.error['result'] = [
        {
            "code": code,
            "description": description,
            "details": [{"name": param}]
        }
    ]

    assert actualresult == response.error
