import re


def verify_password(password):
    errorsList = []
    if len(password) < 6:
        errorsList.append('Deve possuir no mínimo 6 caracteres.')
    if not any(x.isdigit() for x in password):
        errorsList.append('Deve conter no mínimo 1 número.')
    if not any(x.islower() for x in password):
        errorsList.append('Deve conter no mínimo 1 letra minúscula.')
    if not any(x.isupper() for x in password):
        errorsList.append('Deve conter no mínimo 1 letra maiúscula.')
    if not bool(re.search('[!@#$%^&*()-+]+', password)):
        errorsList.append('Deve conter no mínimo 1 caractere especial.')

    return errorsList


pwd = 'jaci'
print(verify_password(pwd))
