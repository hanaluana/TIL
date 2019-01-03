---
title: Java Basic 1

---

## 직진 로봇 문제

```
![Robot Problem](TIL/imgs/robot1.png)
```

```java
package basicjava;
import java.util.Scanner;

public class Robot {
	
	static int findA (String [][] map, int s){
		int sum=0;
		for (int i=0;i<s;i++){
			for (int j=0;j<s;j++){
				if (map[i][j].equals("A")){
					//System.out.println(i+""+j);
					int j1 = j;
					while(j1<=(s-2) && map[i][j1+1].equals("S")){
						sum+=1;
						j1++;
					}
					System.out.println(i+" "+j+" "+sum);
				}
			}
		}
		return sum;
	}
	
	static int findB (String [][] map, int s){
		int sum=0;
		int temp1=0, temp2=0;
		for (int i=0;i<s;i++){
			for (int j=0;j<s;j++){
				if (map[i][j].equals("B")){
					temp1=0;temp2=0;
					int j1 = j;
					while(j1<=(s-2) && map[i][j1+1].equals("S")){
						temp1+=1;
						j1++;
					}
					j1 = j;
					while(j1>=1 && map[i][j1-1].equals("S")){
						temp2+=1;
						j1--;
					}
					if (temp1>temp2){
						sum+=temp1;
					}
					else{
						sum+=temp2;
					}
					System.out.println(i+" "+j+" "+temp2);
				}
			}
		}
		return sum;
	}
	
	static int findC (String [][] map, int s){
		int sum=0;
		int max=0, temp2=0;
		int i1, j1;
		for (int i=0;i<s;i++){
			for (int j=0;j<s;j++){
				if (map[i][j].equals("C")){
					max=0;temp2=0;
					i1=i; j1=j;
					while(j1<=(s-2) && map[i][j1+1].equals("S")){
						max+=1;
						j1++;
					}
					j1=j;
					while(j1>=1 && map[i][j1-1].equals("S")){
						temp2+=1;
						j1--;
					}
					j1=j;
					if (temp2>max){
						max=temp2;
					}
					temp2=0;
					while(i1>=1 && map[i1-1][j].equals("S")){
						temp2+=1;
						i1--;
					}
					i1=i;
					if (temp2>max){
						max=temp2;
					}
					temp2=0;
					while(i1<=(s-2) && map[i1+1][j].equals("S")){
						temp2+=1;
						i1++;
					}
					if (temp2>max){
						max=temp2;
					}
					System.out.println(i+" "+j+" "+max);
					sum+=max;
				}
			}
		}
		return sum;
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int sums[] = new int[n];
		
		for (int x=1;x<=n;x++){
			int s = sc.nextInt();
			String [][] map = new String[s][s];
			for (int i=0;i<s;i++){
				for (int j=0;j<s;j++){
					String m = sc.next();
					map[i][j]=m;
				}
			}
			//System.out.println(map[0][1].equals("A"));
			int sum=0;
			sum=findA(map, s)+findB(map,s)+findC(map,s);
			//System.out.println(findA(map,s)+""+findB(map,s)+""+findC(map,s));
			//System.out.println(sum);
			sums[x-1]=sum;
		}
		sc.close();
		for (int i=0;i<n;i++){
			System.out.println((i+1)+" "+sums[i]);
		}
	}
}

```

