/**
 * This program and the accompanying materials
 * are made available under the terms of the License
 * which accompanies this distribution in the file LICENSE.txt
 */
package com.archimatetool.editor.diagram.figures;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertNotNull;
import static org.junit.jupiter.api.Assertions.assertTrue;

import org.eclipse.draw2d.geometry.Point;
import org.eclipse.draw2d.geometry.Rectangle;

import com.archimatetool.editor.ParamsTest;


@SuppressWarnings("nls")
public abstract class AbstractTextControlContainerFigureTests extends AbstractContainerFigureTests {
    
    @ParamsTest
    public void testSetEnabled(AbstractTextControlContainerFigure figure) {
        assertTrue(figure.isEnabled());
        assertTrue(figure.getTextControl().isEnabled());
        
        figure.setEnabled(false);
        
        assertFalse(figure.isEnabled());
        assertFalse(figure.getTextControl().isEnabled());
    }
    
    @ParamsTest
    public void testGetText(AbstractTextControlContainerFigure figure) {
        assertEquals(figure.getDiagramModelObject().getName(), figure.getText());
        figure.getDiagramModelObject().setName("Fido");
        assertEquals("Fido", figure.getText());
    }

    @ParamsTest
    public void testGetTextControl(AbstractTextControlContainerFigure figure) {
        assertNotNull(figure.getTextControl());
    }
    
    @Override
    @ParamsTest
    public void testDidClickTextControl(AbstractDiagramModelObjectFigure figure) {
        Rectangle bounds = figure.getTextControl().getBounds().getCopy();
        figure.getTextControl().translateToAbsolute(bounds);
        assertTrue(figure.didClickTextControl(new Point(bounds.x + 10, bounds.y + 5)));
    }
    
}
