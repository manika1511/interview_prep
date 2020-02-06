"""
The read4 API is already defined for you.

    @param buf, a list of characters
    @return an integer
    def read4(buf):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf = [' '] * 4 # Create buffer with enough space to store characters
read4(buf) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""


class Solution(object):
    def __init__(self):
        self.buffer = []
        self.pointer = 0

    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """

        eof = False
        while not eof and len(self.buffer) - self.pointer < n:
            tmp_buf = [None] * 4
            chars_read = read4(tmp_buf)
            self.buffer.extend(tmp_buf[0:chars_read])

            if chars_read < 4:
                eof = True

        count = min(len(self.buffer) - self.pointer, n)
        j = 0
        for i in self.buffer[self.pointer:self.pointer + count]:
            buf[j] = i
            j = j + 1
        self.pointer = self.pointer + count
        return count