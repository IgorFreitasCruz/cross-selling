"""Module for CNPJ formatter"""


def format_cnpj_to_digits(client: dict):
    """Custom CNPJ formatter
    Args:
        cnpj (str): CNPJ in format string

    Returns:
        str: CNPJ formatted containing no special catacters
    """
    cnpj = client['cnpj']
    cnpj_formated = cnpj.replace('.', '').replace('/', '').replace('-', '')
    return client.update({'cnpj': cnpj_formated})
    