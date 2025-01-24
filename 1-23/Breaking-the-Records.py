def breakingRecords(scores):
    current_min = current_max = scores[0]
    min_breaks = max_breaks = 0
    
    for score in scores[1:]:
        if score > current_max:
            max_breaks += 1
            current_max = score
        if score < current_min:
            min_breaks += 1
            current_min = score
            
    return [max_breaks, min_breaks]