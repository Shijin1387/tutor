
"""Input Format

The first line contains an integer .

Output Format

Output the answer as explained in the task.

Sample Input 0

3
Sample Output 0

123
"""

from __future__ import print_function

if __name__ == '__main__':
    n = int(raw_input())
    i=1
    for i in range(1,n+1):
        print(i,end='')
    