class SmartBudgetError(Exception):
    """
    Custom exception type for the SmartBudget project.

    This class extends Python's built-in Exception and provides:
        - A standardized project-specific error prefix ("[SmartBudget]")
        - Optional contextual information to help identify the origin
          or cause of the error (e.g., function name, invalid value)

    Attributes
    ----------
    message : str
        The formatted error message with a SmartBudget prefix.
    context : any, optional
        Additional context about where/how the error occurred.
    """



    def __init__(self, message: str, context=None):
        """
        Initialize a SmartBudgetError.

        Parameters
        ----------
        message : str
            The human-readable error message.
        context : any, optional
            Extra debugging information (e.g., filename, failing value).
        """
        super().__init__(message)
        self.message = f"[SmartBudget] {message}"   # 项目特色标签
        self.context = context

    def __str__(self):
        """
        String representation of the exception.

        Returns a full message, including context if provided.
        """
        if self.context is not None:
            return f"{self.message} | Context: {self.context}"
        return self.message
