class ChildThread extends Thread {
    private int number;
    private int result;

    public ChildThread(int number) {
        this.number = number;
    }

    public int getResult() {
        return result;
    }

    @Override
    public void run() {
        result = 0;
        for (int i = 1; i <= 2 * number; i++) {
            result += i;
        }
    }
}

