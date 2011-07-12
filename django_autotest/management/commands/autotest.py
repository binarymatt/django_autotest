import unittest
from django.conf import settings
from django.core.management.commands.test import Command as TestCommand

from Growl import GrowlNotifier

class Command(TestCommand):
    def handle(self, *args, **options):
        gn = GrowlNotifier(applicationName='django_test_runner', notifications=["PASS","FAIL"])
        gn.register()
        def test_stuff():
            print "Running Tests..."
            from django.test.utils import get_runner
            verbosity = int(options.get('verbosity', 1))
            interactive = options.get('interactive', True)
            failfast = options.get('failfast', False)
            TestRunner = get_runner(settings)
            test_runner = TestRunner(verbosity=verbosity, interactive=interactive, failfast=failfast)
            failures = test_runner.run_tests(args)
            if failures:
                #sys.exit(bool(failures))
                gn.notify("FAIL", "Tests Failed","Check the console to see failing tests")
            else:
                gn.notify("PASS", "Tests Passed","Way to go, you rock!")


        from django.utils import autoreload
        autoreload.main(test_stuff)


