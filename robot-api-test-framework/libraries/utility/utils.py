from datetime import datetime


def match_count_and_data(response):
    """
    Match the count and data.
    """
    count = response.get('count')
    if count is not None and count != len(response["data"]):
        return False
    return True


def verify_data_in_date_range(response, start_date, end_date):
    """
    Verify data in date range.

    """
    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    start_date= start_date.strftime("%Y-%b-%d")
    end_date = datetime.strptime(end_date, "%Y-%m-%d")
    end_date= end_date.strftime("%Y-%b-%d")
    for data in response["data"]:
        entry_date = datetime.strptime(data[3], "%Y-%b-%d %H:%M")
        entry_date = entry_date.strftime("%Y-%b-%d")
        if start_date > entry_date or entry_date > end_date:
            return False
    return True


    