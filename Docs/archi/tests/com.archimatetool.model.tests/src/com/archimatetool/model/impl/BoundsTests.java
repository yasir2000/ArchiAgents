/**
 * This program and the accompanying materials
 * are made available under the terms of the License
 * which accompanies this distribution in the file LICENSE.txt
 */
package com.archimatetool.model.impl;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import com.archimatetool.model.IArchimateFactory;
import com.archimatetool.model.IBounds;


public class BoundsTests {
    
    private IBounds bounds;
    
    @BeforeEach
    public void runBeforeEachTest() {
        bounds = IArchimateFactory.eINSTANCE.createBounds();
    }
    
    @Test
    public void testDefaultValues() {
        assertEquals(0, bounds.getX());
        assertEquals(0, bounds.getY());
        assertEquals(-1, bounds.getWidth());
        assertEquals(-1, bounds.getHeight());
    }
    
    @Test
    public void testSetValues() {
        bounds.setX(1);
        bounds.setY(2);
        bounds.setWidth(3);
        bounds.setHeight(4);
        
        assertEquals(1, bounds.getX());
        assertEquals(2, bounds.getY());
        assertEquals(3, bounds.getWidth());
        assertEquals(4, bounds.getHeight());
    }

    @Test
    public void testSetLocation() {
        bounds.setLocation(12, 14);
        
        assertEquals(12, bounds.getX());
        assertEquals(14, bounds.getY());
        assertEquals(-1, bounds.getWidth());
        assertEquals(-1, bounds.getHeight());
    }
    
    @Test
    public void testSetSize() {
        bounds.setSize(100, 200);
        
        assertEquals(0, bounds.getX());
        assertEquals(0, bounds.getY());
        assertEquals(100, bounds.getWidth());
        assertEquals(200, bounds.getHeight());
    }
    
}
