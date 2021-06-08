class Solution {
    public int countOrders(int n) {
        long x = 1;
        for(int i=1; i<=n; i++)x = x*i*(2*i-1)%1000000007;
        return (int)x;
    }
}