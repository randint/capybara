import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)
import java.awt.Point;
import java.awt.Color;
import java.util.ArrayList;

/**
 * Write a description of class MyWorld here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class MyWorld extends World
{
    private class Body
    {
        private double mass;
        private Vector pos;
        private Vector v;

    }

    private class Vector
    {
        public double x, y;

        public Vector(double x, double y)
        {
            this.x = x;
            this.y = y;
        }

        // Return a value in the range [0, 360)
        public double angle()
        {
            double theta = 0;
            if (x >= 0 && y >= 0) { // Quadrant I
                theta = Math.toDegrees(Math.asin(y / this.length()));
            }
            else if (x <= 0 && y >= 0) { // Quadrant II
                theta = 180 - Math.toDegrees(Math.asin(y / this.length()));
            }
            else if (x <= 0 && y <= 0) { // Quadrant III
                theta = 180 - Math.toDegrees(Math.asin(y / this.length()));
            }
            else { // Quadrant IV
                theta = 360 + Math.toDegrees(Math.asin(y / this.length()));
            }
            return theta % 360;
        }

        public double length()
        {
            return Math.sqrt(Math.pow(x, 2) + Math.pow(y, 2));
        }

        public double lengthSquared()
        {
            return Math.pow(x, 2) + Math.pow(y, 2);
        }
    }

    /**
     * Constructor for objects of class MyWorld.
     * 
     */
    public MyWorld()
    {    
        // Create a new world with 600x400 cells with a cell size of 1x1 pixels.
        super(400, 400, 1);
        int w = getWidth();
        int h = getHeight();
        int r = w * 3 / 8; // radius, distorted if world is not square
        Point o = new Point(w/2, h/2); // origin

        GreenfootImage bg = getBackground();
        bg.setColor(Color.BLACK);
        bg.drawOval(o.x - r, o.y - r, 2*r, 2*r);

        ArrayList<Point> pts = new ArrayList<Point>();
        pts.add(new Point(o.x + r, o.y)); // 0
        pts.add(new Point(o.x + (int)(r*Math.sqrt(3)/2), o.y - (int)(r*Math.sqrt(1)/2)));
        pts.add(new Point(o.x + (int)(r*Math.sqrt(2)/2), o.y - (int)(r*Math.sqrt(2)/2)));
        pts.add(new Point(o.x + (int)(r*Math.sqrt(1)/2), o.y - (int)(r*Math.sqrt(3)/2)));
        pts.add(new Point(o.x, o.y + r)); // pi/2
        pts.add(new Point(o.x - (int)(r*Math.sqrt(3)/2), o.y - (int)(r*Math.sqrt(1)/2)));
        pts.add(new Point(o.x - (int)(r*Math.sqrt(2)/2), o.y - (int)(r*Math.sqrt(2)/2)));
        pts.add(new Point(o.x - (int)(r*Math.sqrt(1)/2), o.y - (int)(r*Math.sqrt(3)/2)));       
        pts.add(new Point(o.x - r, o.y)); // pi
        pts.add(new Point(o.x - (int)(r*Math.sqrt(3)/2), o.y + (int)(r*Math.sqrt(1)/2)));
        pts.add(new Point(o.x - (int)(r*Math.sqrt(2)/2), o.y + (int)(r*Math.sqrt(2)/2)));
        pts.add(new Point(o.x - (int)(r*Math.sqrt(1)/2), o.y + (int)(r*Math.sqrt(3)/2)));                
        pts.add(new Point(o.x, o.y - r)); // 3pi/2
        pts.add(new Point(o.x + (int)(r*Math.sqrt(3)/2), o.y + (int)(r*Math.sqrt(1)/2)));
        pts.add(new Point(o.x + (int)(r*Math.sqrt(2)/2), o.y + (int)(r*Math.sqrt(2)/2)));
        pts.add(new Point(o.x + (int)(r*Math.sqrt(1)/2), o.y + (int)(r*Math.sqrt(3)/2)));        

        bg.setColor(Color.MAGENTA);
        for (Point p : pts) {
            bg.drawLine(o.x, o.y, p.x, p.y);
            Vector line = new Vector(p.x - o.x, p.y - o.y);
            double distance = line.length();
            double angle = line.angle();
            // this.showText(Long.toString(Math.round(distance)), p.x, p.y);
            this.showText(Long.toString(Math.round(angle)), p.x, p.y);
        }

    }

    public void act()
    {
        // apply forces
    }
}