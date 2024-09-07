import code.Coins;

public class L7_MinCoin_Main {
    
    public static void main(String[] args) {
        // ex1();
        int amount = 0;

        // for (amount = 4; amount < 12; amount++) { 
            // System.out.println("amount " + amount + " uses " + minNumCoin(amount));
        //     int [] minCoinResidual = new int[amount+1];
        //     System.out.println("amount " + amount + " uses " + minNumCoin(amount,minCoinResidual));
        // }
        fasterBy();
    }
    static void ex1() {
        for (Coins c : Coins.values()) {
            System.out.println("Coin " + c + "s are ready ");
        }
    }

    static int minNumCoin(int amount) {
        // System.out.println("call for " + amount);
        if (amount == 0) return 0; //base case

        int coinsNeeded = Integer.MAX_VALUE;
        
        int numCoin = 0;
        // int[] coinUsed = new int[amount + 1];
        // int size = 0;
        for (Coins c : Coins.values()) {
            if (c.value() <= amount) {
                numCoin = 1 + minNumCoin(amount - c.value());
                if (numCoin < coinsNeeded)coinsNeeded = numCoin; // This is the best because it finds the smallest amount of coins needed.
            }
        }
        return coinsNeeded;
    }
    static int minNumCoin(int amount, int [] residual) {
        if (amount == 0) return 0; //base case

        int coinsNeeded = Integer.MAX_VALUE;
        
        int numCoin = 0;
        for (Coins c : Coins.values()) {
            if (c.value() <= amount) {
                if (residual[amount -  c.value()] > 0)
                    numCoin = 1 + residual[amount - c.value()];
                else
                    numCoin = 1 + minNumCoin(amount - c.value(), residual);
                if (numCoin < coinsNeeded)
                    coinsNeeded = numCoin;
                residual[amount] = coinsNeeded; // This avoids the repeated calls.
            } 
        }
        return coinsNeeded;
    }
    static void fasterBy() {
        int amount = 70;
        long time = System.currentTimeMillis();
        System.out.print("amount = " + amount + " uses " + minNumCoin(amount));
        System.out.println(" elapse time = " + (int)(System.currentTimeMillis() - time));
        
        time = System.currentTimeMillis();
        int [] residual = new int [amount + 1];
        System.out.print("amount = " + amount + " uses " + minNumCoin(amount,residual));
        System.out.println(" elapse time = " + (int)(System.currentTimeMillis() - time));
    }
}

