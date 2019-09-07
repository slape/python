import logging
import sys

#####################
# SETTING UP LOGGER #
#####################
# Gets the main logging object. `root` is the only one you usually need to know about
root = logging.getLogger()

# OPTIONAL — This lets you define exactly how you want your log output to look.
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# OPTIONAL but RECOMMENDED — Explicitly link logger's output to `stdout`
# You can forward data elsewhere, too, but this is obviously what you want locally
stdout_handler = logging.StreamHandler(sys.stdout)
# Ensure this handler uses the format above
stdout_handler.setFormatter(formatter)

# Only inform about messages of severity "INFO" or greater (which will be all of them, since INFO = 0)
root.setLevel(logging.INFO)

# Register the handler w/ the root logger
root.addHandler(stdout_handler)
