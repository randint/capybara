// WARNING: This file is auto-generated and any changes to it will be overwritten
import java.util.*;
import greenfoot.*;
import java.awt.Color;
import java.awt.Point;

/**
 * 
 */
public class MyWorld extends World
{
    private int w;
    private int h;
    private int iter;
    private ArrayList<Point> p =  new ArrayList();
    private GreenfootImage canvas;

    /**
     * 
     */
    public MyWorld()
    {
        super(601, 601, 1);
        canvas =  new GreenfootImage(getWidth(), getHeight());
        canvas.setColor(Color.MAGENTA);
        w = getWidth() - 1;
        h = getHeight() - 1;
        p.add( new Point(0, h / 4));
        p.add( new Point(w, h / 4));
        p.add( new Point(w / 2, h));
        setBackground(canvas);
        draw();
    }

    /**
     * 
     */
    public void draw()
    {
        int i = 0;
        while (i < p.size() - 2) {
            int x1 = (int)p.get(i).getX();
            int y1 = (int)p.get(i).getY();
            int x2 = (int)p.get((i + 1) % p.size()).getX();
            int y2 = (int)p.get((i + 1) % p.size()).getY();
            int x3 = (int)p.get((i + 2) % p.size()).getX();
            int y3 = (int)p.get((i + 2) % p.size()).getY();
            canvas.drawLine(x1, y1, x2, y2);
            canvas.drawLine(x2, y2, x3, y3);
            canvas.drawLine(x3, y3, x1, y1);
            i = i + 3;
        }
    }

    /**
     * 
     */
    public void koch()
    {
        ArrayList<Point> newP =  new ArrayList();
        int i = 0;
        while (i < p.size()) {
            int x1 = (int)p.get(i).getX();
            int y1 = (int)p.get(i).getY();
            int x2 = (int)p.get((i + 1) % p.size()).getX();
            int y2 = (int)p.get((i + 1) % p.size()).getY();
            newP.add( new Point());
            canvas.drawLine(x1, y1, x2, y2);
            i = i + 1;
        }
    }
}
