# this is where we place the data in a frame for streaming

# ==== imports ====

from misc.aggregator import data_aggregator

def frame_data(payload):
    frames = data_aggregator(payload)   # this returns a list of strings(the frames)
    rows = []
    row_count = 0
    row_length = 29

    for i in range(0, len(frames), 1):
        single_frame = frames[i]

        for s in range(0, len(single_frame), 29):
            row = single_frame[s:s+29]
            rows.append(row)
            row_count += 1

    return rows
