
#include <iostream>
#include "RandomNumberGenerator.h"
#include <algorithm>
#include <list>

#define N 10
#define SEED 1
#define MAX 29


struct dane {
	int r;
	int p;
	int pi;
};

void s_c(dane tab[], int s[], int c[]);
void print(dane tab[], int s[], int c[]);
void generuj(dane tab[], RandomNumberGenerator& generator);
bool sort(dane arg1, dane arg2);
void print_tab(dane tab[]);

int main()
{
	RandomNumberGenerator generator(SEED);
	dane tab[N];
	generuj(tab, generator);
	print_tab(tab);
	int s[N];
	int c[N];
	s_c(tab, s, c);
	print(tab,s,c);

	std::sort(tab, tab+N, sort);
	s_c(tab, s, c);
	print(tab,s,c);
}

bool sort(dane arg1, dane arg2)
{
	return(arg1.r < arg2.r);
}

void generuj(dane tab[], RandomNumberGenerator& generator) {
	int sum = 0;
	for (int i = 0; i < N; i++)
	{
		int p = generator.nextInt(1, MAX);
		tab[i].p = p;
		sum += p;
		tab[i].pi = i;
	}
	for (int i = 0; i < N; i++)
	{
		int r = generator.nextInt(1, sum);
		tab[i].r = r;
	}
}


void s_c(dane tab[],int s[], int c[])
{
	s[0] = tab[0].r;
	c[0] = s[0] + tab[0].p;
	for (int i = 1; i < 10; i++)
	{
		s[i] = std::max(tab[i].r, c[i - 1]);
		c[i] = s[i] + tab[i].p;
	}
}

void print(dane tab[], int s[], int c[]) {

	std::cout << std::endl << "pi: ";
	for (int i = 0; i < N; i++)
	{
		std::cout << tab[i].pi << ", ";
	}
	std::cout << std::endl;
	std::cout << "s: ";
	for (int i = 0; i < N; i++)
	{
		std::cout << s[i] << ", ";
	}
	std::cout << std::endl;
	std::cout << "c: ";
	for (int i = 0; i < N; i++)
	{
		std::cout << c[i] << ", ";
	}
	std::cout << std::endl;
}

void print_tab(dane tab[]) {
	std::cout << "Seed: " << SEED << std::endl;
	std::cout << "Rozmiar problemu: " << N << std::endl;


	std::cout << "nr: ";
	for (int i = 0; i < N; i++)
	{
		std::cout << tab[i].pi << ", ";
	}
	std::cout << std::endl;
	std::cout << "r: ";
	for (int i = 0; i < N; i++)
	{
		std::cout << tab[i].r << ", ";
	}
	std::cout << std::endl;
	std::cout << "p: ";
	for (int i = 0; i < N; i++)
	{
		std::cout << tab[i].p << ", ";
	}
	std::cout << std::endl;
}