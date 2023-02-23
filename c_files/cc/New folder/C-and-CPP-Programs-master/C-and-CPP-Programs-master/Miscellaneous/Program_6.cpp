#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>
#include <time.h>
#include <assert.h>
#include <algorithm>
#include <iostream>
#include <queue>
#include <stack>
#include <vector>

using namespace std;

#define sp system("pause")
#define FOR(i,a,b) for(int i=a;i<=b;++i)
#define FORD(i,a,b) for(int i=a;i>=b;--i)
#define REP(i,n) FOR(i,0,(int)n-1)
#define MS0(x) memset(x,0,sizeof(x))
#define MS1(x) memset(x,1,sizeof(x))
#define SORT(a,n) sort(begin(a),begin(a)+n)
#define REV(a,n) reverse(begin(a),begin(a)+n)
#define ll long long
#define MOD 1000000007
#define gc getchar_unlocked
struct Edge{ int v, w; };

void main(){

	FILE *fp = fopen("data.txt", "w");
	int a[8] = { 1, 3, 5, 7, 9, 11, 13, 15 };
	REP(i, 8) REP(j, 8) REP(k, 8) REP(l, 8) REP(m, 8){
		int sum = a[i] + a[j] + a[k] + a[l] + a[m];
		fprintf(fp,"%d + %d + %d + %d + %d  = %d\n", a[i], a[j], a[k], a[l], a[m], sum);
	}
	fclose(fp);
	sp;
}