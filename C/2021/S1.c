#include <stdio.h>

double formula(double h1, double h2, double width) { return (width * (h1 + h2)) / 2; }

int main(int argc, char *argv[]) {
  int N;
  double total = 0;

  scanf("%d", &N);

  double heights[N + 1];
  double widths[N];

  for (int i = 0; i < N + 1; i++)
    scanf("%lf", &heights[i]);

  for (int i = 0; i < N; i++)
    scanf("%lf", &widths[i]);

  for (int i = N; i > 0; i--)
    total += formula(heights[i], heights[i - 1], widths[i - 1]);

  printf("%lf\n", total);

  return 0;
}
