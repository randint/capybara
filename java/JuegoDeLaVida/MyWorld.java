import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)
import java.util.ArrayList;
import java.util.Collections;
import java.awt.Color;
import java.awt.Point;

/**
 * Write a description of class MyWorld here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class MyWorld extends World
{
    private static int s = 10; // cell size
    private static ArrayList<Point> alive = new ArrayList<>();
    private static ArrayList<Point> buffer = new ArrayList<>();
    private static GreenfootImage display;

    private static Color aliveColor = Color.GREEN;
    private static Color deadColor = Color.LIGHT_GRAY;
    private static Color gridColor = Color.GRAY;

    /**
     * Constructor for objects of class MyWorld.
     * 
     */
    public MyWorld()
    {    
        // Create a new world with 600x400 cells with a cell size of 1x1 pixels.
        super(100*s, 80*s, 1);
        display = new GreenfootImage(getWidth(), getHeight());
        setBackground(display);
        randomize(10);
        update();
    }

    public MyWorld(int width, int height, int s)
    {
        super(width*s, height*s, 1);
        display = new GreenfootImage(getWidth(), getHeight());
        setBackground(display);
        randomize(10);
        update();
    }

    public void randomize(double percentAlive)
    {
        alive = new ArrayList<Point>();
        for (int x = 0; x < getWidth() / s; x++) {
            for (int y = 0; y < getHeight() / s; y++) {
                if (Greenfoot.getRandomNumber(101) < percentAlive) {
                    alive.add(new Point(x, y));
                }
            }
        }
    }

    public void update()
    {
        display.setColor(deadColor);
        display.fill();
        display.setColor(aliveColor);
        for (Point p : alive) {
            display.fillRect((int)p.getX()*s, (int)p.getY()*s, s, s);
        }
    }

    public void act()
    {
        buffer = new ArrayList(alive); // need ArrayList<Point>?
        ArrayList<Point> neighborCounts = new ArrayList<Point>();
        for (Point p : alive) {
            int x = (int)p.getX();
            int y = (int)p.getY();
            // consider neighbors; add to buffer if not in buffer
            for (int i = x - 1; i <= x + 1; i++) {
                for (int j = y - 1; j <= y + 1; j++) {
                    if (i != x && j != y) {
                        neighborCounts.add(new Point(i, j));
                    }
                }
            }
        }
        for (Point p : buffer) {
            int n = Collections.frequency(neighborCounts, p);
            if (alive.contains(p)) 
                if (n < 2 || n > 3) {
                alive.remove(n);
            }
            else if (n == 3) {
                alive.add(p);
            }
        }
        update();
    }

}
