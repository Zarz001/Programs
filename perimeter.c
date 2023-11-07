#include "perimeter.h"
#include <stdio.h>
int F3[100];
ull perimeter(int n) {
  int p = 0;
  int sum = 0;
  scanf("%d", &n); 
  if (n <0)
  {
    return 1;
  }
  else if (n <1)
  {
    return 4;
  }
  F3[0] = 1;
  F3[1] = 1;
  for (int i = 2; i <= n+1; i++) {
    F3[i] = F3[i - 1] + F3[i - 2];
  }
  for (int c = 0; c < n+1; c++) {
    sum = sum + F3[c];
  }
  p = 4 * sum;
  return p;
}





