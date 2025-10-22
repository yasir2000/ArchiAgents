"""
Custom Exceptions for TOGAF Framework
"""


class TOGAFException(Exception):
    """Base exception for TOGAF framework"""
    pass


class ValidationException(TOGAFException):
    """Exception raised for validation errors"""
    pass


class GovernanceException(TOGAFException):
    """Exception raised for governance violations"""
    pass


class ComplianceException(TOGAFException):
    """Exception raised for compliance violations"""
    pass


class ArchitectureException(TOGAFException):
    """Exception raised for architecture-related errors"""
    pass


class IntegrationException(TOGAFException):
    """Exception raised for integration errors"""
    pass


class SecurityException(TOGAFException):
    """Exception raised for security violations"""
    pass


class NORAComplianceException(ComplianceException):
    """Exception raised for NORA compliance violations"""
    pass
