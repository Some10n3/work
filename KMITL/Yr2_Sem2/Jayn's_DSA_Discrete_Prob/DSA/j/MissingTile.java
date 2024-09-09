public class MissingTile {
  static class GridView implements Grid {
    private final Grid parentGrid;
    private final int topX;
    private final int topY;
    private final int size;
    private final int paintedX;
    private final int paintedY;

    public GridView(Grid parentGrid, int topX, int topY, int size, int paintedX, int paintedY) {
      this.parentGrid = parentGrid;
      this.topX = topX;
      this.topY = topY;
      this.size = size;
      this.paintedX = paintedX;
      this.paintedY = paintedY;
    }

    @Override
    public int size() {
      return size;
    }

    @Override
    public int getPaintedCellX() {
      return paintedX - topX;
    }

    @Override
    public int getPaintedCellY() {
      return paintedY - topY;
    }

    @Override
    public boolean setTile(int x, int y, int orientation) {
      return parentGrid.setTile(x + topX, y + topY, orientation);
    }

    @Override
    public boolean isFullyTiled() {
      return parentGrid.isFullyTiled();
    }

    public GridView subgrid(int subTopX, int subTopY, int subSize, int subpaintedX, int subPaintedY) {
      return new GridView(parentGrid, topX + subTopX, topY + subTopY, subSize, subpaintedX, subPaintedY);
    }
  }

  public static void tileGrid(Grid board) {
    tileGridHelper(board.size(), 0, 0, board.getPaintedCellX(), board.getPaintedCellY(), new GridView(board, 0, 0, board.size(), board.getPaintedCellX(), board.getPaintedCellY()));
  }

  private static void tileGridHelper(int size, int topX, int topY, int paintedX, int paintedY, GridView gridView) {
    if (size == 1) {
      return;
    }

    int half = size / 2;

    int paintedQuadrant = (paintedX < topX + half ? 0 : 1) + (paintedY < topY + half ? 0 : 0);
    int oppositeQuadrant = 3 - paintedQuadrant;

    for (int i = 0; i < 4; i++) {
      if (i != oppositeQuadrant) {
        int subTopX = (i % 2 == 0 ? 0 : half);
        int subTopY = (i < 2 ? 0 : half);
        int subPaintedX = (paintedX >= topX + half ? paintedX - (topX + half) : paintedX);
        int subPaintedY = (paintedY >= topY + half ? paintedY - (topY + half) : paintedY);
        
        GridView subgridView = gridView.subgrid(subTopX, subTopY, half, subPaintedX, subPaintedY);
        tileGridHelper(half, topX + subTopX, topY + subTopY, subPaintedX, subPaintedY, subgridView);
      }
    }

    int missingX = topX + (oppositeQuadrant % 2 == 0 ? half - 1 : half);
    int missingY = topY + (oppositeQuadrant < 2 ? half - 1 : half);
    int orientation = (oppositeQuadrant + 2) % 4;
    gridView.setTile(missingX, missingY, orientation);
  }

  public static void main(String[] args) {
    Grid board = new BasicBoard(4, 2, 1); 
    tileGrid(board);
  }
}
