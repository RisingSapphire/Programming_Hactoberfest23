import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.io.*;
import java.nio.file.Files;
import java.nio.file.Paths;

public class NotepadApp extends JFrame implements ActionListener {
    private JTextArea textArea;
    private JFileChooser fileChooser;

    public NotepadApp() {
        setTitle("Notepad");
        setSize(600, 400);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        textArea = new JTextArea();
        fileChooser = new JFileChooser();
        fileChooser.setCurrentDirectory(new File("."));

        JMenuBar menuBar = new JMenuBar();
        JMenu fileMenu = new JMenu("File");
        JMenuItem openItem = new JMenuItem("Open");
        JMenuItem saveItem = new JMenuItem("Save");
        JMenuItem exitItem = new JMenuItem("Exit");

        openItem.addActionListener(this);
        saveItem.addActionListener(this);
        exitItem.addActionListener(this);

        fileMenu.add(openItem);
        fileMenu.add(saveItem);
        fileMenu.add(exitItem);
        menuBar.add(fileMenu);
        setJMenuBar(menuBar);

        JScrollPane scrollPane = new JScrollPane(textArea);
        scrollPane.setVerticalScrollBarPolicy(ScrollPaneConstants.VERTICAL_SCROLLBAR_ALWAYS);
        add(scrollPane);

        setLocationRelativeTo(null);
        setVisible(true);
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        if (e.getActionCommand().equals("Open")) {
            int returnVal = fileChooser.showOpenDialog(this);
            if (returnVal == JFileChooser.APPROVE_OPTION) {
                File file = fileChooser.getSelectedFile();
                try {
                    String content = new String(Files.readAllBytes(Paths.get(file.getAbsolutePath())));
                    textArea.setText(content);
                } catch (IOException ex) {
                    ex.printStackTrace();
                }
            }
        } else if (e.getActionCommand().equals("Save")) {
            int returnVal = fileChooser.showSaveDialog(this);
            if (returnVal == JFileChooser.APPROVE_OPTION) {
                File file = fileChooser.getSelectedFile();
                try {
                    BufferedWriter writer = new BufferedWriter(new FileWriter(file));
                    writer.write(textArea.getText());
                    writer.close();
                } catch (IOException ex) {
                    ex.printStackTrace();
                }
            }
        } else if (e.getActionCommand().equals("Exit")) {
            System.exit(0);
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> new NotepadApp());
    }
}
