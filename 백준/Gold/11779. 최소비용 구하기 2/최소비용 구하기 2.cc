#include<iostream>
#include<queue>
#include<functional> //greater
#include<algorithm> // fill


using namespace std;

#define X first
#define Y second

int v, e, st, en;


//{비용, 정점번호}
vector<pair<int, int>> adj[1005];
const int INF = 1e9 + 10;
int d[1005];//최단거리 테이블
int pre[1005];// 경로 복원용 테이블


void dijkstra(int st) {//시작점 입력
	priority_queue<pair<int, int>,
		vector<pair<int, int>>,
		greater< pair<int, int> >> pq;
	pq.push({d[st],st });
	while (!pq.empty()) {
		auto cur = pq.top();
		pq.pop();
		//해당 엣지가 오래된 것인지 체크.
		if (d[cur.Y] != cur.X)continue;
		// adj 노드들을 탐색하며. 업데이트
		for (auto next : adj[cur.Y]) {
			//해당 노드를 거쳐서 가는게 기존 dist보다 더싸면 업데이트
			if (d[next.Y] <= d[cur.Y] + next.X)continue;
			d[next.Y] = d[cur.Y] + next.X;
			pq.push({ d[next.Y], next.Y}); //영향 받았으니, 전파.
			pre[next.Y] = cur.Y;//어디서 왔는지 경로 저장.
		}


	}
}



int main(void) {
	ios::sync_with_stdio(0);
	cin.tie(0);
	cin >> v >> e;
	// 무한대 초기화
	fill(d, d + v + 1, INF); 
	
	//edge 푸쉬.
	while (e--) {
		int u, v, w;
		cin >> u >> v >> w; //w: cost. v: to
		adj[u].push_back({ w,v });
	}
	cin >> st >> en;

	d[st] = 0; // 시작점 추가.
	dijkstra(st);

	//최종 점에 거리 출력.
	cout << d[en] << "\n";

	// 경로 만들기.
	int cur = en;
	vector<int> path;
	while (cur != st) {
		path.push_back(cur);
		cur = pre[cur];
	}
	path.push_back(cur);
	
	//경로에 포함된 도시 개수.

	reverse(path.begin(), path.end());
	cout << path.size() << "\n";
	//최종 점 까지 경로 출력.
	for (int i = 0; i < path.size(); i++) {
		cout << path[i] << " ";
	}
	cout << "\n";

}
