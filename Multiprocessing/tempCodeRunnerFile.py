    url = "https://picsum.photos/2000/3000"
    pros = []
    for i in range(50):
    # downloadFile(url, i)
    p = multiprocessing.Process(target=downloadFile, args=[url, i])
    p.start()
    pros.append(p)

    for p in pros:
    p.join()