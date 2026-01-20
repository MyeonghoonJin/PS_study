import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/**
 * @Author : ljs
 * @Date : 2026. 01. 19.
 * @Description : 백준 15652
 * @Link : https://www.acmicpc.net/problem/15652
 */
public class Main {
    public static int N, M;
    public static StringBuilder sb = new StringBuilder();
    public static int[] arr;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        arr = new int[M];

        dfs(0, 1);
        System.out.println(sb);
    }
    /**
     * @param depth : 재귀의 깊이
     * @param start : 루프를 시작할 숫자
     */
    public static void dfs(int depth, int start) {
        if(depth == M) {
            for(int val : arr) {
                sb.append(val + " ");
            }
            sb.append('\n');
            return;
        }
        for(int i = start; i <= N; i++) {
            arr[depth] = i;
            dfs(depth + 1, i);
        }
    }
}
