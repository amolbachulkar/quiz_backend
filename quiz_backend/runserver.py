# Put this at <yourapp>/management/commands/runserver.py.

# Override the value of the constant coded into django...
import django.core.management.commands.runserver as runserver
runserver.DEFAULT_PORT="8080"

# ...and then just import its standard Command class.
# Then manage.py runserver behaves normally in all other regards.
from django.core.management.commands.runserver import Command