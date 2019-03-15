class Solution:
    def countBits(self, num: int) -> List[int]:
        next_t = 1
        bit_counts = [0] * (num + 1)

        for n in range(1, num + 1):
            if n == next_t:
                bit_counts[n] = 1
                next_t *= 2
            else:
                bit_counts[n] = bit_counts[int(next_t / 2)] + bit_counts[int(n - next_t / 2)]

        return bit_counts
