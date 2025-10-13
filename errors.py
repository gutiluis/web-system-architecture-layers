#!/bin/env python


class ValidationError(Exception):
    """Raised when input data is invalid."""
    pass

class DatabaseError(Exception):
    """Raised when a database operation fails."""
    pass

