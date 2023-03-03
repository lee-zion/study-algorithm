#include<iostream>
#include<queue>
#include<algorithm>
#include<vector>
#include<string.h>
#include<limits.h>
using namespace std;

int M, N, sy, sx, total;
char map[50][50];
int dy[4] = { 1,0,-1,0 };
int dx[4] = { 0,1,0,-1 };
int ans = INT_MAX;
int end_y, end_x;
vector<int> num;
struct INFO {
	int y, x;
}info[5];
queue<INFO> q;
int visited[50][50] = { 0 };

void bfs() {
	for (int i = 0; i < total; i++) {
		num.push_back(i);
	}
	//순열 만들어서 순서대로 탐색하여 가장 최소값 찾기
	do { //num[0] ~ num[total]
		q.push({ sy,sx });
		int tmp = 0;
		int cnt = 0;
		for (int k = 0; k < total; k++) {
			while (!q.empty()) {
				int size = q.size();
				for (int i = 0; i < size; i++) {
					int y = q.front().y;
					int x = q.front().x;
					q.pop();
					visited[y][x] = 1;
					if (y == info[num[k]].y && x == info[num[k]].x) { //현재 순열 X위치
						tmp += cnt;
						cnt = -1;
						while (!q.empty()) q.pop();
						memset(visited, 0, sizeof(visited));
						break;
					}
					for (int dir = 0; dir < 4; dir++) { //4방향 탐색
						int ny = y + dy[dir];
						int nx = x + dx[dir];
						if (ny < 0 || ny >= N || nx < 0 || nx >= M) continue;

						if (!visited[ny][nx] && map[ny][nx] != '#') {
							q.push({ ny, nx });
						}
					}
				}
				cnt++;
			}
			q.push({ info[num[k]].y, info[num[k]].x });
		}

		//X 다 찾고 현재 위치에서 목적지 E로 가기
		while (!q.empty()) {
			int size = q.size();
			for (int i = 0; i < size; i++) {
				int y = q.front().y;
				int x = q.front().x;
				q.pop();
				visited[y][x] = 1;
				if (y == end_y && x == end_x) {
					while (!q.empty()) q.pop();
					memset(visited, 0, sizeof(visited));
					tmp += cnt;
					break;
				}
				for (int dir = 0; dir < 4; dir++) { //4방향 탐색
					int ny = y + dy[dir];
					int nx = x + dx[dir];
					if (ny < 0 || ny >= N || nx < 0 || nx >= M) continue;

					if (!visited[ny][nx] && map[ny][nx] != '#') {
						q.push({ ny, nx });
					}
				}
			}
			cnt++;
		}

		ans = min(ans, tmp);
	} while (next_permutation(num.begin(), num.end()));
}

int main()
{
	cin >> M >> N;
	for (int y = 0; y < N; y++) {
		for (int x = 0; x < M; x++) {
			cin >> map[y][x];

			if (map[y][x] == 'S') {
				sy = y; sx = x;
			}
			else if (map[y][x] == 'X') {
				info[total].y = y;
				info[total++].x = x;
			}
			else if (map[y][x] == 'E') {
				end_y = y; end_x = x;
			}
		}
	}
	bfs();
	cout << ans;
	return 0;
}