from django.test.utils import setup_test_environment
from django.conf import settings

from django_nose.runner import NoseTestSuiteRunner

class AutoTestSuiteRunner(NoseTestSuiteRunner):
    def setup_test_environment(self, **kwargs):
        setup_test_environment()
        settings.DEBUG = False
