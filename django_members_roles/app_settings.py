from django.conf import settings

DJANGO_MEMBERS_ROLES_CONFIRMATION_REQUIRED = getattr(
    settings, 'DJANGO_MEMBERS_ROLES_CONFIRMATION_REQUIRED', True)

DJANGO_MEMBERS_ROLES_TEST_CASE_MODEL_NAME = "user"
DJANGO_MEMBERS_ROLES_TEST_CAES_APP_LABEL = "auth"
DJANGO_MEMBERS_ROLES_QUERY_PARAM_CONTENT_TYPE_ID = getattr(
    settings, 'DJANGO_MEMBERS_ROLES_QUERY_PARAM_CONTENT_TYPE_ID', 'content_type_id')
DJANGO_MEMBERS_ROLES_QUERY_PARAM_OBJECT_ID = getattr(
    settings, 'DJANGO_MEMBERS_ROLES_QUERY_PARAM_OBJECT_ID', 'object_id')

