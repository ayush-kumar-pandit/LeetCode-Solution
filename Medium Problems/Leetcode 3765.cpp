class Solution {
public:
    bool prime(int x) {
        int cnt = 0;
        for (int i = 1; i * i <= x; i++) {
            if (x % i == 0) {
                cnt++;
                if (x / i != i)
                    cnt++;
            }
        }
        return cnt == 2;
    }
    bool completePrime(int num) {
        if (num == 7 or num == 5 or num == 3 or num == 2)
            return true;

        int pow = 0;
        for (int temp = num; temp; temp /= 10) {
            pow++;
            if (prime(temp))
                continue;
            else
                return false;
        }

        int c = 1;
        while (pow--) {
            c *= 10;
        }

        for (int temp = num; temp; temp %= c) {
            if (prime(temp))
                 c /= 10;
            else
                return false;
        }
        return true;
    }
};
