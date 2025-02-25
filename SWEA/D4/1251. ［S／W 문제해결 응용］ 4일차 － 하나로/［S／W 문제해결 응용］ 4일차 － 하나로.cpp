/////////////////////////////////////////////////////////////////////////////////////////////
// 기본 제공코드는 임의 수정해도 관계 없습니다. 단, 입출력 포맷 주의
// 아래 표준 입출력 예제 필요시 참고하세요.
// 표준 입력 예제
// int a;
// float b, c;
// double d, e, f;
// char g;
// char var[256];
// long long AB;
// cin >> a;                            // int 변수 1개 입력받는 예제
// cin >> b >> c;                       // float 변수 2개 입력받는 예제 
// cin >> d >> e >> f;                  // double 변수 3개 입력받는 예제
// cin >> g;                            // char 변수 1개 입력받는 예제
// cin >> var;                          // 문자열 1개 입력받는 예제
// cin >> AB;                           // long long 변수 1개 입력받는 예제
/////////////////////////////////////////////////////////////////////////////////////////////
// 표준 출력 예제
// int a = 0;                            
// float b = 1.0, c = 2.0;               
// double d = 3.0, e = 0.0; f = 1.0;
// char g = 'b';
// char var[256] = "ABCDEFG";
// long long AB = 12345678901234567L;
// cout << a;                           // int 변수 1개 출력하는 예제
// cout << b << " " << c;               // float 변수 2개 출력하는 예제
// cout << d << " " << e << " " << f;   // double 변수 3개 출력하는 예제
// cout << g;                           // char 변수 1개 출력하는 예제
// cout << var;                         // 문자열 1개 출력하는 예제
// cout << AB;                          // long long 변수 1개 출력하는 예제
/////////////////////////////////////////////////////////////////////////////////////////////

#include<iostream>
#include<algorithm>
#include<vector>
#include<array>
#include <iomanip>
#include<math.h>
using namespace std;

using tu = array<long long, 3>;

using tnode = array<long long, 2>;

vector<tnode> nodes(1000);
vector<tu> edges(1000*1000);

int parents[1000];

vector<int>selected_edges;



int edge_count;

int Find(int x) {
	//부모노드가 자기 자신일때까지 타고올라가기.
	//그러면 최상위 부모를 리턴 받아서 루트를 알게됨.
	if (x == parents[x]) {
		return x;
	}

	return Find(parents[x]);



}

void Union(int a, int b) {
	
	int A = Find(a);
	int B = Find(b);


	parents[B] = A;

}




void kruskal(int edge_count) {

	for (int i = 0; i < edge_count; i++) {
		//불러오기/
		int from= edges[i][1];
		int to = edges[i][2];

		// union find 사이클 확인
		int from_par = Find(from);
		int to_par = Find(to);

		if (from_par != to_par) {
			//edge 추가하고. union.
			selected_edges.push_back(i);
			Union(from, to);
		}


	}


}






int main(int argc, char** argv)
{
	int test_case;
	int T;
	
	//freopen("input.txt", "r", stdin);
	cin >> T;
	
	for (test_case = 1; test_case <= T; ++test_case)
	{
		int N;
		double tax;
		cin >> N;

		selected_edges.clear();
		// N개 초기화
		
		for (int i = 0; i < N; i++) {
			int x;
			cin >> x;
			nodes[i][0] = x;
		}
		for (int i = 0; i < N; i++) {
			int y;
			cin >> y;
			nodes[i][1] = y;
		}
		//parents 배열 초기화
		for (int i = 0; i < N; i++) {
			parents[i] = i;
		}



		cin >> tax;
		
		// edge 생성
		edge_count = 0;
		for (int i = 0; i < N; i++) {
			for (int j = i+1; j < N; j++) {
				long long distance_x = abs(nodes[i][0] - nodes[j][0]);
				long long distance_y = abs(nodes[i][1] - nodes[j][1]);
				distance_x = distance_x * distance_x;
				distance_y = distance_y * distance_y;

				edges[edge_count] = { distance_x+ distance_y , i,j};
				edge_count++;
			}
		}

		sort(edges.begin(), edges.begin() + edge_count); //오름차순.
		
		//함수 호출
		kruskal(edge_count);


		//선택된 에지들의 가격합.
		double sum = 0;
		for (auto selected_edge : selected_edges) {
			sum = sum + edges[selected_edge][0];
		} 
		sum = round(sum * tax);
		
		cout <<"#" << test_case << " "<< fixed << setprecision(0) <<sum<<"\n";

	}
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}