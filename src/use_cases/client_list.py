"""Module for the client list use case"""


def client_list_use_case(repo):
    """Client list use case

    Args:
        repo (_type_): Client respository

    Returns:
        List: List of clients
    """
    return repo.list()
