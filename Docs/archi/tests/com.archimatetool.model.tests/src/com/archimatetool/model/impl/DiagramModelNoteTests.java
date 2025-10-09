/**
 * This program and the accompanying materials
 * are made available under the terms of the License
 * which accompanies this distribution in the file LICENSE.txt
 */
package com.archimatetool.model.impl;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertNotSame;

import org.junit.jupiter.api.Test;

import com.archimatetool.model.IArchimateFactory;
import com.archimatetool.model.IDiagramModelComponent;
import com.archimatetool.model.IDiagramModelNote;
import com.archimatetool.model.ITextAlignment;


@SuppressWarnings("nls")
public class DiagramModelNoteTests extends DiagramModelObjectTests {
    
    private IDiagramModelNote note;
    
    @Override
    protected IDiagramModelComponent getComponent() {
        note = IArchimateFactory.eINSTANCE.createDiagramModelNote();
        note.setTextAlignment(ITextAlignment.TEXT_ALIGNMENT_LEFT);
        return note;
    }


    @Test
    public void testGetContent() {
        assertEquals("", note.getContent());
        note.setContent("This is it");
        assertEquals("This is it", note.getContent());
    }

    @Override
    @Test
    public void testGetDefaultTextAlignment() {
        assertEquals(ITextAlignment.TEXT_ALIGNMENT_LEFT, note.getTextAlignment());
    }
    
    @Override
    @Test
    public void testGetCopy() {
        super.testGetCopy();
        
        note.setContent("hello");
        
        IDiagramModelNote copy = (IDiagramModelNote)note.getCopy();
        
        assertNotSame(note, copy);
        assertEquals(note.getContent(), note.getContent());
    }

    @Test
    public void testGetBorderType() {
        assertEquals(0, note.getBorderType());
        note.setBorderType(1);
        assertEquals(1, note.getBorderType());
    }
    
    @Test
    public void testGetProperties() {
        CommonTests.testProperties(note);
    }


}
