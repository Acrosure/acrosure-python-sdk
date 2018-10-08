class DataManager:
    """
    Represents an DataManager. (You most likely shouldn't be accessing this directly, use {@link AcrosureClient#data} instead.)
    """

    def __init__( self, call_api ):
        """
        Parameters
        ----------
        call_api : function
            A function which call Acrosure API.
        """
        self.call_api = call_api
    
    def get( self, args = {} ):
        """
        Get data from a handler.

        Parameters
        ----------
        args : dict
            A dictionary consists of several properties.
            handler : str, optional
                A handler string.
            dependencies : list, optional
                An array of dependencies (if needed).

        Returns
        -------
        dict
            Available values for the combination of handler/dependencies.
        """

        try:
            resp = self.call_api("/data/get", args)
            return resp
        except Exception as err:
            raise err
