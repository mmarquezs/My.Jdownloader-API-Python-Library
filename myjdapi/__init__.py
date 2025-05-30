from .myjdapi import Myjdapi
from .exception import (
    MYJDException,
    MYJDConnectionException,
    MYJDDeviceNotFoundException,
    MYJDDecodeException,
    MYJDApiException,
    MYJDApiCommandNotFoundException,
    MYJDApiInterfaceNotFoundException,
    MYJDAuthFailedException,
    MYJDBadParametersException,
    MYJDBadRequestException,
    MYJDChallengeFailedException,
    MYJDEmailForbiddenException,
    MYJDEmailInvalidException,
    MYJDErrorEmailNotConfirmedException,
    MYJDFailedException,
    MYJDFileNotFoundException,
    MYJDInternalServerErrorException,
    MYJDMaintenanceException,
    MYJDMethodForbiddenException,
    MYJDOfflineException,
    MYJDOutdatedException,
    MYJDOverloadException,
    MYJDSessionException,
    MYJDStorageAlreadyExistsException,
    MYJDStorageInvalidKeyException,
    MYJDStorageInvalidStorageIdException,
    MYJDStorageKeyNotFoundException,
    MYJDStorageLimitReachedException,
    MYJDStorageNotFoundException,
    MYJDTokenInvalidException,
    MYJDTooManyRequestsException,
    MYJDUnknownException,
)

__version__ = "1.1.10"
