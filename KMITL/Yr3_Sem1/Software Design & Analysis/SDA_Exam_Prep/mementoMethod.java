
import java.util.ArrayList;
import java.util.List;

class MementoMethod {
    public static void main(String[] args) {
        TextEditor textEditor = new TextEditor();
        textEditor.setState("Hello");
        textEditor.setState("Hello World");
        textEditor.setState("Hello World!!!");
        System.out.println(textEditor.getText());
        // textEditor.printMementoList();
        textEditor.undo();
        System.out.println(textEditor.getText());
        // textEditor.printMementoList();
        textEditor.undo();
        System.out.println(textEditor.getText());
        // textEditor.printMementoList();
    }
}

class Text {
    private String text;

    public void setText(String text) {
        this.text = text;
    }

    public Memento takeSnapshot(){
        return new Memento(this.text);
    }

    public void restoreFromSnapshot(Memento memento){
        this.text = memento.getSavedText();
    }

    @Override
    public String toString() {
        return text;
    }
}

class Memento {
    private final String text;

    public Memento(String text) {
        this.text = text;
    }

    public String getSavedText() {
        return text;
    }
}


class TextEditor {
    private Text text;
    private List<Memento> mementoList;

    public TextEditor() {
        this.mementoList = new ArrayList<>();
        this.text = new Text();
    }

    public void setState(String text) {
        this.text.setText(text);
        this.mementoList.add(this.text.takeSnapshot());
    }

    public void undo() {
        if (mementoList.size() < 2) {
            return;
        }
        text.restoreFromSnapshot(mementoList.get(mementoList.size() - 2));
        mementoList.remove(mementoList.size() - 1);
    }

    public String getText() {
        return text.toString();
    }

    public void printMementoList() {
        System.out.println("Memento List {");
        for (Memento memento : mementoList) {
            System.out.println(memento.getSavedText());
        }
        System.out.println("}");
    }
}