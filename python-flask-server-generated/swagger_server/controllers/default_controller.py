import connexion
import six

from swagger_server.models.recipe import Recipe  # noqa: E501
from swagger_server import util


def getrecipe_get(username=None, recipe_id=None, recipe_like=None):  # noqa: E501
    """Gets new recipe for user with last swipe

    Update an existing pet by Id # noqa: E501

    :param username: name or uuid of user
    :type username: str
    :param recipe_id: name or uuid of recipe
    :type recipe_id: str
    :param recipe_like: name or uuid of recipe
    :type recipe_like: str

    :rtype: Recipe
    """
    recipe = Recipe("Pasta arrabiatta", ["spaghetti", "basil", "tomatosauce", "onion"])
    return recipe
