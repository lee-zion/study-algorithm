# 눈사태

사람들이 일직선으로 탁자에 앉아있다. 젓가락은 A,B,C,D 중 하나이며  각 사람이 가진 젓가락 쌍은 해당 사람의 위치를 인덱스로 하는 배열의 값과 같다. 이 때 젓가락은 반드시 옆 사람을 통해서만 옮길 수 있으며, 반드시 하나의 젓가락만을 주고 받아야 한다. 젓가락 짝을 맞추기까지 필요한 최소 교환횟수를 구하시오. 언제나 

# 입력

첫째 줄에 총 사람의 수 N(2 ≤ N ≤ 100)가 주어진다.
둘째 줄에 총 N명의 젓가락 상태가 공백으로 구분되어 주어진다.

# 출력

젓가락 짝을 맞추는데 필요한 교환횟수의 최소값을 출력한다.

## 예제 입력 1

```
2
AB BA
```

## 예제 출력 1

```
1
```

## 예제 입력 2

```
4
AB CD DC BA
```

## 예제 출력 2

```
5
```

## 예제 입력 3

```
4
AA AA AA AA
```

## 예제 출력 3

```
0
```