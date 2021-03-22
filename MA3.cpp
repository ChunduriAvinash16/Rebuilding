#include <iostream>

int main()
{
    long long int n;
    std::cin >> n;
    while (n--)
    {
        long long c;
        std::cin >> c;
        int d = 0, x = 1;
        while (1)
        {
            if (x > c)
                break;
            else
                x <<= 1;
            d++;
        }
        int m1 = 1 * (1 ^ c);
        for (int i = 2; i < x; i++)
        {
            if (i * (i ^ c) > m1)
                m1 = i * (i ^ c);
        }
        std::cout << m1 << std::endl;
    }
}