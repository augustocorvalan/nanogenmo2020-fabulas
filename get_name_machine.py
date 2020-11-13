# import shortuuid
import datetime

def get_uuid_filename(identifier="sample", extension=""):
  uuid = current_time = str(datetime.datetime.now())
  name = f'{identifier}-{uuid}'
  if extension:
    name = f'{name}.{extension}'
  return name
