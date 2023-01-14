class Runner:
    def __getattr__(self, attr):
        from django.core.management import call_command
        return lambda: call_command(attr)

import sys
sys.modules[__name__] = Runner()