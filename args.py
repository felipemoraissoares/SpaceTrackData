import os
from datetime import datetime

# a diferent query could be generate in https://www.space-track.org/#/queryBuilder
# just put the credentials to accces https://www.space-track.org in ### fields site_cred

args = {
    'url_login': "https://www.space-track.org/ajaxauth/login",
    'site_cred': {'identity': "###", 'password': "###"},
    'query': "https://www.space-track.org/basicspacedata/query/class/tle_latest/DECAYED/NULL/ORDINAL/1/orderby/NORAD_CAT_ID%20asc/",
    'output_csv': os.path.join(os.path.dirname(os.path.realpath(__file__)) + "/csv_files/" + datetime.now().strftime("%Y%m%d-%H%M%S") + ".csv")
}
