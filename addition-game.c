#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main()
{
    int val1, val2, input;

    srand((int)time(NULL));

    while(1)
    {
        val1 = (rand()%19)+1; // 피연산자1: 1에서 9까지
        val2 = (rand()%19)+1; // 피연산자2: 1에서 9까지

        printf("%d + %d = ", val1, val2); scanf("%d", &input);
        if(val1+val2 == input)
            printf("   Correct!\n");
        else
            printf("   Correct Answer: %d\n", val1+val2);
    }

    return 0;
}
