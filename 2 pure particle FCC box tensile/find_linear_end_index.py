def find_linear_end_index(slopes, window:int=15, allow_err:float=0.2):
    avg_slope = sum(slopes[1:1+window])/window
    for i in range(1,len(slopes-window)):
        window_avg_slope = sum(slopes[i:i+window])/window
        error = (avg_slope - window_avg_slope)/avg_slope
        if error < allow_err:
            avg_slope = sum(slopes[1:i+window])/(i+window)            
        else:
            return i, avg_slope