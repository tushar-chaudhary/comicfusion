import logging

# Create and configure logger
logging.basicConfig(filename="activity.log",
                    format='%(asctime)s:%(levelname)s:%(name)s %(message)s',
                    filemode='w')

# Creating an object
logger = logging.getLogger()

# Setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)
