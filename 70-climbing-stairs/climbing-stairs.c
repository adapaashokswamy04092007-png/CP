int climb(int n , int memo[n+1])
{
    if(memo[n]==0)
    {
        memo[n]=climb(n-1,memo)+climb(n-2,memo);
    }
    return memo[n];
}
int climbStairs(int n) {
    int i;
    int memo[n+1];
    for(i=0;i<=n;i++)
    {
        memo[i]=0;
    }
    memo[0]=1;
    memo[1]=1;
    return climb(n,memo);
}
