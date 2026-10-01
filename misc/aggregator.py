# ==== frame data composition ====

# === imports ===

from misc.converter import convert
from misc.checksum import checksum
from misc.data_handlers import chunker

"""
here is where we aggregate all the data to a frame and pass it to the next step

the format is simple;   - size in bits
1, the top right mark   - 4
2, the frame number     - 21
3, total frames         - 21
4, checksum             - 16
5, length               - 7              - for padding math
5, payload              - 768
6, bottom left mark     - 4

total                   - 841


the orientation marks, they are strings of 4 bits that are constant, no conversion needed, numbers are;

top = 0110
bottom = 1001

"""
def data_aggregator(data):
    top_flag = "0110"
    bottom_flag = "1001"
    frame_count = "0"

    frames = []
    
    data = chunker(data)    # this gives us the chunks and their chunk sizes in bytes

    # first is the total frame number
    total_frames = len(data[1])
    
    # next we prep the payload
    payload_list = data[1]

    for i in range(0, len(payload_list), 1):
        payload = payload_list[i]

        frame_count = i

        checksum_state_1 = checksum(payload)
        
        # just a precaution to ensure we don't break the frame
        if len(checksum_state_1) > 16:
            checksum_state_2 = checksum_state_1[16:]

        # next is the chunk length in bytes
        chunk_length = len(payload) // 8

        # mow we run converts before bundling everything together
        total_frames_count = convert([total_frames], width=21)
        frames_count = convert([frame_count], width=21)
        length = convert([chunk_length], width=7)

        # now we aggregate the data in that order, since its strings of data its just a "+" sign
        single_frame = top_flag + frames_count + total_frames_count + checksum_state_2 + length + payload + bottom_flag

        frames.append(single_frame)

    return frames
