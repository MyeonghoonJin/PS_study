import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/**
 * @Author : ljs
 * @Date : 2026. 01. 08.
 * @Description : 백준 15650
 * @Link : https://www.acmicpc.net/problem/15650
 */
public class Main {

    public static int[] arr;
    public static int N, M;
    public static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());    // 숫자 범위
        M = Integer.parseInt(st.nextToken());    // Depth

        arr = new int[M];    // 수열 결과

        dfs(1, 0);    // 재귀 호출
        System.out.println(sb);    // 결과 출력
    }

    /**
     * @param at    : 반복문 시작 지점
     * @param depth : 재귀의 깊이
     */
    public static void dfs(int at, int depth) {
        if (depth == M) {
            for (int val : arr) {
                sb.append(val + " ");
            }
            sb.append("\n");
            return;
        }

        for (int i = at; i <= N; i++) {    // 현재 Depth 트리 순회
            arr[depth] = i;    // 현재 깊이에 숫자 저장
            dfs(i + 1, depth + 1);    // 다음은 현재보다 큰 i+1부터 탐색
        }
    }
}
