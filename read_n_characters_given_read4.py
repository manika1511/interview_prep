class Solution(object):
    def read(self, buf, n):
        write_pointer = 0
        temp_buf = [None] * 4
        eof = False

        while not eof and write_pointer < n:
            chars_read = read4(temp_buf)
            if chars_read < 4:
                eof = True

            for i in range(chars_read):
                buf[write_pointer] = temp_buf[i]
                write_pointer = write_pointer + 1
                if write_pointer == n:
                    break
        return write_pointer
