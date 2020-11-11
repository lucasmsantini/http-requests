import requests
import random


def altera_politica(policyName='POLICE_NAME',
                    policyType='0',
                    behaviorType='1',
                    enabled='True',
                    notify='True',
                    customNotificationMessage='Impressão liberada',
                    useDefaultNotificationMessage='True',
                    filters='[]',
                    applyToAll='true'):
    POLICE_NAME = 'PythonPolitica' + str(random.randint(0, 99999999))
    print('Nome da politica criada: ', POLICE_NAME)
    police_data = {
        "policyName": POLICE_NAME,
        "policyType": policyType,

        "behaviorType": behaviorType,
        "enabled": enabled,
        "notify": notify,
        "customNotificationMessage": customNotificationMessage,
        "useDefaultNotificationMessage": useDefaultNotificationMessage,
        "filters": filters,
        "applyToAll": applyToAll
    }

    requests.post(url='https://360.nddprint.com/api/policies', data=police_data)
