import speedtest

s = speedtest.Speedtest()
result_servers = s.get_servers(country_city='Germany:Berlin')
result_best = s.get_best_server()

result_download = s.download()
result_upload = s.upload()
results_ping = s.results.ping

_ = results_ping
