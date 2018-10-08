from .utils import decorate

class ApplicationManager:
    """
    Represents an ApplicationManager. (You most likely shouldn't be accessing this directly, use {@link AcrosureClient#application} instead.)
    """

    def __init__( self, id, call_api ):
        """
        Parameters
        ----------
        id : string
            Current managing application id.
        call_api : function
            A function which call Acrosure API.
        """
        self.id = id
        self.call_api = call_api

    def set_id( self, id ):
        """
        Set current application id.

        Parameters
        ----------
        id : str
            An application id.
        """
        self.id = id

    def get( self, id = None ):
        """
        Get an application with specify id or with current id.

        Parameters
        ----------
        id : str, optional
            An application id.

        Returns
        -------
        dict
            An application.
        """
        try:
            if id:
                self.id = id
            # resp = self.call_api("/applications/get", {
            resp = self.call_api("/success", {
                "application_id": self.id
            })
            if resp.get("data", {}).get("status"):
                self.status = resp.get("data").get("status")
            return resp
        except Exception as err:
            raise err

    def list( self, query = {} ):
        """
        Get applications list with or without query.

        Parameters
        ----------
        query : dict, optional
            Query object (See Acrosure API document for more detail).

        Returns
        -------
        list
            Applications.
        """
        try:
            resp = self.call_api("/applications/list", query)
            return resp
        except Exception as err:
            raise err

    def create(
        self,
        product_id,
        basic_data = None,
        package_options = None,
        additional_data = None,
        attachments = None,
        package_code = None,
        ref1 = None,
        ref2 = None,
        ref3 = None,
        group_policy_id = None,
        step = None
    ):
        """
        Create an application and change {@link ApplicationManager#id} if possible.

        Parameters
        ----------
        product_id : str
            A product id.
        basic_data : dict, optional
            Application's basic_data.
        package_options : dict, optional
            Application's package_options.
        additional_data : dict, optional
            Application's additional_data.
        attachments : list, optional
            A list of files.
        package_code : str, optional
            A string of package_code.
        ref1 : str, optional
            A string of reference #1.
        ref2 : str, optional
            A string of reference #2.
        ref3 : str, optional
            A string of reference #3.
        group_policy_id : str, optional
            A string of group policy id.
        step : int, optional
            A number of current step.

        Returns
        -------
        dict
            Created application.
        """
        try:
            body = decorate({
                "product_id": product_id,
                "basic_data": basic_data,
                "package_options": package_options,
                "additional_data": additional_data ,
                "attachments": attachments,
                "package_code": package_code,
                "ref1": ref1,
                "ref2": ref2,
                "ref3": ref3,
                "group_policy_id": group_policy_id,
                "step": step
            })
            resp = self.call_api("/applications/create", body)
            if not resp:
                raise("no response")
            if resp.get("data", {}).get("id"):
                self.id = resp.get("data").get("id")
            if resp.get("data", {}).get("status"):
                self.status = resp.get("data").get("status")
        except Exception as err:
            raise err

    def update(
        self,
        application_id = None,
        basic_data = None,
        package_options = None,
        additional_data = None,
        attachments = None,
        package_code = None,
        ref1 = None,
        ref2 = None,
        ref3 = None,
        group_policy_id = None,
        step = None
    ):
        """
        Update current application or with specified id.

        Parameters
        ----------
        application_id : str, optional
            An application id.
        basic_data : dict, optional
            Application's basic_data.
        package_options : dict, optional
            Application's package_options.
        additional_data : dict, optional
            Application's additional_data.
        attachments : list, optional
            A list of files.
        package_code : str, optional
            A string of package_code.
        ref1 : str, optional
            A string of reference #1.
        ref2 : str, optional
            A string of reference #2.
        ref3 : str, optional
            A string of reference #3.
        group_policy_id : str, optional
            A string of group policy id.
        step : int, optional
            A number of current step.

        Returns
        -------
        dict
            Updated application.
        """
        try:
            if application_id:
                self.id = application_id
            body = decorate({
                "application_id": self.id,
                "basic_data": basic_data,
                "package_options": package_options,
                "additional_data": additional_data ,
                "attachments": attachments,
                "package_code": package_code,
                "ref1": ref1,
                "ref2": ref2,
                "ref3": ref3,
                "group_policy_id": group_policy_id,
                "step": step
            })
            resp = self.call_api("/applications/update", body)
            if resp.get("data", {}).get("status"):
                self.status = resp.get("data").get("status")
            return resp
        except Exception as err:
            raise err
    
    def get_packages( self ):
        """
        Get available packages for current application.

        Returns
        -------
        list
            Available packaged.
        """
        try:
            resp = self.call_api("/applications/get-packages", {
                "application_id": self.id
            })
            return resp
        except Exception as err:
            raise err

    def get_package( self ):
        """
        Get current application's package.

        Returns
        -------
        list
            Current application's package.
        """
        try:
            resp = self.call_api("/applications/get-package", {
                "application_id": self.id
            })
            return resp
        except Exception as err:
            raise err

    def select_package( self, args ):
        """
        Select package for current application.

        Parameters
        ----------
        args : dict
            A dictionary consists of several properties.
            package_code : str
                A string of package_code.

        Returns
        -------
        dict
            Updated application.
        """
        try:
            resp = self.call_api("/applications/select-package", {
                "application_id": self.id,
                "package_code": args.get("package_code")
            })
            return resp
        except Exception as err:
            raise err

    def submit( self ):
        """
        Submit current application.

        Returns
        -------
        dict
            Submitted application.
        """
        try:
            resp = self.call_api("/applications/submit", {
                "application_id": self.id
            })
            if resp.get("data", {}).get("status"):
                self.status = resp.get("data").get("status")
            return resp
        except Exception as err:
            raise err
    
    def confirm( self ):
        """
        Confirm current application.

        Returns
        -------
        dict
            Confirmed application.
        """
        try:
            resp = self.call_api("/applications/confirm", {
                "application_id": self.id
            })
            if resp.get("data", {}).get("status"):
                self.status = resp.get("data").get("status")
            return resp
        except Exception as err:
            raise err
    
    def get_2c2p_hash( self, args ):
        """
        Get 2C2P hash.

        Parameters
        ----------
        args : dict
            frontend_url : str
                A string of frontend_url.

        Returns
        -------
        str
            2C2P hash string.
        """
        try:
            resp = self.call_api("/payments/2c2p/get-hash", {
                "application_id": self.id,
                "frontend_url": args.get("frontend_url")
            })
            return resp
        except Exception as err:
            raise err
