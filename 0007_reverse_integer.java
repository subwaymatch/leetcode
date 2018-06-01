class Solution {
public:
    int reverse(int x) {
        int prev_answer = 0, answer = 0, remainder = 0;

        while(x != 0) {
            remainder = x % 10;
            x /= 10;

            prev_answer = answer;
            answer = (answer * 10) + remainder;

            if ((answer > INT_MAX / 100) || (answer < INT_MIN / 100))
            {
                if ((answer / 100) != (prev_answer / 10)) { return 0; }
            }
        }

        return answer;
    }
};
