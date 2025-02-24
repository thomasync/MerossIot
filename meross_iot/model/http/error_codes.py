from enum import Enum


class ErrorCodes(Enum):
    """
    Status codes returned by the Meross HTTP APIs
    """

    CODE_NO_ERROR = 0
    """Not an error"""

    CODE_MISSING_PASSWORD = 1001
    """Wrong or missing password"""

    CODE_UNEXISTING_ACCOUNT = 1002
    """Account does not exist"""

    CODE_DISABLED_OR_DELETED_ACCOUNT = 1003
    """This account has been disabled or deleted"""

    CODE_WRONG_CREDENTIALS = 1004
    """Wrong email or password"""

    CODE_INVALID_EMAIL = 1005
    """Invalid email address"""

    CODE_BAD_PASSWORD_FORMAT = 1006
    """Bad password format"""

    CODE_WRONG_EMAIL = 1008
    """This email is not registered"""

    CODE_TOKEN_INVALID = 1019
    """Token expired"""

    CODE_UNKNOWN_FAILURE_1021 = 1021
    """Unknown error"""

    CODE_TOKEN_ERROR = 1022
    """Token error"""

    CODE_UNKNOWN_FAILURE_1023 = 1023
    """Unknown error"""

    CODE_UNKNOWN_FAILURE_1024 = 1024
    """Unknown error"""

    CODE_UNKNOWN_FAILURE_1025 = 1025
    """Unknown error"""

    CODE_UNKNOWN_FAILURE_1026 = 1026
    """Unknown error"""

    CODE_UNKNOWN_FAILURE_1027 = 1027
    """Unknown error"""

    CODE_UNKNOWN_FAILURE_1028 = 1028
    """Unknown error"""

    CODE_REDIRECT_REGION = 1030
    """Wrong login region"""

    CODE_TOKEN_EXPIRED = 1200
    """Token has expired"""

    CODE_UNKNOWN_FAILURE_1201 = 1201
    """Unknown error"""

    CODE_UNKNOWN_FAILURE_1202 = 1202
    """Unknown error"""

    CODE_UNKNOWN_FAILURE_1203 = 1203
    """Unknown error"""

    CODE_UNKNOWN_FAILURE_1204 = 1204
    """Unknown error"""

    CODE_UNKNOWN_FAILURE_1210 = 1210
    """Unknown error"""

    CODE_UNKNOWN_FAILURE_1211 = 1211
    """Unknown error"""

    CODE_UNKNOWN_FAILURE_1212 = 1212
    """Unknown error"""

    CODE_UNKNOWN_FAILURE_1213 = 1213
    """Unknown error"""

    CODE_UNKNOWN_FAILURE_1214 = 1214
    """Unknown error"""

    CODE_UNKNOWN_FAILURE_1215 = 1215
    """Unknown error"""

    CODE_UNKNOWN_FAILURE_1226 = 1226
    """Unknown error"""

    CODE_UNKNOWN_FAILURE_1227 = 1227
    """Unknown error"""

    CODE_UNKNOWN_FAILURE_1228 = 1228
    """Unknown error"""

    CODE_UNKNOWN_FAILURE_1229 = 1229
    """Unknown error"""

    CODE_UNKNOWN_FAILURE_1230 = 1230
    """Unknown error"""

    CODE_UNKNOWN_FAILURE_1231 = 1231
    """Unknown error"""

    CODE_UNKNOWN_FAILURE_1232 = 1232
    """Unknown error"""

    CODE_UNKNOWN_FAILURE_1233 = 1233
    """Unknown error"""

    CODE_MAX_CONTROL_BOARDS_REACHED = 1255
    """The number of remote control boards exceeded the limit"""

    CODE_TOO_MANY_TOKENS = 1301
    """Too many tokens have been issued"""

    CODE_UNKNOWN_FAILURE_1400 = 1400
    """Unknown error"""

    CODE_UNKNOWN_FAILURE_1401 = 1401
    """Unknown error"""

    CODE_UNKNOWN_FAILURE_1402 = 1402
    """Unknown error"""

    CODE_UNKNOWN_FAILURE_1403 = 1403
    """Unknown error"""

    CODE_UNKNOWN_FAILURE_1500 = 1500
    """Unknown error"""

    CODE_UNKNOWN_FAILURE_1501 = 1501
    """Unknown error"""

    CODE_UNKNOWN_FAILURE_1502 = 1502
    """Unknown error"""

    CODE_UNKNOWN_FAILURE_1503 = 1503
    """Unknown error"""

    CODE_UNKNOWN_FAILURE_1504 = 1504
    """Unknown error"""

    CODE_UNKNOWN_FAILURE_1601 = 1601
    """Unknown error"""

    CODE_UNKNOWN_FAILURE_1602 = 1602
    """Unknown error"""

    CODE_UNKNOWN_FAILURE_1603 = 1603
    """Unknown error"""

    CODE_UNKNOWN_FAILURE_1604 = 1604
    """Unknown error"""

    CODE_UNKNOWN_FAILURE_1605 = 1605
    """Unknown error"""

    CODE_UNKNOWN_FAILURE_1700 = 1700
    """Unknown error"""

    CODE_UNSUPPORTED_TIMEZONE = 500
    """The selected timezone is not supported"""

    CODE_GENERIC_ERROR = 5000
    """Unknown or generic error"""

    CODE_UNKNOWN_FAILURE_5001 = 5001
    """Unknown or generic error"""

    CODE_UNKNOWN_FAILURE_5002 = 5002
    """Unknown or generic error"""

    CODE_UNKNOWN_FAILURE_5003 = 5003
    """Unknown or generic error"""

    CODE_UNKNOWN_FAILURE_5004 = 5004
    """Unknown or generic error"""

    CODE_IR_DEVICE_BUSY = 5020
    """Infrared Remote device is busy"""

    CODE_IR_RECORD_TIMEOUT = 5021
    """Infrared record timeout"""

    CODE_IR_RECORD_INVALID = 5022
    """Infrared record invalid"""
