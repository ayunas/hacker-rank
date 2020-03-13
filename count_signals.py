#given an array of signals (Hz), determine the signals that come through after applying the filters.  the filters are an array of arrays.
#calc combined filter range. using intersection of all filters.
#if a signal is within the intersected filter range, increment the filtered signal count
#return the filtered signal count
#lower bound = highest of the 1st elements.  
#upper bound = lowest of the 2nd elements.




def countSignals(signals, filters):
    # print(signals)
    lowers = [l for l,u in filters]
    uppers = [u for l,u in filters]
    super_filter = [max(lowers),min(uppers)]
    # print(super_filter)
    filtered = list(filter(lambda s: (s >= super_filter[0] and s <= super_filter[1]),signals))
    # print(filtered)
    return len(filtered)

signals = countSignals([2,3,4,5,6,7,11,14,24,12,14],[[10,20],[5,15],[5,30]])
print(signals)
