import logging
import colorlog


def get_script_logger(level: str = 'DEBUG') -> logging.Logger:
  logger_name = 'default'
  logger = logging.getLogger(logger_name)
  formatter = colorlog.ColoredFormatter(
      fmt='%(log_color)s%(levelname)s: %(asctime_log_color)s[%(asctime)s] %(pathname_log_color)s%(pathname)s:%(lineno_log_color)s%(lineno)d %(funcName_log_color)s%(funcName)s %(message_log_color)s%(message)s',
      log_colors={
          'DEBUG': 'cyan',
          'INFO': 'green',
          'WARNING': 'yellow',
          'ERROR': 'red',
          'CRITICAL': 'red,bg_white',
      },
      datefmt='%Y-%m-%d %H:%M:%S',
      secondary_log_colors={
          'message': {
              'DEBUG': 'cyan',
              'INFO': 'green',
              'WARNING': 'bold_yellow',
              'ERROR': 'red',
              'CRITICAL': 'blue,bg_white',
          },
          'lineno': {
              'DEBUG': 'red',
              'INFO': 'red',
              'WARNING': 'red',
              'ERROR': 'red',
              'CRITICAL': 'red,bg_white',
          },
          'levelname': {
              'DEBUG': 'cyan',
              'INFO': 'green',
              'WARNING': 'yellow',
              'ERROR': 'red',
              'CRITICAL': 'red,bg_white',
          },
          'asctime': {
              'DEBUG': 'yellow',
              'INFO': 'yellow',
              'WARNING': 'yellow',
              'ERROR': 'yellow',
              'CRITICAL': 'yellow,bg_white',
          },
          'pathname': {
              'DEBUG': 'green',
              'INFO': 'green',
              'WARNING': 'green',
              'ERROR': 'red',
              'CRITICAL': 'green,bg_white',
          },
          'funcName': {
              'DEBUG': 'purple',
              'INFO': 'purple',
              'WARNING': 'purple',
              'ERROR': 'purple',
              'CRITICAL': 'purple,bg_white',
          },
      }

  )
  handler = logging.StreamHandler()
  handler.setFormatter(formatter)
  handler.name = logger_name

  for handler in logger.handlers:
    if handler.name == logger_name:
      return logger

  logger.addHandler(handler)
  logger.setLevel(level)
  return logger
