import hashlib
import hmac
import base64

from .utils import ( api, is_python3 )
from .application import ApplicationManager
from .product import ProductManager
from .policy import PolicyManager
from .data import DataManager
from .team import TeamManager

class AcrosureClient:
    """
    Represents an Acrosure API client

    ...

    Attributes
    ----------
    application : class
        A class for application api
    product : class
        A class for product api
    policy : class
        A class for policy api
    data : class
        A class for data api
    team : class
        A class for team api
    token : str
        An access token

    Methods
    -------
    call_api( token = token, path = path, data = data, api_url = api_url )
        Call Acrosure API with corresponding url & current API key.
    """

    def __init__( self, token, api_url = None ):
        """
        Parameters
        ----------
        token : str
            An access token
        api_url : str
            An API end point.
        """
        self.token = token
        self.api_url = api_url
        call_api = self.call_api
        self.application = ApplicationManager(call_api = call_api)
        self.product = ProductManager(call_api = call_api)
        self.policy = PolicyManager(call_api = call_api)
        self.data = DataManager(call_api = call_api)
        self.team = TeamManager(call_api = call_api)
    
    def call_api( self, path, data = None ):
        """
        Call Acrosure API with corresponding url & current API key.

        Parameters
        ----------
        path : str
            An API path.
        data : dict
            A data object which is specified by Acrosure.
        api_url : str
            An API end point.
        """

        return api( path, data, self.token, self.api_url )

    def verify_signature( self, signature, data ):
        """
        Verify signature in webhook event.

        Parameters
        ----------
        signature : str
            A signature received from webhook.
        data : str
            A string of raw data.

        Returns
        ----------
        boolean
            Whether the signature is valid or not.
        """
        if is_python3():
            message = bytes(data, "utf-8")
            secret = bytes(self.token, "utf-8")
        else:
            message = bytes(data.decode('utf-8').encode('utf-8'))
            secret = bytes(self.token.decode('utf-8').encode('utf-8'))
        hash = hmac.new(secret, message, hashlib.sha256)

        expected = hash.hexdigest()

        return signature == expected
