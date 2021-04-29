class Constants:

    # Users
    ROLE_ADMIN = 'ROLE_ADMIN'
    ROLE_USER = 'ROLE_USER'
    ROLE_TEACHER = 'ROLE_TEACHER'

    ROLE_OPTIONS = [
        (ROLE_ADMIN, 'Admin role'),
        (ROLE_USER, 'User role'),
        (ROLE_TEACHER, 'Teacher role'),
    ]

    # Tokens
    TYPE_ACCOUNT_CONFIRMATION = 'ACCOUNT_CONFIRMATION'
    TYPE_RESET_PASSWORD = 'RESET_PASSWORD'

    TOKEN_TYPES = [
        (TYPE_ACCOUNT_CONFIRMATION, 'Account confirmation'),
        (TYPE_RESET_PASSWORD, 'Reset password')
    ]

    # Notifications
    TYPE_EMAIL = 'EMAIL'
    TYPE_PRIVATE = 'PRIVATE'
    TYPE_SMS = 'SMS'
    TYPE_WHATSAPP = 'WHATSAPP'

    TYPE_NOTIFICATIONS = [
        (TYPE_EMAIL, 'Email Type'),
        (TYPE_SMS, 'SMS Type'),
        (TYPE_WHATSAPP, 'Whatsapp Type'),
        (TYPE_PRIVATE, 'Private Type')
    ]

    STATUS_PENDING = 'PENDING'
    STATUS_SEND = 'SEND'

    STATUS_NOTIFICATIONS = [
        (STATUS_PENDING, 'Pending'),
        (STATUS_SEND, 'Send'),
    ]

    # Genres
    MALE = 'MALE'
    FEMALE = 'FEMALE'

    GENRES = [
        (MALE, 'Male Type'),
        (FEMALE, 'Female Type')
    ]
