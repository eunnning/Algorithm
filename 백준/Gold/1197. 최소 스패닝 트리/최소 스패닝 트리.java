import java.util.PriorityQueue;
import java.util.Scanner;

public class Main {
	static int[] arr;
	static PriorityQueue<pEdge> q;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
	    int N = sc.nextInt(); // 노드의 수
	    int M = sc.nextInt(); // 간선의 수
	    q = new PriorityQueue<>();
	    arr=new int[N+1];
	    
	    for (int i = 0; i < N+1; i++) {
			arr[i]=i;
		}
	    
	    for (int i = 0; i < M; i++) {
	        int s = sc.nextInt();
	        int e = sc.nextInt();
	        int v = sc.nextInt();
	        q.add(new pEdge(s, e, v));
        }
	    
	    int sum=0;
	    int count=0;
	    
	    while ( count < N-1) {
	    	for (int i =1 ; i < M+1; i++) {
	    		pEdge node = q.poll();
				if (find(node.e) != find(node.s) ) {
					union(node.s, node.e);
					sum+=node.v;
					count++;
					
				}
			}
	    }
	    System.out.println(sum);
	    
	    
	}
	private static void union(int a, int b) {
		a= find(a);
		b= find(b);
		
		if (a != b)
			arr[b]=a;
		
	}
	private static int find(int a) {
		if (arr[a] != a)
			return arr[a]=find(arr[a]);
		return a;
	}
}
class pEdge implements Comparable<pEdge> {
	int s;
	int e;
	int v;
	
	pEdge( int s, int e, int v){
		this.s=s;
		this.e=e;
		this.v=v;
	}
	@Override
	  public int compareTo(pEdge o) {
	    return this.v - o.v;
	  }
}
