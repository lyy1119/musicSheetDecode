#include <stdio.h>
#include <math.h>

int main()
{
    double bi = pow(2 , 1.0/12.0);
    double freq = 523;

    printf("%lf" , bi);

    // for (int i = 0; i < 24; i++)
    // {
    //     printf("%.0lf " , freq);
    //     freq = freq * bi;
    // }
    
    return 0;
}