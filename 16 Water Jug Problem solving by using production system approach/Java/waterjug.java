import java.util.*;

class Pair {
	int first, second;

	Pair(int f, int s) {
		first = f;
		second = s;
	}
}

public class waterjug {
	static void printpath(Vector<Pair> path) {
		int sz = path.size();
		for (int i = 0; i < sz; i++)
			System.out.println("(" + path.get(i).first +
					", " + path.get(i).second + ")");
	}

	static void bfs(int a, int b, int target) {
		int v[][] = new int[1000][1000]; // visited array
		for (int[] i : v) { // for each element i in array v fill -1(unvisited)
			Arrays.fill(i, -1);
		}

		boolean isSolvable = false;
		Vector<Pair> path = new Vector<Pair>();

		Queue<Pair> q = new LinkedList<Pair>();
		q.add(new Pair(0, 0));

		while (!q.isEmpty()) {

			Pair u = q.peek(); // retrieve the first element of the Queue

			q.poll(); // retrieve and delete

			if ((u.first > a || u.second > b || u.first < 0 || u.second < 0))
				continue;

			if (v[u.first][u.second] > -1) // visited, so skip this iteration of the loop
				continue;

			path.add(new Pair(u.first, u.second));

			v[u.first][u.second] = 1;

			if (u.first == target || u.second == target) {
				isSolvable = true;
				if (u.first == target) {
					if (u.second != 0)
						path.add(new Pair(u.first, 0));
				} else {
					if (u.first != 0)
						path.add(new Pair(0, u.second));
				}

				printpath(path);
				break;
			}

			q.add(new Pair(u.first, b));
			q.add(new Pair(a, u.second));

			for (int ap = 0; ap <= Math.max(a, b); ap++) {

				int c = u.first + ap;
				int d = u.second - ap;

				if (c == a || (d == 0 && d >= 0))
					q.add(new Pair(c, d));

				c = u.first - ap;
				d = u.second + ap;

				if ((c == 0 && c >= 0) || d == b)
					q.add(new Pair(c, d));
			}

			q.add(new Pair(a, 0));
			q.add(new Pair(0, b));
		}

		if (!isSolvable)
			System.out.print("No solution");
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter the capacity of first jug in L: ");
		int a = sc.nextInt();
		System.out.print("Enter the capacity of second jug in L: ");
		int b = sc.nextInt();
		System.out.println("Enter the target amount: ");
		int target = sc.nextInt();
		sc.close();
		bfs(a, b, target);
	}
}
