from dataclasses import dataclass

import pytest


@pytest.fixture(scope='function')
def responses(prepared_request_id):
    @dataclass()
    class Responses:
        version = '0.0.1'
        ok = {'id': f'{prepared_request_id}', 'data': {}, 'version': version}
        errors = {'id': f'{prepared_request_id}', 'errors': [], 'version': version}

    return Responses


@pytest.fixture(scope='function')
def payload_template(prepared_request_id):
    return {
        "id": "",
        "command": "",
        "context": {},
        "data": {},
        "version": "0.0.1"
    }


@pytest.fixture(scope='function')
def prepared_payload(payload_template, prepared_request_id, prepared_operation_id):
    def with_values(command, cpid=None, stage="EV", operationid=prepared_operation_id, id=None, token=None,
                    owner='445f6851-c908-407d-9b45-14b92f3e964b'):
        payload_template['id'] = f"{prepared_request_id}"
        payload_template['command'] = command
        payload_template['context'] = {
            "operationId": f"{operationid}",
            "requestId": "7eb32550-2335-11ea-7a78-e9a0e1c3d51d",
            "cpid": cpid,
            "ocid": "ocds-t1s2t3-MD-1576850865434-EV-1576850873109",
            "stage": stage,
            "prevStage": "EV",
            "processType": "startConsiderByAward",
            "operationType": "doAwardConsideration",
            "phase": "awarding",
            "owner": f"{owner}",
            "country": "MD",
            "language": "ro",
            "pmd": "TEST_OT",
            "token": f'{token}',
            "startDate": "2019-12-20T14:32:05Z",
            "id": f"{id}",
            "timeStamp": 1576852325413,
            "isAuction": False
        }
        return payload_template

    return with_values


@pytest.fixture(scope='function')
def prepared_payload_getAmendmentIds(prepared_request_id, prepared_cpid, prepared_ev_ocid):
    def with_values(version="2.0.0", id=f"{prepared_request_id}", action="getAmendmentIds",
                    relatesTo="tender", status="pending", type="cancellation", cpid=prepared_cpid,
                    ocid=prepared_ev_ocid, relatedItems=prepared_ev_ocid):
        return {
            "version": version,
            "id": id,
            "action": action,
            "params": {
                "status": status,
                "type": type,
                "relatesTo": relatesTo,
                "relatedItems": [relatedItems],
                "cpid": cpid,
                "ocid": ocid
            }
        }

    return with_values


@pytest.fixture(scope='function')
def prepared_payload_dataValidation(prepared_request_id, prepared_amendment_id, prepared_cpid, prepared_ev_ocid):
    def with_values(id=prepared_request_id):
        return {
            "version": "2.0.0",
            "id": f"{id}",
            "action": "dataValidation",
            "params": {
                "amendment": {
                    "rationale": "Some_string_1",
                    "description": "Some_string_2",
                    "documents": [
                        {
                            "documentType": "cancellationDetails",
                            "id": "835b8d03-80dc-4d1b-8b1c-fe2b1a23366c-1573211196021",
                            "title": "string",
                            "description": "string"
                        }
                    ],
                    "id": f"{prepared_amendment_id}"
                },
                "cpid": f"{prepared_cpid}",
                "ocid": f"{prepared_ev_ocid}",
                "operationType": "tenderCancellation"
            }
        }

    return with_values


@pytest.fixture(scope='function')
def prepared_payload_createAmendment(prepared_request_id, prepared_amendment_id, prepared_cpid, prepared_ev_ocid):
    return {
        "version": "2.0.0",
        "id": f"{prepared_request_id}",
        "action": "createAmendment",
        "params": {
            "amendment": {
                "rationale": "Some_string_1",
                "description": "Some_string_2",
                "documents": [{
                    "documentType": "cancellationDetails",
                    "id": "835b8d03-80dc-4d1b-8b1c-fe2b1a23366c-1573211196021",
                    "title": "amendments documents title",
                    "description": "amendments documents description"
                }],
                "id": f"{prepared_amendment_id}"
            },
            "relatedEntityId": f"{prepared_ev_ocid}",
            "operationType": "tenderCancellation",
            "startDate": "2020-02-28T16:14:54Z",
            "cpid": f"{prepared_cpid}",
            "ocid": f"{prepared_ev_ocid}",
            "owner": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
        }
    }


@pytest.fixture(scope='function')
def prepared_payload_getLotIds(prepared_request_id, prepared_cpid, prepared_ev_ocid):
    return {
        "version": "2.0.0",
        "id": f"{prepared_request_id}",
        "action": "getLotIds",
        "params": {
            "states": [
                {
                    "status": "active",
                    "statusDetails": "empty"
                }
            ],
            "cpid": f"{prepared_cpid}",
            "ocid": f"{prepared_ev_ocid}"
        }
    }