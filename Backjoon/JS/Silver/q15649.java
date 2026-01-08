import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/**
 * @Author : ljs
 * @Date : 2026. 01. 09.
 * @Description : 백준 15649
 * @Link : https://www.acmicpc.net/problem/15649
 */
public class Main {
    public static int[] arr;
    public static boolean[] visited;
    public static int N, M;
    public static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        arr = new int[M];
        visited = new boolean[N + 1];

        dfs(0);
        System.out.println(sb);
    }

    /**
     * @param depth : 재귀의 깊이
     */
    public static void dfs(int depth) {
        if(depth == M) {
            for (int val : arr) {
                sb.append(val + " ");
            }
            sb.append("\n");
            return;
        }

        for(int i = 1; i <= N; i++) {
            if(!visited[i]) {
                visited[i] = true;
                arr[depth] = i;
                dfs(depth + 1);
                visited[i] = false;
            }
        }
    }
}