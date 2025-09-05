/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package parcial1;

import javax.swing.JFrame;
import javax.swing.*;
import java.awt.event.*;

/**
 *
 * @author esteb
 */
public class Parcial1 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        JFrame ventana = new JFrame("Calculadora de áreas");
        ventana.setSize(400,250);
        ventana.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        ventana.setLayout(null);
        
        JLabel lblTitulo = new JLabel("Seleccione la figura a calcular: ");
        lblTitulo.setBounds(130,30,200,30);
        ventana.add(lblTitulo);
        
        JButton btnCirculo = new JButton("Circulo");
        btnCirculo.setBounds(50, 80, 120, 30);
        ventana.add(btnCirculo);
        
        JButton btnCuadrado = new JButton("Cuadrado");
        btnCuadrado.setBounds(200, 80, 120, 30);
        ventana.add(btnCuadrado);

        JButton btnRectangulo = new JButton("Rectangulo");
        btnRectangulo.setBounds(50, 130, 120, 30);
        ventana.add(btnRectangulo);

        JButton btnTriangulo = new JButton("Triangulo");
        btnTriangulo.setBounds(200, 130, 120, 30);
        ventana.add(btnTriangulo);
        
        btnCirculo.addActionListener(e -> new parcial1.Formularios.FrmCirculo().setVisible(true));
        btnCuadrado.addActionListener(e -> new parcial1.Formularios.FrmCuadrado().setVisible(true));
        btnRectangulo.addActionListener(e -> new parcial1.Formularios.FrmRectangulo().setVisible(true));
        btnTriangulo.addActionListener(e -> new parcial1.Formularios.FrmTriangulo().setVisible(true));

        ventana.setVisible(true);
    }
    
}
