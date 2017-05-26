# this repo will import all db related params from this file.

# google Machine
# ip = "104.199.157.84"
import os

# Digital ocean
ip = "postgres-master.hawker.news"
imart_ip = "139.59.64.208"
us_ip = "138.68.251.148"
db_name = "crawler"
login = "postgres"
password = "@hawkerIndia"
raw_abbrs = "raw_abbrs"
tender_table = "tenders_raw"
tender_int_table = "tenders_int_raw"
tender_test = "tenders_test"
tender_user_table = "tender_user_db"
tender_log_table = "tender_metadata_db"
location_table = "locations"
location_map = "locations_map"
tender_keywords = "tender_keywords"
tender_config = "tender_sites_config"
tender_doctext_table = "document_text"
tender_no_end_date_table = "tenders_no_end_date"
tender_no_emd_value_table = "tenders_no_emd_value"
tender_leads = "processed_leads"
temp_seed_urls = "temp_seed_urls"
tender_machines = "tender_machines"
tender_seed_urls = "tender_seed_urls"
tender_annex = "tender_annex"
tender_leads_table = "tender_leads_raw"
tender_leads_processed = "tender_leads_processed"
tender_leads_processed_new = "tender_leads_processed_new"
email_events = "email_events"
tender_eproc_captcha = "tender_eproc_captcha"
lat_long = "lat_long"
test_lat_long = "test_lat_long"
tender_results_processed = "tender_results_processed"

none_list = ["None", None, "none", "null", "", [], {}]

ZONE_INDIA = 'india'
ZONE_US = 'united states'
ZONE_IMART = 'imart'


def get_ip(zone):
    if zone == ZONE_INDIA:
        return ip
    if zone == ZONE_US:
        return us_ip
    if zone == ZONE_IMART:
        return imart_ip


def connect_db(flag=False, zone=ZONE_INDIA):
    # Connects to database of that zone. Use get_zone method if you don't
    # know which zone the crawler is in.
    from pg_python import pg_python
    mode = os.environ.get("CRAWL_ENV", "main")
    server_ip = get_ip(zone)
    if mode == "test":
        pg_python.pg_server("crawler", "postgres", "@hawkerIndia", ip, flag)
    else:
        pg_python.pg_server("crawler", "postgres", "@hawkerIndia", ip, flag)


def get_zone():
    # zone of the crawler. code must use this method to determine which zone
    # the current crawler is in.
    zone = os.environ.get("HAWKER_ZONE", ZONE_INDIA)
    return zone

#
# def connect_db_jd(flag=False):
#     from pg_python import pg_python
#     pg_python.pg_server("justdial", "postgres", "@hawkerjd", jd_ip, flag)
