import datetime
import ntplib

client = ntplib.NTPClient()
response = client.request('ntp.api.bz')
print datetime.datetime.fromtimestamp(response.tx_time)

