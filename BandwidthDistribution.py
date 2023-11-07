# Total bandwidth is total_bandwidth units and there are n API endpoints. The i^th endpoint needs a bandwidth of bandwidth[i] to be functional, and the expected number of requests for the endpoint is request[i]. Given total_bandwidth, bandwidth, and request, find the maximum total number of requests that can be served by optimally allocating bandwidth to different endpoints.


# total_bandwidth = 500 bandwidth = [200, 90,350,50,100] request = [270, 142,450,124,189] 
# Output: 763
 
def getMaxRequests(bandwidth, request, total_bandwidth):
    n = len(bandwidth)
    
    # Create a list of tuples (bandwidth, request, index) and sort it by request in decreasing order
    endpoints = [(bandwidth[i], request[i], i) for i in range(n)]
    endpoints.sort(key=lambda x: x[1], reverse=True)
    
    total_requests_served = 0

    for b, r, i in endpoints:
        if b <= total_bandwidth:
            total_requests_served += r
            total_bandwidth -= b

    return total_requests_served


total_bandwidth = 200
bandwidth = [200, 80, 100] 
request = [50, 60, 90]
output = getMaxRequests(bandwidth, request, total_bandwidth)
print(output)  # Output: 763


  