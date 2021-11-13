start_time = time.time()
Process("static/uploads/vbg.jpeg", "static/downloads/compressed_vbg.jpeg", 12)
print("execution time:  %s seconds" % (time.time() - start_time))
