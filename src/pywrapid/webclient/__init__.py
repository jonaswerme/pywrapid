# -*- coding: utf-8 -*-
# flake8: noqa
# pylint: skip-file

from .exceptions import (
    ClientAuthenticationError,
    ClientAuthorizationError,
    ClientConnectionError,
    ClientException,
    ClientHTTPError,
    ClientTimeout,
    ClientURLError,
    CredentialCertificateFileError,
)
from .web import (
    AuthorizationType,
    BasicAuthCredentials,
    WebClient,
    WebCredentials,
    X509Credentials,
)
