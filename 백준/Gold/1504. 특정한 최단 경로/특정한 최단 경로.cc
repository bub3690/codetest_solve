#include<iostream>
#include<queue>
#include<climits>
#include<vector>

using namespace std;


vector<pair<int, int>> node[805];


long long dist1[805];
long long dist2[805];




int N, E;
int v1, v2;


void dijkstra(int v, long long arr[]) {
	priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>> > pq;
	pq.push({0,v});
	arr[v] = 0;
	while (!pq.empty()) {
		auto now = pq.top(); pq.pop();
		int now_cost = now.first;
		int now_pos = now.second;
		if (arr[now_pos] < now_cost) continue; //중복

		for (auto next_pair : node[now_pos]) {
			int next_cost = next_pair.second;
			int next_pos = next_pair.first;
			

			if (arr[next_pos] > next_cost+now_cost) {
				arr[next_pos] = next_cost + now_cost;
				pq.push({ arr[next_pos] ,next_pos });

			}

		}



	}


}


int main() {

	ios::sync_with_stdio(false);
	cin.tie(0);
	
	cin >> N >> E;
	

	
	for (int i = 0; i < E; i++) {
		int from, to, cost;
		cin >> from >> to >> cost;
		node[from].push_back({ to,cost });
		node[to].push_back({ from,cost });
	}

	cin >> v1 >> v2;

	// 초기화
	for (int i = 0; i <N+5 ; i++) {
		dist1[i] = INT_MAX;
		dist2[i] = INT_MAX;
	}
	

	// v1에서 전부 가는 방향 찾고.
	dijkstra(v1, dist1);
	// v2
	dijkstra(v2, dist2);

	//1->v1->v2->n
	long long dat1 = dist1[1] + dist1[v2] + dist2[N];
	//1->v2->v1->n 비교
	long long dat2 = dist2[1] + dist2[v1] + dist1[N];
	
	long long ans = min(dat1, dat2);
	if (ans >= INT_MAX) {
		ans = -1;
	}
	
	cout << ans << "\n";


	return 0;
}




